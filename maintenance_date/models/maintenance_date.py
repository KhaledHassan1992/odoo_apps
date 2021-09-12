# -*- encoding: utf-8 -*-
from openerp import models, fields, api, _
import datetime as dt


class MaintainTime(models.Model):
    _inherit = "account.asset.asset"
    maintenance_date = fields.Datetime(string="Maintenance Due Date", required=True, )

    asset_code = fields.Char(string='Code', required=True, copy=False, readonly=True, index=True,
                               default=lambda self: _('New'))

    warn_date = fields.Datetime(string="Warranty Date",)

    @api.model
    def create(self, vals):
        if vals.get('asset_code', _('New')) == _('New'):
            vals['asset_code'] = self.env['ir.sequence'].next_by_code('manage.asset.sequence') or _('New')
        return super(MaintainTime, self).create(vals)


