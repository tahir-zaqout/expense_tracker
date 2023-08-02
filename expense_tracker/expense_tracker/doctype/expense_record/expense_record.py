# Copyright (c) 2023, tahir zaqout and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class ExpenseRecord(Document):
	def before_save(self):
		self.formatted_amount = float(self.amount) if self.type == "Credit" else (0 - float(self.amount))
