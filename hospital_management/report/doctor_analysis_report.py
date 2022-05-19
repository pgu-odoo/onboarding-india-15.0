from odoo import models,fields,tools

class PatientAnalysis(models.Model):
    _name = 'patient.analysis'
    _auto = False

    patient_name = fields.Char('Patient Name')
    parent_ids = fields.Many2one(comodel_name='res.partner',string='Parent Name')
    gender = fields.Selection([('male','Male'),
                               ('female','Female'),
                               ('other','Other')],string='Gender')
    doctor_ids = fields.Many2one(comodel_name='hospital.doctor',string='Doctor Name')
    total = fields.Float(string='Total Bill')

    def init(self):
        """
        This is an init method which will be used to create a view in postgresql
        ----------------------------------------------------------------------------------------------
        :return:
        """
        tools.drop_view_if_exists(self._cr,self._table)
        self.env.cr.execute("""
            CREATE OR REPLACE VIEW patient_analysis AS (
                SELECT 
            )
        """)