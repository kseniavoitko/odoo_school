from odoo import models, fields, api


class HrHospitalDiagnose(models.Model):
    _name = 'hr_hospital.diagnose'
    _description = 'Hospital diagnose'

    name = fields.Char(required=True)
    active = fields.Boolean(
        default=True, )
    doctor_id = fields.Many2one(comodel_name='hr_hospital.doctor', string='Doctor')
    patient_id = fields.Many2one(comodel_name='hr_hospital.patient', string='Patient')
    sickness_id = fields.Many2one(comodel_name='hr_hospital.sickness', string='Sickness')
    sickness_category_id = fields.Many2one(comodel_name='hr_hospital.sickness.category',
                                           compute='_compute_sickness_category',
                                           string='Sickness Category',
                                           store=True)
    therapy = fields.Text()
    diagnose_date = fields.Date('Date of Diagnose')
    mentor_id = fields.Many2one(comodel_name='hr_hospital.doctor',
                                string='Mentor',
                                domain=[('is_intern', '=', False)])
    comment = fields.Text()
    research_ids = fields.Many2many(comodel_name='hr_hospital.research')
    qty = fields.Integer(default=1, )
    grade_of_sick = fields.Selection([
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
    ], tracking=True, default='1')

    @api.onchange('doctor_id')
    def onchange_doctor_id(self):
        for rec in self:
            rec.mentor_id = rec.doctor_id.mentor_id

    @api.depends('sickness_id')
    def _compute_sickness_category(self):
        for rec in self:
            rec.sickness_category_id = rec.sickness_id.sickness_category_id
