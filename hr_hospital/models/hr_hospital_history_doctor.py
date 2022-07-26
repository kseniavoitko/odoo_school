from odoo import models, fields


class HrHospitalHistoryDoctor(models.Model):
    _name = 'hr_hospital.history.doctor'
    _description = "History of personal doctor"

    date = fields.Date('Date')
    patient_id = fields.Many2one('hr_hospital.patient')
    doctor_id = fields.Many2one('hr_hospital.doctor')
