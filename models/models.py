from odoo import models, fields, api

class course(models.Model):
	_name = 'openacademy.course'
	_description = "Openacademy Course"

	name = fields.Char(string="Title", required=True)
	description = fields.Text()




	