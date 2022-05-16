# -*_ encoding: utf-8 -*-
from odoo import http

class hospital(http.Controller):
    #SAMPLE CONTROLLER CREATED
    @http.route('/hospital/patient/', website=True, auth="public")
    def hospital_appointment(self, **kw):
        import pdb
        pdb.set_trace()
        return "Hello User, Welcome to Appointment Model"
