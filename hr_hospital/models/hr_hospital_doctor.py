from odoo import models, fields


class HrHospitalDoctor(models.Model):
    _name = 'hr_hospital.doctor'
    _description = 'Hospital doctor'

    name = fields.Char()

    active = fields.Boolean(
        default=True, )
