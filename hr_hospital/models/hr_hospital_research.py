from odoo import models, fields


class HrHospitalResearch(models.Model):
    _name = 'hr_hospital.research'
    _description = 'Research'

    name = fields.Char()
    date = fields.Date()
    active = fields.Boolean(
        default=True, )
    patient_id = fields.Many2one('hr_hospital.patient', string='Patient')
    patient_telephone_number = fields.Char(related='patient_id.telephone_number')
    research_type_id = fields.Many2one('hr_hospital.research.type')
    doctor_id = fields.Many2one('hr_hospital.doctor', string='Doctor')
    sample_id = fields.Many2one('hr_hospital.sample', string='Sample')
    sample_type_id = fields.Many2one('hr_hospital.sample.type', string='Sample Type',
                                     related='sample_id.sample_type_id',
                                     store=True)
    conclusion = fields.Text()
    qty = fields.Integer(default=1, )
