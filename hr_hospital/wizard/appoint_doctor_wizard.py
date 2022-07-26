from odoo import models, fields


class AppointDoctorWizard(models.TransientModel):
    _name = 'appoint.doctor.wizard'
    _description = 'Appoint personal doctor'

    def default_patient(self):
        return self.env['hr_hospital.patient'].browse(self._context.get('active_id'))

    patient_ids = fields.Many2many('hr_hospital.patient',
                                   string='Patients',
                                   default=default_patient)
    doctor_id = fields.Many2one('hr_hospital.doctor', string='Doctor')

    def action_open_wizard(self):
        return {
            'name': _('Appoint personal doctor'),
            'type': 'ir.actions.act_window',
            'res_model': 'appoint.doctor.wizard',
            'view_mode': 'form',
            'target': 'new',
        }

    def action_appoint(self):
        for record in self.patient_ids:
            record.doctor_id = self.doctor_id
