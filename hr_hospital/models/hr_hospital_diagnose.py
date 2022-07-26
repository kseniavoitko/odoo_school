from odoo import models, fields, api


class HrHospitalDiagnose(models.Model):
    _name = 'hr_hospital.diagnose'
    _description = 'Hospital diagnose'

    name = fields.Char(required=True)
    active = fields.Boolean(
        default=True, )
    doctor_id = fields.Many2one('hr_hospital.doctor', string='Doctor')
    patient_id = fields.Many2one('hr_hospital.patient', string='Patient')
    sickness_id = fields.Many2one('hr_hospital.sickness', string='Sickness')
    therapy = fields.Text()
    diagnose_date = fields.Date('Date of Diagnose')
    mentor_id = fields.Many2one('hr_hospital.doctor',
                                string='Mentor',
                                domain=[('is_intern', '=', False)])
    comment = fields.Text()
    research_ids = fields.Many2many('hr_hospital.research')

    @api.onchange('doctor_id')
    def onchange_doctor_id(self):
        for rec in self:
            rec.mentor_id = rec.doctor_id.mentor_id
