def calcular_precio_total(precio_unitario, cantidad, porcentaje_iva):
    """Calcula el precio total de una compra incluyendo el IVA."""
    subtotal = precio_unitario * cantidad
    iva = subtotal * (porcentaje_iva / 100)
    total = subtotal + iva
    return total


# Programa principal
print("=== CALCULADORA DE COMPRA ===")
producto = input("Nombre del producto: ")
precio = float(input("Precio unitario ($): "))
unidades = int(input("Cantidad de unidades: "))
iva = float(input("Porcentaje de IVA (%): "))

total_a_pagar = calcular_precio_total(precio, unidades, iva)

print(f"\nProducto: {producto}")
print(f"Total a pagar (con IVA): ${total_a_pagar:.2f}")
