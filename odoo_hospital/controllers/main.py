# from asyncio.constants import SENDFILE_FALLBACK_READBUFFER_SIZE
# from httplib2 import Authentication
from odoo import http
from odoo.http import request

class HospitalController(http.Controller):
    @http.route(['/hospital/patient','/hospital/patient/page/<int:page>'], website=True, auth='public')  #three type auth value : auth='public' (page is access by anyone),auth='user'(page is access by login user ),auth='non'
    def hospital_patient(self,page=0, **kw):
        # return "Welcome To My Odoo !"
        import pdb
        pdb.set_trace()
        patient_model=request.env['hospital.patients']
        customer_obj = request.env['hospital.patients'].sudo().search([])
        total =customer_obj.sudo().search_count([])
        pager = request.website.pager(
                    url='/hospital/patient',
                    total=total,
                    page=page,
                    step=5,
                )
        
        offset = pager['offset']
        customer_obj = customer_obj[offset: offset + 5]
        return request.render('odoo_hospital.patient_page', {
        'customer_details': customer_obj,
        'pager': pager,
        'root':'/hospital/patient'
        })
        # patient_details= request.env['hospital.patients'].sudo().search([],offset=pager['offset'] ,limit=10)
        
        


        # return request.render("odoo_hospital.patient_page",{'objects':patient_details,
        #     'root':'/hospital/patient'})
        # return request.render("odoo_hospital.doctor_page",{
        #     'objects': http.request.env['odoo_hospital.HospitalDoctor'].sudo().search([]),
        # })
    
    @http.route('/hospital/patient/<model("hospital.patients"):obj>/', auth='public', website=True)
    def object(self, obj, **kw):
        return http.request.render('odoo_hospital.patient_form_page', {
            'root': '/hospital/appointment',
            'object' : obj
        })

    @http.route('/hospital/appointment/<model("hospital.appointment"):obj>/', auth='public', website=True)
    def hospital_appoitment(self,obj,**kw):
        return http.request.render('odoo_hospital.appointment_page',{
            'appo': obj
        })

# class Restrict(HospitalController):
#     @http.route(auth='user')
#     def hospital_patient(self):
#         return super(Restrict, self).hospital_patient()