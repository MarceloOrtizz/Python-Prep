import sys

# Comprobación de seguridad, ejecutar sólo si se recibe 3 argumentos
if len(sys.argv) == 4:
    import datetime
    import os

    x = datetime.datetime.now()
    x = int(datetime.datetime.timestamp(x))

    temperatura = sys.argv[1]
    humedad = sys.argv[2]
    lluvia = sys.argv[3]
    # temperatura = input('Ingrese la temperatura en grados centígrados')
    # humedad = input('Ingrese el porcentaje de humedad')
    linea = str(x) + "," + temperatura + "," + humedad + "," + lluvia

    logs_lluvia = open("clase09_ej2.csv", "a")
    logs_lluvia.write(linea + "\n")
    logs_lluvia.close()

else:
    print("ERROR: Introdujo una cantidad de argumentos distinta de tres (3)")
    print("Ejemplo: clase09_ej1.py <temperatura> <humedad> <True o False>")
