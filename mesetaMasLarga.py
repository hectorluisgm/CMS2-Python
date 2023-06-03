from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def mesetaMasLarga(l: List[int]) -> int :
  i:int = 0

  contador:int = 1
  contadorMax: int = 1

  if len(l) == 0:
    return 0

  for i in range(1,len(l)):
    if  l[i] == l[i-1]:
      contador += 1
      if contador > contadorMax:
          contadorMax = contador
    else:
      contador = 1
  
  return contadorMax

if __name__ == '__main__':
  x = input()
  print(mesetaMasLarga([int(j) for j in x.split()]))
