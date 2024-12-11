from odoo import models, fields, api, exceptions

class RSClass(models.Model):
    _name='rs.class'
    _rec_name='course_name'

    course_name = fields.Char(string="Course", required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Course Taker", index=True)
    session_ids = fields.One2many('rs.registration', 'course_id', string='Sessions')

    rs_location = fields.Selection(
        string='Location',
        selection=[('one', 'Santa Ursula'), ('two', 'Avante')],
        groups = "rs_school_base.rs_class_manager"
    )
