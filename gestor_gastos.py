# gestor_gastos.py
# Trabajo práctico - Gestor de gastos personales
# Requiere Python 3 - Ejecutar en consola: python gestor_gastos.py

# Lista para guardar los gastos
gastos = []

# Función para registrar un nuevo gasto
def registrar_gasto():
    print("\n--- Registrar nuevo gasto ---")
    categoria = input("Ingresá la categoría (ej: comida, transporte, etc.): ")
    try:
        monto = float(input("Ingresá el monto del gasto: $"))
        gastos.append({"categoria": categoria.lower(), "monto": monto})
        print(f"✅ Gasto registrado: ${monto:.2f} en '{categoria}'")
    except ValueError:
        print("❌ Monto inválido. Debe ser un número.")

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

    for gasto in gastos:
        total += gasto["monto"]
        cat = gasto["categoria"]
        categorias[cat] = categorias.get(cat, 0) + gasto["monto"]

    print(f"💰 Total gastado: ${total:.2f}")
    print("📊 Gastos por categoría:")
    for cat, monto in categorias.items():
        print(f" - {cat.capitalize()}: ${monto:.2f}")

# Función principal con menú
def menu():
    while True:
        print("\n========== GESTOR DE GASTOS ==========")
        print("1. Registrar nuevo gasto")
        print("2. Ver lista de gastos")
        print("3. Ver resumen de gastos")
        print("4. Salir")
        opcion = input("Elegí una opción (1-4): ")

        if opcion == "1":
            registrar_gasto()
        elif opcion == "2":
            mostrar_gastos()
        elif opcion == "3":
            mostrar_resumen()
        elif opcion == "4":
            print("👋 ¡Gracias por usar el gestor!")
            break
        else:
            print("❌ Opción inválida. Intentá de nuevo.")

# Punto de entrada del programa
if __name__ == "__main__":
    menu()