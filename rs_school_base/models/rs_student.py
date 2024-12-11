
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
        ('ab_negative', 'AB-'),],

        groups = "rs_school_base.rs_school_base_students_admin"
    )
    student_account_number = fields.Char(string='Account Number',readonly=True)

    # rs_teacher = fields.Boolean('Teacher?')

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            next_san_seq = self.env['ir.sequence'].next_by_code('rs_student')
            vals['student_account_number'] = next_san_seq
        return super().create(vals_list)




class ResPartner(models.Model):
    _inherit = 'res.partner'

#     @api.model
#     def read(self, fields=None, load='_classic_read'):

#         result = super(ResPartner, self).read(fields=fields, load=load)

#         if fields and 'name' in fields:
#             for record in result:
#                 if record['name'] == 'Matias':
#                     group_student_admin = self.env.ref('rs_school_base.rs_school_base_students_admin')
#                     if group_student_admin in self.env.user.groups_id:
#                         raise UserError(_('Ejele no te dejo ver a Matias'))

#         return result





#         # # Agregar lógica personalizada después de llamar al método original
#         # for record in result:
#         #     if 'name' in record:
#         #         record['name'] = record['name'].upper()  # Ejemplo: convertir nombres a mayúsculas

#         return result


    @api.model
    def read(self, fields=None, load='_classic_read'):
        # Agregar lógica personalizada antes de llamar al método original
        if fields and 'name' in fields:
            self.env['mail.message'].create({
                'body': 'Se ha accedido a datos de partner',
                'subject': 'Lectura de datos',
                'model': 'res.partner',
                'res_id': self.id,
            })

        # Llamar al método original
        result = super(ResPartner, self).read(fields=fields, load=load)

        # # Agregar lógica personalizada después de llamar al método original
        # for record in result:
        #     if 'name' in record:
        #         record['name'] = record['name'].upper()  # Ejemplo: convertir nombres a mayúsculas

        return result


    def write(self, values):
        """
            Update all record(s) in recordset, with new value comes as {values}
            return True on success, False otherwise

            @param values: dict of new values to be set

            @return: True on success, False otherwise
        """
        # import wdb;wdb.set_trace()
        # group_student_admin = self.env.ref('rs_school_base.rs_school_base_students_admin')
        # if group_student_admin in self.env.user.groups_id:
        #     raise UserError(_('Ejele no te dejo escribir por que eres administrador de Estudiantes'))
        #     return False
        result = super(ResPartner, self).write(values)

        return result


    def unlink(self):
        """
            Delete all record(s) from recordset
            return True on success, False otherwise

            @return: True on success, False otherwise

            #TODO: process before delete resource
        """
        import wdb;wdb.set_trace()
        # group_student_admin = self.env.ref('rs_school_base.rs_school_base_students_admin')
        # if group_student_admin in self.env.user.groups_id:
        #     raise UserError(_('Ejele no te dejo borrar por que eres administrador de Estudiantes'))
        #     return False
        if self.env.user.id == 6:
            raise UserError(_('Ejele no te dejo borrar por que eres usuario id 3'))
            return False
        result = super(ResPartner, self).unlink()

        return result
