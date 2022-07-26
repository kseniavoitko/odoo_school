from datetime import date
from odoo import models, fields, api


class HrHospitalPatient(models.Model):
    _name = 'hr_hospital.patient'
    _description = 'Hospital patient'
    _inherit = 'hr_hospital.person'

    name = fields.Char(required=True)
    active = fields.Boolean(
        default=True, )
    birthday = fields.Date('Date of Birth')
    age = fields.Integer(compute='_compute_age', tracking=True)
    passport_id = fields.Char('Passport No', tracking=True)
    passport_date = fields.Date('Date of passport issue', tracking=True)
    passport_authority = fields.Char('Authority', tracking=True)
    partner_id = fields.Many2one('res.partner', string='Contact')
    doctor_id = fields.Many2one('hr_hospital.doctor', string='Personal Doctor')
    visit_ids = fields.One2many('hr_hospital.visit',
                                inverse_name='patient_id')
    history_doctor_ids = fields.One2many('hr_hospital.history.doctor',
                                         inverse_name='patient_id')

    @api.depends('birthday')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.birthday:
                rec.age = today.year - rec.birthday.year
            else:
                rec.age = 1

    @api.onchange('doctor_id')
    def onchange_doctor_id(self):
        for rec in self:
            lines = []
            vals = {
                'date': date.today(),
                'patient_id': rec.id,
                'doctor_id': rec.doctor_id
            }
            lines.append((0, 0, vals))
            rec.history_doctor_ids = lines
