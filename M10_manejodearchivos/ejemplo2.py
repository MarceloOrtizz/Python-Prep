import sys
import datetime

if len(sys.argv) == 4:
    x = datetime.datetime.now()
    x = int(datetime.datetime.timestamp(x))
    a = open("clase09_ej2.csv", "a")
    fecha = x
    humedad = sys.argv[2]
    temperatura = sys.argv[1]
    llovio = sys.argv[3]
    a.write(f"{fecha}, {humedad}, {temperatura}, {llovio} \n")
    a.close()
else:
    print("3 arg")
