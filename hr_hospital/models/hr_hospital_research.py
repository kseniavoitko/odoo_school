from odoo import models, fields


class HrHospitalResearch(models.Model):
    _name = 'hr_hospital.research'
    _description = 'Research'

    name = fields.Char()
    active = fields.Boolean(
        default=True, )
    patient_id = fields.Many2one('hr_hospital.patient', string='Patient')
    research_type_id = fields.Many2one('hr_hospital.research.type')
    doctor_id = fields.Many2one('hr_hospital.doctor', string='Doctor')
    sample_id = fields.Many2one('hr_hospital.sample', string='Sample')
    conclusion = fields.Text()
