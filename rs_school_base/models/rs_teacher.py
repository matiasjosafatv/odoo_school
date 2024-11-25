
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError


class RsTeacher(models.Model):
    _inherit = 'res.partner'

    rs_teacher = fields.Boolean('Teacher?')

    teacher_account_number = fields.Char(string='Account Number',readonly=True)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            next_san_seq = self.env['ir.sequence'].next_by_code('rs_teacher')
            vals['teacher_account_number'] = next_san_seq
        return super().create(vals_list)

