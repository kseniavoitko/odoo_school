from odoo import models, fields


class HrHospitalSickness(models.Model):
    _name = 'hr_hospital.sickness'
    _description = 'Sickness'

    name = fields.Char()
    active = fields.Boolean(
        default=True, )
    sickness_category_id = fields.Many2one('hr_hospital.sickness.category')
