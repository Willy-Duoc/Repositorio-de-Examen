pareja_divisible = 0
pareja_indivisible = 0

while True:
    print("\n*** Menú Principal ****")
    print("A. Ingresar 2 números")
    print("B. Mostrar estadísticas")
    print("C. Terminar programa")

    opcion = input("Selecciona una opción: ").upper()

    if opcion == "A":
        valores_correctos = False
        while not valores_correctos:
            try:
                num1 = int(input("Ingrese el primer número: "))
                num2 = int(input("Ingrese el segundo número: "))
                if num1 % num2 == 0 or num2 % num1 == 0:
                    pareja_divisible += 1
                else:
                    pareja_indivisible += 1
                valores_correctos = True
            except ValueError:
                print("Valor no válido, solo se pueden ingresar números enteros.\nIntente nuevamente.")
            except ZeroDivisionError:
                print("No se puede dividir por cero. Intente con otros números.")
    elif opcion == "B":
        print(f"Cantidad de parejas de números donde un número es divisible por el otro: {pareja_divisible}")
        print(f"Cantidad de parejas de números donde los números no son divisibles entre ellos: {pareja_indivisible}")
    elif opcion == "C":
        print("Saliendo del programa.")
        print("Agradezco que usara mi programa y espero que vuelva pronto. Adiós.")
        print("Programa desarrollado por: Williams Contreras")
        break
    else:
        print("Debe ingresar una opción válida (A, B o C).")