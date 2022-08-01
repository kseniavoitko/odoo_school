from datetime import date
from odoo import models, fields, _


class AppointDoctorWizard(models.TransientModel):
    _name = 'appoint.doctor.wizard'
    _description = 'Appoint personal doctor'

    def default_patient(self):
        return self.env['hr_hospital.patient'].browse(self._context.get('active_ids'))

    patient_ids = fields.Many2many('hr_hospital.patient',
                                   string='Patients',
                                   default=default_patient)
    doctor_id = fields.Many2one('hr_hospital.doctor', string='Doctor')

    def action_appoint(self):
        for record in self.patient_ids:
            record.doctor_id = self.doctor_id
