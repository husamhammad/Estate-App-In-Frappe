# Copyright (c) 2023, husam hammad and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
from frappe import _
import frappe


def execute(filters=None):
	return get_columns(), get_data(filters)


def get_data(filters):
	
	_from, to = filters.get('from'), filters.get('to')  #Data rang
	# conditions 
	conditions = " AND 1=1 "
	if(filters.get('property')):conditions += f" AND name LIKE '%{filters.get('property')}'"
	if(filters.get('agent')):conditions += f" AND agent='{filters.get('agent')}'"
	if(filters.get('status')):conditions += f" AND status='{filters.get('status')}'"


	print(f"\n\n\n\n\n\n\n\n{conditions}\n\n\n\n\n\n\n\n")

	data = frappe.db.sql(f"""SELECT name, property_name, address,
	 property_type, status, property_price, discount, grand_total, agent , agent_name
	  FROM `tabProperty` WHERE (creation BETWEEN '{_from}' AND '{to}') {conditions}; """)
	return data

def get_columns():
	return [
		"ID:Link/Property:70",
		"Property Name:Data:150",
		"Address:Data:120",
		"Type:Data:80",
	    "Status:Data:120",
		"Price:Currency:120",
		"Discount:Percent:120",
		"Grand Total:Currency:130",
		"Agent:Data:100",
		"Agent Name:Data:120",

	]