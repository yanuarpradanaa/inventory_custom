# -*- coding: utf-8 -*-
from odoo import models, fields, api

class account_custom(models.Model):
	_inherit = 'account.invoice.line'

	@api.onchange('product_id')
	def name_custom(self):
		if self.product_id:
			cat = self.product_id.categ_id.name
			self.name = "{} {}".format(cat, self.product_id.name)