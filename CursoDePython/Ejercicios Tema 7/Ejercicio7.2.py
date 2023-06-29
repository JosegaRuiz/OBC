import time

hora_actual = time.localtime().tm_hour

if hora_actual >= 19:
    print("¡Es hora de ir a casa!")
else:
    tiempo_restante = 19 - hora_actual
    print("Aún quedan", tiempo_restante, "horas para ir a casa.")
