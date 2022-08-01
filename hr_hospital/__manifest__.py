{
    'name': "Hospital",
    'summary': "Hospital",

    'author': "Ksenia Voitko",

    'category': 'Customizations',
    'license': 'OPL-1',
    'version': '15.0.1.0.0',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/hr_hospital_menus.xml',
        'views/hr_hospital_diagnose_views.xml',
        'views/hr_hospital_research_views.xml',
        'views/hr_hospital_visit_views.xml',
        'views/hr_hospital_doctor_views.xml',
        'views/hr_hospital_patient_views.xml',
        'views/hr_hospital_sickness_category_views.xml',
        'views/hr_hospital_research_type_views.xml',
        'views/hr_hospital_sample_views.xml',
        'views/hr_hospital_sample_type_views.xml',
        'wizard/appoint_doctor_wizard_views.xml',
    ],

}
