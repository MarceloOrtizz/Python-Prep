import sys
import datetime

x = datetime.datetime.now()
a = open("clase06_ej2.csv", "a")
a.write(x, sys.argv[2], sys.argv[1], sys.argv[3])
a.close()
