# Copyright (c) 2023, husam hammad and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Property(Document):
	def after_insert(self):
		frappe.msgprint(f'Document {self.name} inserted successfully')


	def validate(self):
		try:
			frappe.db.sql(""" SELECT name , tenant, friends FROM `tabProperty`; """)
		except Exception as e:
			error = frappe.log_error(frappe.get_traceback(),f"{e}")
			frappe.msgprint((f"An error occurred <a href='/app/error-log/{error.name}'><b>{error.name}</b></a>"))



	# def validate(self):
	# 	if(self.property_type == "Flat"):
	# 		for amenity in self.amenities:
	# 			if(amenity.amenity == "Deck"):
	# 				frappe.throw((f'''Property of type <b> Flat </b>
	# 				should not have amenity <b> {amenity.amenity} </b>'''))
