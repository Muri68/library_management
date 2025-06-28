# Copyright (c) 2025, Isyaku Murtala and contributors
# For license information, please see license.txt


import frappe
from frappe.model.document import Document
from frappe import _

class Librarian(Document):
    def before_insert(self):
        if not self.email:
            frappe.throw(_("Email is required"))

        # Check if User exists
        if not frappe.db.exists("User", self.email):
            user = frappe.get_doc({
                "doctype": "User",
                "email": self.email,
                "first_name": self.full_name,
                "send_welcome_email": 1,
                "roles": [{"role": "Librarian"}]
            })
            user.insert(ignore_permissions=True)
            self.user = user.name
        else:
            self.user = self.email
            