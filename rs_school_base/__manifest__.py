
# -*- coding: utf-8 -*-
###############################################################################
#
#    jeffery CHEN fan<jeffery9@gmail.com>
#
#    Copyright (c) All rights reserved:
#        (c) 2017  TM_FULLNAME
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses
#
#    Odoo and OpenERP is trademark of Odoo S.A.
#
###############################################################################
{
    'name': 'Realsystems School Management',
    'summary': 'Designed to manage school items',
    'version': '1.0',

    'description': """The School Management module is designed to streamline administrative tasks within educational institutions. It includes comprehensive features for managing student enrollments, scheduling classes, organizing student information, and setting up timetables. This module enables schools to efficiently handle day-to-day operations, ensuring that both administrators and educators have a clear overview of class schedules, student records, and enrollment status. By centralizing school management, this module reduces manual work and improves operational efficiency across the board.


    """,

    'author': 'Real Systems ',
    'maintainer': 'Matias Josafat Vera martinez',
    'contributors': ['Matias Josafat Vera martinez <matiasjosafatv@gmail.com>'],

    'website': 'https://github.com/matiasjosafatv/odoo_school.git',

    'license': 'AGPL-3',
    'category': 'Uncategorized',

    'depends': [
        'base'
    ],
    'external_dependencies': {
        'python': [
        ],
    },
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/ir_rule_data.xml',

        "views/rs_class_views.xml",
        "views/rs_registration_views.xml",
        "views/rs_student_views.xml",
        "views/rs_teacher_views.xml",
        "views/res_users_views.xml",

        "views/rs_school_base_menu_views.xml",
    ],
    'demo': [
    ],
    'js': [
    ],
    'css': [
    ],
    'qweb': [
    ],
    'images': [
    ],
    'test': [
    ],

    'installable': True
}
