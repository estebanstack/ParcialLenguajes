import time

def factorial(n):
    if n == 0:
        return 1
    else: 
        return n*factorial(n-1)

n = 40  # valor de prueba
start = time.time()

result = factorial(n)

end = time.time()
print(f"Factorial({n}) = {result}")
print(f"Tiempo en Python: {end - start:.6f} segundos")
