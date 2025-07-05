# Trabajo práctico - Gestor de gastos personales

# Lista para guardar los gastos
gastos = []

# Umbrales para clasificar gastos
UMBRAL_MENOR = 1000
UMBRAL_MAYOR = 5000

# Función para registrar un nuevo gasto
def registrar_gasto():
    print("\n--- Registrar nuevo gasto ---")
    categoria = input("Ingresá la categoría (ej: comida, transporte, etc.): ")
    try:
        monto = float(input("Ingresá el monto del gasto: $"))
        gastos.append({"categoria": categoria.lower(), "monto": monto})
        print(f" Gasto registrado: ${monto:.2f} en '{categoria}'")
    except ValueError:
        print(" Monto inválido. Debe ser un número.")

# Función para mostrar todos los gastos
def mostrar_gastos():
    print("\n--- Lista de gastos ---")
    if not gastos:
        print("Aún no cargaste ningún gasto.")
        return
    for i, gasto in enumerate(gastos, start=1):
        print(f"{i}. ${gasto['monto']:.2f} - {gasto['categoria'].capitalize()}")

# Función para mostrar el total gastado y por categoría
def mostrar_resumen():
    print("\n--- Resumen de gastos ---")
    if not gastos:
        print("No hay gastos cargados.")
        return

    total = 0
    categorias = {}
    menores = []
    mayores = []

    for gasto in gastos:
        total += gasto["monto"]
        cat = gasto["categoria"]
        categorias[cat] = categorias.get(cat, 0) + gasto["monto"]

        # Clasificación adicional
        if gasto["monto"] < UMBRAL_MENOR:
            menores.append(gasto)
        elif gasto["monto"] > UMBRAL_MAYOR:
            mayores.append(gasto)

    print(f" Total gastado: ${total:.2f}")
    print(" Gastos por categoría:")
    for cat, monto in categorias.items():
        print(f" - {cat.capitalize()}: ${monto:.2f}")

    print("\n Compras menores a $1000:")
    if menores:
        for gasto in menores:
            print(f"  - ${gasto['monto']:.2f} en {gasto['categoria']}")
    else:
        print("  No se registraron compras menores a $1000.")

    print("\n Compras mayores a $5000:")
    if mayores:
        for gasto in mayores:
            print(f"  - ${gasto['monto']:.2f} en {gasto['categoria']}")
    else:
        print("  No se registraron compras mayores a $5000.")

# Función para buscar gastos por categoría
def buscar_por_categoria():
    print("\n--- Buscar gastos por categoría ---")
    categoria = input("Ingresá la categoría a buscar: ").lower()
    encontrados = [g for g in gastos if g["categoria"] == categoria]

    if encontrados:
        print(f" Gastos encontrados en '{categoria}':")
        for g in encontrados:
            print(f"  - ${g['monto']:.2f}")
    else:
        print(" No se encontraron gastos en esa categoría.")

# Función para eliminar un gasto
def eliminar_gasto():
    mostrar_gastos()
    if not gastos:
        return
    try:
        idx = int(input("Ingresá el número del gasto a eliminar: "))
        if 1 <= idx <= len(gastos):
            eliminado = gastos.pop(idx - 1)
            print(f" Gasto eliminado: ${eliminado['monto']:.2f} en {eliminado['categoria']}")
        else:
            print(" Número fuera de rango.")
    except ValueError:
        print(" Entrada inválida. Debe ser un número.")

# Función para ver todas las categorías registradas
def ver_categorias():
    print("\n--- Categorías registradas ---")
    if not gastos:
        print("No hay gastos cargados.")
        return

    categorias = set(g["categoria"] for g in gastos)
    print("Categorías ingresadas:")
    for cat in sorted(categorias):
        print(f" - {cat.capitalize()}")

# Menú principal
def menu():
    while True:
        print("\n========== GESTOR DE GASTOS ==========")
        print("1. Registrar nuevo gasto")
        print("2. Ver lista de gastos")
        print("3. Ver resumen de gastos")
        print("4. Buscar por categoría")
        print("5. Eliminar gasto")
        print("6. Ver categorías registradas")
        print("7. Salir")
        opcion = input("Elegí una opción (1-7): ")

        if opcion == "1":
            registrar_gasto()
        elif opcion == "2":
            mostrar_gastos()
        elif opcion == "3":
            mostrar_resumen()
        elif opcion == "4":
            buscar_por_categoria()
        elif opcion == "5":
            eliminar_gasto()
        elif opcion == "6":
            ver_categorias()
        elif opcion == "7":
            print("\nGracias por usar el gestor. \U0001F91D Hasta la próxima!")
            break
        else:
            print(" Opción inválida. Intentá de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
