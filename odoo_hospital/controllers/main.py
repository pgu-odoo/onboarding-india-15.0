# from asyncio.constants import SENDFILE_FALLBACK_READBUFFER_SIZE
# from httplib2 import Authentication
from odoo import http
from odoo.http import request

class HospitalController(http.Controller):
    @http.route('/hospital/patient', website=True, auth='public')  #three type auth value : auth='public' (page is access by anyone),auth='user'(page is access by login user ),auth='non'
    def hospital_doctors(self,**kw):
        # return "Welcome To My Odoo !"
        patient_details= request.env['hospital.patients'].sudo().search([])
        return request.render("odoo_hospital.patient_page",{'objects':patient_details,
            'root':'/hospital/patient'})
        # return request.render("odoo_hospital.doctor_page",{
        #     'objects': http.request.env['odoo_hospital.HospitalDoctor'].sudo().search([]),
        # })

# class Restrict(HospitalController):
#     @http.route(auth='user')
#     def hospital_doctor(self):
#         return super(Restrict, self).hospital_doctors()