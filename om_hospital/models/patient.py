from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', tracking=True)
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([('male','Male'),
                               ('female','Female'),
                               ], string='Gender', tracking=True)
    date_of_birth = fields.Date(string='Date of Birth', tracking=True)