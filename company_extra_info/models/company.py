from odoo import models, fields, api
from odoo.exceptions import ValidationError


class company(models.Model):
    _inherit = 'res.company'
    fax = fields.Char('Fax')
    extra_info = fields.Text('Extra Information')

