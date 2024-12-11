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

    def action_rs_registration_action(self):
        res = self.env.ref('rs_school_base.view_rs_registration_list')
        return {
                   "view_mode": 'list',
                   'res_model': 'rs.registration',
                   'type': 'ir.actions.act_window',
                   'view_id': res.id,
                   'target': 'new',
                   'domain': [('session_ids','in',self.ids)],
                   }
