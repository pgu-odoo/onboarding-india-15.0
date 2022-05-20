from odoo import models,fields,api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    company_id = fields.Many2one(comodel_name='res.company',string='Company')

    #COMPANY'S FIELD
    def_patient_amount = fields.Float('Default Amount',
                                      related='company_id.def_patient_amount',
                                      readonly=False)

    #SYSTEM PARAMETER FIELD
    def_patient_amount2 = fields.Float('Default Amount 2',
                                       config_parameter='hospital_management.default_amount2')

    #GROUP
    group_grp_patient_admin =  fields.Boolean('Hospital Admin', implied_group='hospital_management.hospital_admin_grp')

    #MODULE
    module = fields.Boolean('Sale')