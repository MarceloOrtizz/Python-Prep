class Herramientas:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros

    def test_primo(self):
        for x in self.lista:
            if self.__test_primo(x):
                print(f"{x} es primo")
            else:
                print(f"{x} NO es primo")

    def __test_primo(self, n):
        primo = True
        if type(n) != int or n < 2:
            return False
        for x in range(2, int(n ** (1 / 2)) + 1):
            if n % x == 0:
                primo = False
                break
        return primo

    def mayor_frequencia(self, mayor=True):
        if type(self.lista) != list or len(self.lista) == 0:
            return None
        mayorf = 1
        if mayor:
            mayorf = 0
        else:
            mayorf = len(self.lista)
        for i, v in enumerate(self.lista):
            c = 0
            for x in self.lista:
                if v == x:
                    c = c + 1
            if mayor:
                if c > mayorf:
                    mayorf = c
                    imf = i
            else:
                if c < mayorf:
                    mayorf = c
                    imf = i
        return self.lista[imf], mayorf

    def convierte(self, origen, destino):
        for x in self.lista:
            print(
                f"{x} grados {origen} corresponden a {self.__convierte(x,origen, destino)} grados {destino}"
            )

    def __convierte(self, valor, origen, destino):
        if origen != "C" and origen != "F" and origen != "K":
            return None
        if destino != "C" and destino != "F" and destino != "K":
            return None
        if origen == "C" and destino == "F":
            r = valor * 9 / 5 + 32
        if origen == "C" and destino == "K":
            r = valor + 273.15
        if origen == "F" and destino == "C":
            r = (valor - 32) * 5 / 9
        if origen == "F" and destino == "K":
            r = (valor - 32) * 5 / 9 + 273.15
        if origen == "K" and destino == "C":
            r = valor - 273.15
        if origen == "K" and destino == "F":
            r = (valor - 273.15) * 9 / 5 + 32
        if origen == destino:
            r = valor
        return r

    def factorial(self):
        for x in self.lista:
            print(f"{self.__factorial(x)} es factorial de {x}")

    def __factorial(self, num):
        if type(num) != int or num < 0:
            return None
        f = num
        if f == 0:
            f = 1
        while num > 1:
            num = num - 1
            f = f * num
        return f
