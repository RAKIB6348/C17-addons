from odoo import api, fields, models
from datetime import date


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient Record'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', tracking=True)
    age = fields.Integer(string='Age', compute='_compute_age')
    gender = fields.Selection([('male','Male'),
                               ('female','Female'),
                               ], string='Gender', tracking=True)
    date_of_birth = fields.Date(string='Date of Birth', tracking=True)


    @api.onchange('date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.age = today.year - rec.date_of_birth.year
            else:
                rec.age = 0