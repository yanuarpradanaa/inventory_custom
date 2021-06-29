# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Inventory_custom(models.Model):
	_inherit = 'stock.picking'

	product_uomx = fields.Many2one(related="move_lines.product_uom",string="Unit of Measure")

	@api.onchange('product_id')
	def description(self):
		if self.product_id:
			cat = self.product_id.categ_id.name
			self.product_description = "{} {}".format(cat, self.product_id.name)

# Tabline Initial Demand
class stock_move(models.Model):
	_inherit = 'stock.move'

	product_description = fields.Char(string="Description")

	@api.onchange('product_id')
	def description(self):
		if self.product_id:
			cat = self.product_id.categ_id.name
			self.product_description = "{} {}".format(cat, self.product_id.name)

# Tabline Operation
class stock_pack_ops(models.Model):
	_inherit = 'stock.pack.operation'

	@api.onchange('product_id')
	def description(self):
		if self.product_id:
			cat = self.product_id.categ_id.name
			self.product_description = "{} {}".format(cat, self.product_id.name)