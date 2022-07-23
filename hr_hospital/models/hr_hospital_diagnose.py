from odoo import models, fields


class HrHospitalDiagnose(models.Model):
    _name = 'hr_hospital.diagnose'
    _description = 'Hospital diagnose'

    name = fields.Char()

    active = fields.Boolean(
        default=True, )
