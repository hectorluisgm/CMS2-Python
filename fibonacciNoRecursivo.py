import sys

def fibonacciNoRecursivo(n: int) -> int:
  listaFib = esSecuenciaFibonacci(n)
  resultado = listaFib[len(listaFib) - 1]
  return resultado

def esSecuenciaFibonacci(n:int) -> list:
  secuenciaFib:list = []
  i:int = 0
  if n <= 0:
      return [0]
  elif n == 1:
      return [0,1]
  elif n == 2:
      return [0,1,1]
  else:
      secuenciaFib: list = [0,1,1]
      for i in range(3,n+1):
        secuenciaFib.append(secuenciaFib[i-1] + secuenciaFib[i-2])
      return secuenciaFib

if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))