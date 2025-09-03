# Punto 4

## Función utilizada: Factorial
Se implementó la función recursiva clásica de factorial:

```
n*factorial(n-1)
```

---

##  Código en C (lenguaje compilado)
```c
#include <stdio.h>
#include <time.h>

int factorial(int n) {
    if (n == 0 ){
     	return 1;
    }
    else{
    	return n*factorial(n-1);
    }
    
}

int main() {
    int n = 40; 
    clock_t start = clock();

    int result = factorial(n);

    clock_t end = clock();
    double time_taken = (double)(end - start) / CLOCKS_PER_SEC;

    printf("Factorial(%d) = %lld\n", n, result);
    printf("Tiempo en C: %f segundos\n", time_taken);

    return 0;
}

```

Compilación y ejecución:
```bash
gcc compilado.c -o comp
./comp
```

---

## Código en Python (lenguaje interpretado)
```python
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

```

Ejecución:
```bash
python3 interpretado.py
```

---

## Resultados esperados
Para `n = 40`:
- **C (compilado):** en 0.000004 segundos.  
- **Python (interpretado):** en 0.000005 segundos.  

Los tiempos exactos dependen de la máquina usada.

---

## Conclusión
- El lenguaje C, al ser compilado, genera código máquina optimizado y por lo tanto es mucho más rápido.  
- El lenguaje Python, al ser interpretado, evalúa línea por línea en tiempo de ejecución, lo que lo hace más lento.  
- Este experimento demuestra la diferencia de rendimiento entre un lenguaje compilado y uno interpretado al resolver el mismo problema con una función recursiva intensiva.
