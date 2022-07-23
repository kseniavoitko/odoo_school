from odoo import models, fields


class HrHospitalPatientCard(models.Model):
    _name = 'hr_hospital.patient.card'
    _description = 'Hospital patient card'

    name = fields.Char()

    active = fields.Boolean(
        default=True, )
