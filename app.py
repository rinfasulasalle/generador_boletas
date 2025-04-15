from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice
import os
os.environ["INVOICE_LANG"] = "es"
# Datos de factura
client = Client('John Doe')
provider = Provider('ABC Inc',logo_filename = 'imgs/logo.png')
creator = Creator('John Doe2')

invoice = Invoice(client, provider, creator)
invoice.currency = 'S/'


# Ítems
invoice.add_item(Item(10, 2, description="Eggs"))
invoice.add_item(Item(4, 3, description="Milk"))
invoice.add_item(Item(10, 2, description="Eggs"))
invoice.add_item(Item(4, 3, description="Milk"))
invoice.add_item(Item(10, 2, description="Eggs"))
invoice.add_item(Item(4, 3, description="Milk"))
invoice.add_item(Item(10, 2, description="Eggs"))
invoice.add_item(Item(4, 3, description="Milk"))
invoice.add_item(Item(10, 2, description="Eggs"))

pdf = SimpleInvoice(invoice)
pdf.gen("invoice.pdf")