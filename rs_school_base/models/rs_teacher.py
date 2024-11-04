
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
    