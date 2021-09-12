

from odoo import api, fields, models, _

class ProductTemplate(models.Model):
    _inherit = "product.template"



    maximum_order_quantity = fields.Float(string='Maximum Order Quantity',help="This field display maximum order qunatity")