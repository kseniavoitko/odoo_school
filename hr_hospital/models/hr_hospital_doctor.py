from odoo import models, fields


class HrHospitalDoctor(models.Model):
    _name = 'hr_hospital.doctor'
    _description = 'Hospital doctor'
    _inherit = 'hr_hospital.person'

    name = fields.Char(required=True)
    active = fields.Boolean(
        default=True, )
    specialization = fields.Char(required=True)
    visit_ids = fields.One2many('hr_hospital.visit',
                                inverse_name='doctor_id')
    is_intern = fields.Boolean('is intern')
    intern_id = fields.Many2one('hr_hospital.doctor',
                                string='Intern',
                                domain=[('is_intern', '=', True)])
    mentor_id = fields.Many2one('hr_hospital.doctor',
                                string='Mentor',
                                domain=[('is_intern', '=', False)])
