from odoo import models, fields

class Subject(models.Model):
    _name = 'school.subject'
    _description = 'Subject'

    name = fields.Char(string="Subject Name", required=True)
    teacher_id = fields.Many2one('school.teacher', string="Teacher")