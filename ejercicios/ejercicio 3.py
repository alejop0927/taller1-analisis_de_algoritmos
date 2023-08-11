matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
resultado = []
for i in range(3):
    for j in range(3):
        resultado.append(matriz[i][j])
for i in range(3):
    resultado.append(matriz[i][2])
for i in range(2, -1, -1):
    resultado.append(matriz[i][0])
for i in range(2, -1, -1):
    resultado.append(matriz[i][1])
print(resultado)