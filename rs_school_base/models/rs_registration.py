from odoo import models, fields, api, exceptions
from datetime import timedelta

class RsRegistration(models.Model):
	_name='rs.registration'
	_rec_name='session_name'
 
	session_name= fields.Char(required=True)
	start_date = fields.Date()
	duration = fields.Float(digits=(6,2), help="Duration in days")
	seats = fields.Integer(string="Number of seats")
	active = fields.Boolean(default=True)
	color = fields.Integer()
	instructor_id = fields.Many2one('res.partner', string='Course Instructor', 
                                    domain=[('rs_teacher', '=', True)])
    
	course_id = fields.Many2one('rs.class', ondelete='cascade', string='Course', required=True)
    
	attendee_ids = fields.Many2many('res.partner', string="Attendees")
    
	state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done','Done')])