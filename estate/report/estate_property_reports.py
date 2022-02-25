# -*- coding: utf-8 -*-

from odoo import models, fields, api

class EstatePropertyReport(models.AbstractModel):
    _name = "report.estate.report_property_offers"
    _description = "report"

    @api.model
    def _get_report_values(self, docids, data=None):
        records_data = self.env['estate.property'].browse(docids)
        return {
            'doc_ids' : records_data.ids,
            'doc_model' : 'estate.property',
            'records_data' : records_data,
        }