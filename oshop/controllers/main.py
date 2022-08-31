from odoo.http import Controller, request, route

# Controllers for odoo is same as route in Flask

class LaunchShopOrderController(Controller):
    
    def get_product(self, product_id):
        """
        It will get the product from `product.product` model and
        :param product_id:
        :return: product
        """
        return request.env['product.product'].search([('id', '=', int(product_id))])

    def get_current_order(self):
        """
        @return: orders from `shop.order` that are in draft state
        """
        return request.env['shop.order'].search([('state', '=', 'draft')])

    def get_order_line(self, order, product_id):
        """
        :param order: current order
        :param product_id: product_id
        :return: order_id and product_id from `shop.order.line` model
        """
        return request.env['shop.order.line'].search([('order_id', '=', order.id), ('product_id', '=', product_id)])


    def add_order_line(self, order, product, qty):
        """
        :return: create new order_line
        """
        vals = {
            'order_id': order.id,
            'product_id': product.id,
            'price': (int(qty) * product.list_price),
            'product_uom_type': int(qty),
        }
        return request.env['shop.order.line'].create(vals)

    def add_order(self):
        vals = {'partner_id': request.env.user.id}
        return request.env['shop.order'].create(vals)

    def set_order_done(self, order):
        if order.state == 'draft':
            order['state'] = 'done'
        return True
    
    @route('/search', methods=['POST', 'GET'], type='json', auth='user')
    def search_product(self, name):
        """
        `/search` is route/controller defined in `o_shop.js` as a Search Owl Component.
        which triggers `search_product` method when Search button clicked and onSearch JS
        methods gets called with routing `/search`.

        @return:: product_list
        """
        product_list = []
        products = request.env['product.product'].search([('check', '=', True), ('name', 'ilike', name)])

        for product in products:
            vals = {
                'id': product.id,
                'name': product.name,
                'price': product.list_price
            }
            product_list.append(vals)
        return {'products': product_list}

    @route('/add_to_cart', methods=['GET', 'POST'], type='json', auth='user')
    def add_to_cart(self, product_id):
        qty = 1
        vals = []
        product = self.get_product(product_id)
        order = self.get_current_order()
        print("product_id :------>,", product_id)

        if order:
            line = self.get_order_line(order, product_id)
            if line:
                line.product_uom_type += qty
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
                'qty': line.product_uom_type,
                'price': line.price
            })
        return {'order_lines': vals}
    
    @route('/remove_from_cart', methods=['POST', 'GET'], type='json', auth='user')
    def remove_from_Cart(self, product_id):
        order = self.get_current_order()
        vals = []
        if order:
            line = self.get_order_line(order, product_id)
            if line:
                line.unlink()
            for line in order.order_lines:
                vals.append({
                    'id': line.product_id.id,
                    'name': line.product_id.name,
                    'qty': line.product_uom_type,
                    'price': line.price
                })
            if not order.order_lines:
                order.unlink()
        return {'order_lines': vals}

    @route('/checkout', methods=['POST', 'GET'], type='json', auth='user')
    def checkout(self):
        order = self.get_current_order()
        order_lines = []
        price = 0

        if order:
            for line in order.order_lines:
                order_lines.append({
                    'name': line.product_id.name,
                    'qty': line.product_uom_type,
                    'price': line.price
                })
                price += line.price

            vals = {
                'products': order_lines,
                'total': price
            }

            self.set_order_done(order)
            return {'order_detail': vals}
