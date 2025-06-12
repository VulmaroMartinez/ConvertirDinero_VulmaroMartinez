#Desarrolla un programa con un menú interactivo que permita al usuario realizar
#conversiones entre monedas, usando valores fijos (por ejemplo):
#✓ Pesos mexicanos a dólares (tipo de cambio: 1 USD = 17.5 MXN)
#✓ Pesos mexicanos a euros (tipo de cambio: 1 EUR = 19.2 MXN)
#✓ Dólares a pesos
#✓ Euros a pesos

def convertir_pesos_a_dolares(pesos):
    return pesos / 17.5

def convertir_pesos_a_euros(pesos):
    return pesos / 19.2

def convertir_dolares_a_pesos(dolares):
    return dolares * 17.5

def convertir_euros_a_pesos(euros):
    return euros * 19.2

while True:
    print("1. Pesos mexicanos a dólares")
    print("2. Pesos mexicanos a euros")
    print("3. Dólares a pesos")
    print("4. Euros a pesos")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        pesos = float(input("Ingrese la cantidad de pesos mexicanos: "))
        dolares = convertir_pesos_a_dolares(pesos)
        print(f"{pesos} pesos mexicanos son {dolares} dólares")
    elif opcion == "2":
        pesos = float(input("Ingrese la cantidad de pesos mexicanos: "))
        euros = convertir_pesos_a_euros(pesos)
        print(f"{pesos} pesos mexicanos son {euros} euros")
    elif opcion == "3":
        dolares = float(input("Ingrese la cantidad de dólares: "))
        pesos = convertir_dolares_a_pesos(dolares)
        print(f"{dolares} dólares son {pesos} pesos mexicanos")
    elif opcion == "4":
        euros = float(input("Ingrese la cantidad de euros: "))
        pesos = convertir_euros_a_pesos(euros)
        print(f"{euros} euros son {pesos} pesos mexicanos")
    elif opcion == "5":
        print("Hasta luego")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
        
        
