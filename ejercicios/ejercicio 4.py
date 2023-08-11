import math



def raiz_cuadrada(numero):
    aproximacion = 1  # O(1)
    while True:  # O(log n)
        division = numero / aproximacion  # O(1)
        promedio = (aproximacion + division) / 2  # O(1)
        if abs(aproximacion - promedio) < 0.000001:  # O(1)
            break
        aproximacion = promedio  # O(1)
    return aproximacion  # O(1)

#ecuacion:1 O(log n) +6 O(1)
numero = int(input("Introduce el numero al que se le quiere hallar la raiz cuadrada: "))  # O(1)
aproximacion = int(input("Introduce la primera aproximacion a la raiz cuadrada: "))  # O(1)
raiz = raiz_cuadrada(numero)  # O(log n)
print("La raiz cuadrada del numero {} es aproximadamente {}".format(numero, raiz))  # O(1)

#ecuacion:1 O(log n) +3 O(1)
#complejidad:O(log n)