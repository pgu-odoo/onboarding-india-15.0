# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
import datetime
import uuid

from odoo.http import Controller, request, route


class LunchOrderController(Controller):

    def get_current_order(self):
        return request.env['lunch.order'].search([('state', '=', 'draft')])

    def get_order_line(self, order, product_id):
        return request.env['lunch.order.line'].search([('order_id', '=', order.id), ('product_id', '=', product_id)])

    def get_product(self, pid):
        return request.env['product.product'].search([('id', '=', int(pid))])

    def add_order_line(self, order, product, qty):
        vals = {
            'order_id': order.id,
            'product_id': product.id,
            'price': (int(qty) * product.list_price),
            'product_uom_qty': int(qty),
        }
        return request.env['lunch.order.line'].create(vals)

    def add_order(self):
        vals = {
            'partner_id': request.env.user.id
        }
        return request.env['lunch.order'].create(vals)

    def set_order_done(self, order):
        if order.get('state') == 'draft':
            order['state'] = 'done'
        return True

    @route('/search', methods=['POST', 'GET'], type='json', auth='user')
    def search_product(self, name):
        product_list = []
        products = request.env['product.product'].search([('lunch_ok', '=', True), ('name', 'ilike', name)])
        for p in products:
            vals = {
                'id': p.id,
                'name': p.name,
                'price': p.list_price
            }
            product_list.append(vals)
        return {'products': product_list}

    @route('/add_to_cart', methods=['GET', 'POST'], type='json', auth='user')
    def add_to_cart(self, p_id):
        qty = 1
        vals = []
        product = self.get_product(p_id)
        order = self.get_current_order()

        if order:
            line = self.get_order_line(order, product.id)
            if line:
                line.product_uom_qty += qty
                line.price += (qty * product.list_price)
            else:
                self.add_order_line(order, product, qty)
        else:
            order = self.add_order()
            self.add_order_line(order, product, qty)

        for line in order.order_lines:
            vals.append({
                'id': line.product_id.id,
                'name': line.product_id.name,
                'qty': line.product_uom_qty,
                'price': line.price
            })
        return {'order_lines': vals}

    @route('/remove_from_cart', methods=['GET', 'POST'], type='json', auth='user')
    def remove_from_cart(self, pid):
        order = self.get_current_order()
        vals = []
        if order:
            line = self.get_order_line(order, pid)
            if line:
                line.unlink()           
            for line in order.order_lines:
                vals.append({
                    'id': line.product_id.id,
                    'name': line.product_id.name,
                    'qty': line.product_uom_qty,
                    'price': line.price
                })
            if not order.order_lines:
                order.unlink()
        return {'order_lines': vals}


    @route('/checkout', methods=['GET', 'POST'], type='json', auth='user')
    def checkout(self):
        order = self.get_current_order()
        order_lines = []
        price = 0

        if order:
            for line in order.order_lines:
                order_lines.append({
                    'name': line.product_id.name,
                    'qty': line.product_uom_qty,
                    'price': line.price
                })
                price += line.price
            
            vals = {
                'products': order_lines,
                'total': price           }

            self.set_order_done(order)
            return {'order_detail': vals}

    