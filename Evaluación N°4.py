# Diccionario de tarjetas
tarjetas = {}

# Función de agregar tarjeta
def agregar_tarjeta(lst_elementos: dict, codigo: str, datos: list) -> bool:
    compras, saldo = datos
    if codigo not in lst_elementos:
        lst_elementos[codigo] = {"Compras": compras, "Saldo": saldo}
        return True
    return False

# Función de usar tarjeta para compra
def usar_tarjeta(lst_elementos: dict, codigo: str, monto: int) -> bool:
    if codigo in lst_elementos and monto > 0:
        saldo_actual = lst_elementos[codigo]["Saldo"]
        if saldo_actual >= monto:
            lst_elementos[codigo]["Saldo"] -= monto
            lst_elementos[codigo]["Compras"] += 1
            return True
    return False

# Función de listar tarjetas
def listar(lst_elementos: dict) -> None:
    if len(lst_elementos) > 0:
        for codigo, datos in lst_elementos.items():
            print(f"Código de la tarjeta: {codigo}, Compras: {datos['Compras']}, Saldo: ${datos['Saldo']}")
    else:
        print("No hay tarjetas registradas.")

# Función de ver saldos críticos
def ver_saldos_criticos(lst_elementos: dict, saldo_minimo: int) -> None:
    encontrados = False
    for codigo, datos in lst_elementos.items():
        if datos["Saldo"] <= saldo_minimo:
            print(f"Tarjeta crítica - Código: {codigo}, Saldo: ${datos['Saldo']}")
            encontrados = True
    if not encontrados:
        print("No hay tarjetas con saldo crítico.")

# Menú interactivo
while True:
    print("\nMenú de gestión de tarjetas")
    print("1. Registrar una nueva tarjeta")
    print("2. Registrar la compra de una tarjeta")
    print("3. Mostrar tarjetas registradas")
    print("4. Mostrar tarjetas con saldos críticos")
    print("5. Salir del menú")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        code = input("Ingrese el código de la tarjeta: ")
        try:
            saldo_inicial = int(input("Ingrese el saldo inicial de la tarjeta: $"))
            if saldo_inicial < 0:
                raise ValueError
            if agregar_tarjeta(tarjetas, code, [0, saldo_inicial]):
                print("Tarjeta registrada exitosamente.")
            else:
                print("La tarjeta ya está registrada.")
        except ValueError:
            print("Saldo inválido. Debe ser un número entero positivo.")

    elif opcion == "2":
        code = input("Ingrese el código de la tarjeta: ")
        try:
            compra = int(input("Ingrese el monto de la compra: $"))
            if usar_tarjeta(tarjetas, code, compra):
                print("Compra registrada exitosamente.")
            else:
                print("Error al registrar la compra. Verifique el saldo o el código de la tarjeta.")
        except ValueError:
            print("Monto no válido. Debe ingresar un número entero positivo.")

    elif opcion == "3":
        listar(tarjetas)

    elif opcion == "4":
        try:
            valor = int(input("Ingrese el valor mínimo para saldo crítico: $"))
            ver_saldos_criticos(tarjetas, valor)
        except ValueError:
            print("Valor no válido. Debe ingresar un número entero positivo.")

    elif opcion == "5":
        print("Cerrando menú.")
        break

    else:
        print("Opción inválida. Debe ingresar un número del 1 al 5.")