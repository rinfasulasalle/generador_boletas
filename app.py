from datetime import date
import os
os.environ["INVOICE_LANG"] = "es"

from InvoiceGenerator.api import Invoice, Item, Client, Provider, Creator
from InvoiceGenerator.pdf import SimpleInvoice

# Datos del cliente y proveedor
client = Client('John Doe', address="Av. Siempre Viva 123, Springfield", email="john@example.com", phone="987654321")
provider = Provider('ABC Inc',
                    bank_account='123456789',
                    bank_code='001',
                    address='Jr. Comercio 456, Lima',
                    email='contacto@abc.com',
                    phone='012345678',
                    logo_filename='imgs/logo.png')

creator = Creator('Administrador del Sistema')

# Crear factura
invoice = Invoice(client, provider, creator)
invoice.currency = 'S/'
invoice.title = "FACTURA ELECTRÓNICA"
invoice.date = date.today()

# Agregar ítems
invoice.add_item(Item(10, 2, description="Huevos"))
invoice.add_item(Item(4, 3, description="Leche"))
invoice.add_item(Item(7.5, 1, description="Pan"))
invoice.add_item(Item(12.3, 5, description="Queso"))

# Generar PDF
pdf = SimpleInvoice(invoice)
pdf.gen("invoice.pdf")