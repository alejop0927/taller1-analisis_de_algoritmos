
def suma_numeros_impares(numero_inicial, numero_final):
    suma = 0  # O(1)
    for numero in range(numero_inicial, numero_final + 1):  # O(n)
        if numero % 2 != 0:  # O(1)
            suma += numero  # O(1)
    return suma  # O(1)



def suma_numeros_pares(numero_inicial, numero_final):
    suma = 0  # O(1)
    for numero in range(numero_inicial, numero_final + 1):  # O(n)
        if numero % 2 == 0:  # O(1)
            suma += numero  # O(1)
    return suma  # O(1)



def main():
    numero_inicial = int(input("Introduce el numero inicial: "))  # O(1)
    numero_final = int(input("Introduce el numero final: "))  # O(1)


    suma_impares = suma_numeros_impares(numero_inicial, numero_final)  # O(n)
    suma_pares = suma_numeros_pares(numero_inicial, numero_final)  # O(n)


    print("La suma de los numeros impares es: {}".format(suma_impares))  # O(1)
    print("La suma de los numeros pares es: {}".format(suma_pares))  # O(1)

#ecuacion: 4 O(n) + 10 O(1)
#complejidad: O(n)


if __name__ == "__main__":
    main()
