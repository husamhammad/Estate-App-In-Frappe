import frappe
import frappe.tests.utils
import frappe.defaults

def get_context(context):
    print(f"\n\n\n\n\n\n {frappe.form_dict}\n\n\n\n\n\n\n")
    try:
        docname = frappe.form_dict.docname;
        context.property = frappe.get_doc("Property",frappe.form_dict.docname) ;
        context.agent = frappe.get_doc("Agent", context.property.agent);
        realted_properties = frappe.db.sql(f"""SELECT creation, name , property_name , status , address , grand_total ,
        image FROM `tabProperty` WHERE property_type = '{context.property.property_type}' ORDER BY creation DESC LIMIT 3 ;
        """, as_dict=True);
        context.realted_properties = realted_properties

    except Exception as e:

        frappe.local.flags.redirect_location = '/404'
        raise frappe.Redirect

   
    return context