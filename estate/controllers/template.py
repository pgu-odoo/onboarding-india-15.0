# -*- coding: utf-8 -*-
from odoo import http

class Academy(http.Controller):

    @http.route('/estate', auth='public', website=True)
    def index(self, **kw):
        Properties = http.request.env['estate.property']

        return http.request.render('estate.index', {
             'properties': Properties.search([])
         })

    @http.route('/estate/<model("estate.property"):name>', auth="public", website=True)
    def property(self, name):
        return http.request.render('estate.property_details', {
            'property' : name
        })


######################## Extras ##############################

    # @http.route('/estate/<int:id>/', auth='public', website=True)
    # def property(self, id):
    #     return '<h1>{} ({})</h1>'.format(id, type(id).__name__)

    # @http.route('/estate/<name>/', auth='public', website=True)
    # def property(self, name):
    #     return '<h1>{}</h1>'.format(name)