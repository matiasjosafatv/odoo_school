
# -*- coding: utf-8 -*-
###############################################################################
#    License, author and contributors information in:                         #
#    __manifest__.py file at the root folder of this module.                  #
###############################################################################

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError



class ResUsers(models.Model):
    _inherit = 'res.users'


    rs_location = fields.Selection(
        string='Location',
        selection=[('one', 'Santa Ursula'), ('two', 'Avante')],
        default='one'
    )
