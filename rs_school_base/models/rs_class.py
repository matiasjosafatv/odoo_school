from odoo import models, fields, api, exceptions

class RSClass(models.Model):
    _name='rs.class'
    _rec_name='course_name'
    _description='Classes for Sessions'

    #defaults

    course_name = fields.Char(string="Course", required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Course Taker", index=True)
    session_ids = fields.One2many('rs.registration', 'course_id', string='Sessions')

    rs_location = fields.Selection(
        string='Location',
        selection=[('one', 'Santa Ursula'), ('two', 'Avante')],
        groups = "rs_school_base.rs_class_manager"
    )



    count_sessions = fields.Integer(string='Session Count',
        compute='_compute_session_ids' )

    #Methods

    @api.depends('session_ids')
    def _compute_session_ids(self):
        for record in self:
            record.count_sessions = len(record.session_ids)





    def action_rs_registration_action_view(self):
        res = self.env.ref('rs_school_base.view_rs_registration_list')
        return {
                   "view_mode": 'list',
                   'name': f'Registrations from {self.display_name}',
                   'res_model': 'rs.registration',
                   'type': 'ir.actions.act_window',
                   'view_id': res.id,
                   'target': 'self',
                   'context': {'default_course_id': self.id,
                                  'default_session_name': 'New Course by Obj View',
                                },
                   'domain': [('course_id','in',self.ids)],

                   }

    def action_rs_registration_action(self):
        action = self.env.ref('rs_school_base.rs_registration_action')
        action_dict = action._get_action_dict()
        action_dict['context'] = {
            **self.env.context,
            'default_course_id': self.id,
            'default_session_name': 'New Course',
        }
        action_dict['domain'] = [('course_id','in',self.ids)]
        return action_dict

    def action_registration_action_two(self):
        action = self.env.ref('rs_school_base.rs_registration_action')
        action_dict = action._get_action_dict()
        action_dict['context'] = {
            **self.env.context,
            'default_course_id': self.id,
            'default_session_name': 'New Course',
        }
        action_dict['domain'] = [('course_id','in',self.ids)]
        return action_dict

