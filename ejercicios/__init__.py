def calcular_angulo_recursivo(hora, minutos):
    if hora == 12:
        hora = 0
    if minutos == 60:
        minutos = 0
        hora += 1
    if hora == minutos == 0:
        return 0

    angulo_horario = (hora % 12) * 30 + minutos * 0.5
    angulo_minutero = minutos * 6

    angulo = abs(angulo_horario - angulo_minutero)
    angulo = min(360 - angulo, angulo)

    return angulo


hora = int(input("Ingresa la hora (0-12): "))
minutos = int(input("Ingresa los minutos (0-59): "))

angulo = calcular_angulo_recursivo(hora, minutos)
print(f"El ángulo entre las manecillas es: {angulo} grados")
