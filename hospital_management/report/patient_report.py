from odoo import models,fields,api

class PatientReport(models.AbstractModel):
    _name = 'report.patient.report_patient'
    _description = 'Patient Report'

    @api.model
    def _get_report_values(self,docids,data=None):
        if not docids:
            docids = data['docids']
        return {
            'doc_ids'
        }