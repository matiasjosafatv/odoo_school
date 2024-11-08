
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
        ('ab_negative', 'AB-')]
    )
    rs_teacher = fields.Boolean('Teacher?')