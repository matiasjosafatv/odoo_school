from odoo import models, fields, api, _
from datetime import timedelta
from odoo.exceptions import UserError, ValidationError


class RsRegistration(models.Model):
	_name='rs.registration'
	_rec_name='session_name'
 
	session_name= fields.Char(required=True)
	start_date = fields.Date(default=fields.Date.context_today)
	duration = fields.Float(digits=(6,2), help="Duration in days", default= 1.0)
	seats = fields.Integer(string="Number of seats")
	active = fields.Boolean(default=True)
	color = fields.Integer()
	instructor_id = fields.Many2one('res.partner', string='Course Instructor', 
                                    domain=[('rs_teacher', '=', True)])
    
	course_id = fields.Many2one('rs.class', ondelete='cascade', string='Course', required=True)
    
	attendee_ids = fields.Many2many('res.partner', string="Attendees")
    
	state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done','Done')])
 
	attendees_count = fields.Integer(string='Attendees Count', compute='calc_attendees', store=True)
 
	hours = fields.Float(string="Duration in hours", compute='calc_hours', inverse='set_hours')
 
	end_date = fields.Date(string="End Date", store=True, compute='get_end_date',inverse='set_end_date')
 
	@api.onchange('start_date')
	def _onchange_start_date(self):
		if self.start_date:
			today= fields.Date.today(self)
			if self.start_date < today:
				raise ValidationError(_('You cannot have a start date before Today'))

	@api.depends('attendee_ids')
	def calc_attendees(self):
		for rec in self:
			rec.attendees_count = len(rec.attendee_ids)
   
	@api.onchange('seats','attendee_ids')
	def verify_valid_seats(self):
		if self.seats < 0:
			return {
				'warning': { 
					'title': "Incorrect amount for seats",
					'message': "No. of seats can't be negative"
				},
			}
		if self.seats < len(self.attendee_ids):
			return {
				'warning': {
					'title': "Too many Attendees",
					'message': "More Attendees than seats"
				}
			}
   
	@api.constrains('instructor_id', 'attendee_ids')
	def check_instructor_not_in_attendees(self):
		for rec in self:
			if rec.instructor_id and rec.instructor_id in rec.attendee_ids:
				raise ValidationError("The Instructor cannot be an attendee")

	@api.depends('duration')
	def calc_hours(self):
		for rec in self:
			rec.hours = rec.duration * 24

	def set_hours(self):
		for rec in self:
			rec.duration = rec.hours / 24
   
	@api.depends('duration', 'start_date')
	def get_end_date(self):
		for record in self:
			if not(record.start_date and record.duration):
				record.end_date = record.start_date
			else:
				record.end_date = fields.Date.add(record.start_date,days=record.duration)
   
	def set_end_date(self):
		for rec in self:
			if rec.end_date:
				if not rec.start_date and rec.duration:
					rec.start_date = fields.Date.add(rec.end_date,days=-rec.duration)
				else:
					if rec.start_date and not rec.duration:
						start_date = rec.start_date
						end_date = rec.end_date
						rec.duration = (end_date - start_date).days + 1
					else:
						rec.duration = 1.0					
						rec.start_date = fields.Date.add(rec.end_date,days=-rec.duration)
   