from fpdf import FPDF

def generar_boleta(nombre_cliente, productos, total, archivo_salida, logo_path):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Logo de la empresa
    pdf.image(logo_path, 10, 8, 33)  # Ajusta la posición y tamaño del logo
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, 'BOLETA DE VENTA', ln=True, align='C')

    # Información de la empresa
    pdf.set_font('Arial', '', 12)
    pdf.ln(10)
    pdf.cell(200, 10, 'Nombre de la Empresa', ln=True)
    pdf.cell(200, 10, 'Dirección: Calle Ficticia 123', ln=True)
    pdf.cell(200, 10, 'RUC: 123456789', ln=True)
    pdf.cell(200, 10, 'Teléfono: +51 987 654 321', ln=True)

    # Datos del cliente
    pdf.ln(10)
    pdf.cell(200, 10, f'Cliente: {nombre_cliente}', ln=True)
    pdf.cell(200, 10, 'Fecha: 2025-04-15', ln=True)
    pdf.cell(200, 10, 'Boleta No: 00123', ln=True)

    # Línea divisoria
    pdf.set_line_width(0.5)
    pdf.line(10, 70, 200, 70)

    # Títulos de los productos
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(50, 10, 'Producto', border=1, align='C')
    pdf.cell(50, 10, 'Cantidad', border=1, align='C')
    pdf.cell(50, 10, 'Precio', border=1, align='C')
    pdf.cell(50, 10, 'Subtotal', border=1, align='C')
    pdf.ln()

    # Productos
    pdf.set_font('Arial', '', 10)
    for producto in productos:
        nombre, cantidad, precio = producto
        subtotal = cantidad * precio
        pdf.cell(50, 10, nombre, border=1, align='C')
        pdf.cell(50, 10, str(cantidad), border=1, align='C')
        pdf.cell(50, 10, f'S/ {precio:.2f}', border=1, align='C')
        pdf.cell(50, 10, f'S/ {subtotal:.2f}', border=1, align='C')
        pdf.ln()

    # Total
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(150, 10, 'TOTAL:', 0, 0, 'R')
    pdf.cell(50, 10, f'S/ {total:.2f}', 0, 1, 'C')

    # Agradecimiento
    pdf.ln(10)
    pdf.set_font('Arial', 'I', 10)
    pdf.cell(200, 10, '¡Gracias por tu compra!', 0, 1, 'C')

    # Guardar archivo
    pdf.output(archivo_salida)

# Datos de ejemplo
nombre_cliente = "Juan Pérez"
productos = [("Producto 1", 1, 50), ("Producto 2", 1, 30), ("Producto 3", 2, 20)]
total = 140.00
archivo_salida = "boleta_profesional.pdf"
logo_path = "imgs/logo.png"  # Ruta al logo

# Generar la boleta
generar_boleta(nombre_cliente, productos, total, archivo_salida, logo_path)

print("Boleta generada exitosamente.")
