import frappe
from frappe.utils import cint

@frappe.whitelist()
def get_total_card(type):
    total = frappe.db.sql(f"SELECT SUM(amount) total FROM `tabExpense Record` WHERE type='{type}'", as_dict=True)
    return cint(total[0].total) if any(total) else 0
