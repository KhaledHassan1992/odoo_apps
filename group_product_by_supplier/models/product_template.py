# -*- coding: utf-8 -*-
from odoo import models, api, fields, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    supplier_id = fields.Many2one('res.partner', string="Supplier",
                                  compute='_compute_supplierinformation', store=True)

    @api.depends('seller_ids')
    def _compute_supplierinformation(self):
        for product in self:
            if len(product.seller_ids) > 0:
                product.supplier_id = product.seller_ids[0].name.id
