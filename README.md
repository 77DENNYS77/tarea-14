# Cálculo del precio total de una compra

Programa en Python que resuelve un problema de la vida real: calcular cuánto se debe pagar por una compra, incluyendo el IVA. Fue desarrollado para aplicar **funciones con parámetros y retorno de valores**.

## Autor

- **Nombre:** Malla Alban Dennys Bladimir
- **Universidad:** Universidad Estatal Amazónica
- **Carrera:** Tecnologías de la Información
- **Materia:** Programación Básica

## Problema que resuelve

Al comprar varias unidades de un producto, se necesita conocer el total a pagar sumando el IVA al subtotal.

## Estructura de la función

```python
def calcular_precio_total(precio_unitario, cantidad, porcentaje_iva):
    subtotal = precio_unitario * cantidad
    iva = subtotal * (porcentaje_iva / 100)
    total = subtotal + iva
    return total
```

| Elemento | Descripción |
|---|---|
| **Función** | `calcular_precio_total` |
| **Parámetros** | `precio_unitario`, `cantidad`, `porcentaje_iva` |
| **Retorno** | `total` (subtotal + IVA) |
| **Llamada** | `calcular_precio_total(precio, unidades, iva)` |

## Cómo ejecutarlo

1. Instalar [Python 3](https://www.python.org/downloads/).
2. Descargar o clonar este repositorio.
3. Ejecutar en la terminal:

```bash
python precio_total_compra.py
```

## Ejemplo de ejecución

```
=== CALCULADORA DE COMPRA ===
Nombre del producto: Cuaderno
Precio unitario ($): 2.50
Cantidad de unidades: 4
Porcentaje de IVA (%): 15

Producto: Cuaderno
Total a pagar (con IVA): $11.50
```

## Archivos

- `precio_total_compra.py`: código fuente del programa.
- `README.md`: descripción del proyecto.
