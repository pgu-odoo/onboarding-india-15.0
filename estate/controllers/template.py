# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class RealEstateController(http.Controller):

    @http.route([
                    '/estate',
                    '/estate/page/<int:page>'
                ],
                type='http', auth='public', website=True)
    def index(self, page=1 , search = '', **post):
        #for number of properties per page
        limit = 6

        #domain to obtain available properties
        domain = [
                    ('state','in',['new','offer_received'])
                ]

        #for Listed After DatePicker
        if post.get('my_date'):
            domain.append(('create_date','>=',post.get('my_date')))

        #for search (not used right now)
        if search:
            domain.append(('name', 'ilike', search))
        if search:
            post["search"] = search

        #for publish management
        if not http.request.env.user.has_group('estate.group_estate_admin'):
            domain.append(('is_published','=','True'))

        #requesting all properties in object
        properties = http.request.env['estate.property']

        #total number of properties with the domain applied
        total = properties.search_count(domain)

        #pager code [
        #            url is our path , 
        #            total is the total number of records in pager,
        #            page is the default page number,
        #            step is the total number of records per page
        #           ]
        pager = request.website.pager(
                                        url= '/estate',
                                        total=total,
                                        page=page,
                                        step=limit,
                                    )
        #offset is for the next page to start from the last record of previous page + 1
        offset = pager['offset']

        return request.render('estate.index', {
                                                'search': search,
                                                'properties': properties.search(domain, limit=limit, offset=offset, order='is_published desc, create_date desc'),
                                                'pager': pager,
                                            })

    @http.route('/estate/<model("estate.property"):name>', type='http', auth="public", website=True)
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
