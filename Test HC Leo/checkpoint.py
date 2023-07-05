# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def numeroBinario(numero):
   '''
    Esta función recibe como argumento un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 debe retornar nulo.
    Recibe un argumento:
        numero: Será el número que se convertirá a binario.
    Ej:
        NumeroBinario(12) debe retornar 1100
        NumeroBinario(2) debe retornar 10
        NumeroBinario(14) debe retornar 1110
   
    #Tu código aca:
    '''
   if type(numero)==int:
      if numero>-1:
         b=""
         while True:
            dig=numero%2
            numero=int(numero/2)
            b=str(dig)+b
            if numero==0:
               break
      else:
        return None
   else:
      return None

   return int(b)

def dividirMultiplicar(lista):
   '''
   La función recibe como argumento una lista de números enteros, y debe retornar una lista
   con los siguientes parámetros:
   1.Los números que sean positivos y pares se deben dividir por 2, y el resultado expresado como entero (sin decimales, no redondeando, debe tomar sólo la parte entera de la división por 2).
   2.Los números negativos multiplicados por 2.
   3.Los que no cumplan los criterios anteriores deben quedar igual al valor original.
   4.Ordernar los números de mayor a menor.
   Ej: dividirMultiplicar([2,4,1,-3]): debe retornar: [2, 1, 1, -6]
   '''   
   #Tu código acá
   lf=[]
   for i in lista:
    if i>=0:
        if i%2==0:
            lf.append(i/2)
        else:
            lf.append(i)    
    if i<0:
        lf.append(i*2)
   lf.sort(reverse=True)
   return lf

def crearDiccionario(lista):
   '''
   La función recibe como argumento una lista de números enteros, y debe retornar un diccionario 
   con tres claves, "multiplos3", 'cuadrados", "menores_promedio".
   Para la clave "multiplos3", el valor debe ser una lista con los múltiplos de 3 de la lista original.
   Para la clave "cuadrados", el valor debe ser una lista con los valores de la lista original 
   elevados al cuadrado.
   Para la clave "menores_promedio", el valor debe ser una lista con los valores 
   menores al promedio de la lista original.
   EJ: crearDiccionario([3,6,7,12]): debe retornar: {'multiplos3': [3, 6, 12], 
   'cuadrados': [9, 36, 49, 144], 'menores_promedio': [3, 6]}
   '''
   #Tu código acá
   m3=[]
   e2=[]
   mp=[]
   dicc={}
   for i, v in enumerate(lista):
      if (v%3)==0:
         m3.append(v)
      e2.append(v**2)
      if (v<(sum(lista)/len(lista))):
         mp.append(v)
   dicc["multiplos3"]=m3
   dicc["cuadrados"]=e2
   dicc["menores_promedio"]=mp

   return dicc

def trianguloRectangulo(a,b,c):
   '''
   La función debe recibir como argumentos el valor en cm de los lados de un triángulo (a y b son los catetos), y dado estos valores, retornar True si en efecto corresponden a un triángulo rectángulo, o False en caso contrario. Sólo se debe poder pasar valores enteros como argumentos de la función, caso contrario debe retornar nulo.
   EJ: trianguloRectangulo(3.5,3.5,2.4), debe retornar nulo
   EJ: trianguloRectangulo(3,3,3), debe retornar False
   EJ: trianguloRectangulo(3,4,5), debe retornar True
   
   #Tu código acá
   '''
   if type(a)==int and type(b)==int and type(c)==int:
      if a and b and c > 0:
         if (a**2 + b**2) == (c**2):
            return True
         else:
           return False
      else:
         return False
   else:
      return None

   
 
  

def ciudadesPoblacion(diccionario):
   '''
   Dado el siguiente diccionario ciudades, la función debe retornar una lista de listas, donde cada 
   elemento de la lista sea una lista con el par ['ciudad', población],
   pero sólo de las ciudades que comiencen con la letra 'B', y como último elemento 
   de la lista el par ['promedio', promedio de población] con el promedio de población
   de las ciudades seleccionadas.
   Ej: Si se pidiera ciudades que comiencen con la letra 'S', debe devolver: [['São Paulo', 21048514], ['Santiago de Chile', 7112808],['promedio', 14080661.0]]

   ciudades = {
      'São Paulo': 21048514,
      'Buenos Aires': 14975587,
      'Río de Janeiro': 11902701,
      'Bogotá': 10777931,
      'Lima': 10479899,
      'Santiago de Chile': 7112808,
      'Belo Horizonte': 6006091,
      'Caracas': 5622798,
      'Brasília': 4291577
      }
      Pista: investigar método de string startswith()
   '''
   li=[]
   suma=0
   for c, p in diccionario.items():
        if c.startswith("B"):
            li.append([c,p])
            suma+=p
   li.append(['promedio', suma/len(li)])
   return li


def ordenarPalabras(palabras):
   '''
   La función recibe como argumento una secuencia de palabras unidas por guiones, 
   y debe retornar las mismas palabras, unidas por guiones, pero en orden alfabético. 
   Si el argumento que se le pasa no es un string o no contiene guiones, debe retornar nulo.
   EJ: ordenarPalabras('saco-libro-casa') debe retornar 'casa-libro-saco'
   EJ: ordenarPalabras('Hola') debe retornar nulo
   Pista: investigar métodos de string
   '''
   if type(palabras)==str:
        if palabras.count("-")>0:
            li=palabras.split("-")
            li.sort()
            return "-".join(li)
        else:
            return None
   else:
        return None


def stringEspejo(texto):
   '''
    La función recibe como argumento una cadena de texto y retorna la cadena invertida, 
    pero sólo si tiene más de tres caracteres, sino debe retornar nulo.
    EJ: stringEspejo('Hola Mundo') debe retornar 'odnuM aloH'
    EJ: stringEspejo('Hoy') debe retornar nulo
   '''   
   
   if len(texto) > 3:
      otxet=""
      for i, c in enumerate(texto):
         otxet=c+otxet
   else:
      return None
   return otxet


