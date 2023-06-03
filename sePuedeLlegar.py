from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.
def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int :

  for vuelo in vuelos:
    if vuelo[0] == origen and vuelo[1] == destino:
      return 1

  # Ruta Indirecta 
  existeRutaInditecta: bool = True

  origenNuevo:str = origen
  rutaIndirecta: List[Tuple[str,str]] = []


  while existeRutaInditecta:
    rutaNueva = None

   #Busco si existen vuelos desde el origen indicado por parametro
    for vuelo in vuelos: 
      if vuelo[0] == origenNuevo:
        rutaNueva = vuelo
        rutaIndirecta.append(vuelo)
    
    if rutaNueva is None:
      break

    origenNuevo = rutaNueva[1]
    destinoNuevo:str =  rutaNueva[1]

    # Verificamos si consiguio el destino
    if destinoNuevo == destino:
      return len(rutaIndirecta)
    
    # Como arriba no salto la validadcion (DestinoNuevo no es el destino deseado), Buscamos en este segundo bucle si existen vuelos desde ese destinoNuevo
    for vuelo in vuelos:
      if vuelo[0] == destinoNuevo:
        origenNuevo = vuelo[0]


  return -1


if __name__ == '__main__':
  origen = input()
  destino = input()
  vuelos = input()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))