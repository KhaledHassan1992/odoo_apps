# -*- coding: utf-8 -*-

from odoo import api,fields,models,_
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = "sale.order"


    @api.one
    @api.constrains('order_line')
    def check_constraint_quantity(self):
        for record in self:
            if record.order_line:
                for product_ids in record.order_line:
                    product = product_ids.product_id.id
                    maximum_order_quantity = self.env['product.product'].browse(product).maximum_order_quantity
                    if product_ids.product_uom_qty > maximum_order_quantity:
                        raise ValidationError(_(
                            'Maximum order quantity of the product' + product_ids.name + ' is ' + str(
                                maximum_order_quantity)))
