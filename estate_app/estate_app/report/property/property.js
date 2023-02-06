// Copyright (c) 2023, husam hammad and contributors
// For license information, please see license.txt
/* eslint-disable */



frappe.query_reports["Property"] = {
	"filters": [
		{
			"fieldname":"Property",
			"label":__("Property Name"),
			"fieldtype":"Data",
			"width":100,
			"read":0,
		},
		{
			"fieldname":"from",
			"label":__("From Date"),
			"fieldtype":"Date",
			"width":100,
			"read":0,
			"default":dateutil.year_start()
		},
		{
			"fieldname":"to",
			"label":__("To Date"),
			"fieldtype":"Date",
			"width":100,
			"read":0,
		},
		{
			"fieldname":"agent",
			"label":__("Agent Name"),
			"fieldtype":"Link",
			"options":"Agent",
			"width":100,
			"read":0,
		},
		{
			"fieldname":"status",
			"label":__("Status"),
			"fieldtype":"Select",
			"options":['Sale','Rent','Lease'],
			"width":100,
			"read":0,
		}
	]
};
