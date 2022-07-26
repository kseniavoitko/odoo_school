from odoo import models, fields


class HrHospitalVisit(models.Model):
    _name = 'hr_hospital.visit'
    _description = "Doctor's visit"

    name = fields.Char()
    visit_date = fields.Datetime('Date')
    patient_id = fields.Many2one('hr_hospital.patient', string='Patient')
    doctor_id = fields.Many2one('hr_hospital.doctor', string='Doctor')
    diagnose_id = fields.Many2one('hr_hospital.diagnose', string='Diagnose')
    recommendation = fields.Text()
    research_ids = fields.Many2many('hr_hospital.research')
