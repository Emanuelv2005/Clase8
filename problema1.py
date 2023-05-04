def sumar_5_enteros():
    # definicion de variables
    lista = []
    contadorwhile = 0
    tamaño = 5
    suma = 0

    # ingresamos los numeros
    while contadorwhile < tamaño:
        lista.append(float(input("Ingrese numero "+str(contadorwhile+1) +": ")))
        contadorwhile +=1

    # sumamos los numeros
    contadorwhile = 0
    while contadorwhile < tamaño:
        suma += lista[contadorwhile]
        contadorwhile +=1

    print("Los elementos de la lista son:")
    for numero in lista:
        print(numero,end=', ')

    print("\n la suma de todos sus elementos es:")
    print(suma)

    

