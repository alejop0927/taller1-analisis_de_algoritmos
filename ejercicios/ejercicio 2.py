def mostrar_zigzag(matriz, inicio_fila, inicio_columna): #O(n)
    n = len(matriz)  # O(1)
    m = len(matriz[0]) if n > 0 else 0  # O(1)

    if inicio_fila >= n or inicio_columna >= m:  # O(1)
        return "Posición de inicio fuera de los límites de la matriz"  # O(1)

    indices_zigzag = []  # O(1)

    while inicio_fila >= 0 and inicio_columna >= 0:  # O(n)
        indices_zigzag.append((inicio_fila, inicio_columna))  # O(1)

        if (inicio_fila + inicio_columna) % 2 == 0:  # O(1)
            if inicio_columna > 0:  # O(1)
                inicio_columna -= 1  # O(1)
            else:
                inicio_fila -= 1  # O(1)
        else:
            if inicio_fila < n - 1:  # O(1)
                inicio_fila += 1  # O(1)
            else:
                inicio_columna -= 1  # O(1)

    return indices_zigzag  # O(1)

#ecuacion:  14 O(1) + 2 O(n)

n = int(input("Ingrese el tamaño de la matriz cuadrada: "))  # O(1)
fila_inicio = int(input("Ingrese la fila de inicio: "))  # O(1)
columna_inicio = int(input("Ingrese la columna de inicio: "))  # O(1)

matriz = [[0] * n for _ in range(n)]  # O(n^2)

resultado = mostrar_zigzag(matriz, fila_inicio, columna_inicio)  # O(n)
if isinstance(resultado, str):  # O(1)
    print(resultado)  # O(1)
else:
    print("Índices en forma de zig-zag:")  # O(1)
    for fila, columna in resultado:  # O(n)
        print(f"[{fila}][{columna}]")  # O(1)

#ecuacion: 1 O(n^2) + 2 O(n) + 7 O(n)
#Complejidad: O(n^2)


