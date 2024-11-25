
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class RsStudent(models.Model):
    _inherit = 'res.partner'

    rs_student = fields.Boolean('Student?')
    rs_blood_type = fields.Selection(
        string='Blood Type',
        selection=[('a_positive', 'A+'),
        ('a_negative', 'A-'),
        ('b_positive', 'B+'),
        ('b_negative', 'B-'),
        ('o_positive', 'O+'),
        ('o_negative', 'O-'),
        ('ab_positive', 'AB+'),
        ('ab_negative', 'AB-'),]
    )
    student_account_number = fields.Char(string='Account Number',readonly=True)

    # rs_teacher = fields.Boolean('Teacher?')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            next_san_seq = self.env['ir.sequence'].next_by_code('rs_student')
            vals['student_account_number'] = next_san_seq
        return super().create(vals_list)




