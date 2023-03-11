import math
import time

escolha = int(input("digite o número escolhido: "))

t0 = time.time()

primos = []

primos.append(2)
for c in range(3, escolha+1,2):
        primos.append(c)
        
for n in range(3, round(math.sqrt(escolha))+1,2):
    for x in primos:
        if n != x:
            if x % n == 0:
                primos.remove(x)
print(primos)
t1 = time.time()
tempoFinal = t1 - t0
print(f"O tempo final foi {tempoFinal:.5f} segundos")