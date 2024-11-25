from odoo import models, fields

class Schedule(models.Model):
    _name = 'school.schedule'
    _description = 'Schedule'

    class_id = fields.Many2one('school.class', string="Class", required=True)
    subject_id = fields.Many2one('school.subject', string="Subject", required=True)
    time = fields.Datetime(string="Time", required=True)