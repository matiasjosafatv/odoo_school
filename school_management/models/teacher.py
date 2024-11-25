from odoo import models, fields

class Teacher(models.Model):
    _name = 'school.teacher'
    _description = 'Teacher'

    name = fields.Char(string="Name", required=True)
    subject_ids = fields.Many2many('school.subject', string="Subjects")