# Punto 2

## Ejemplos de cadenas
### Válidos
```
a
abc
C2D
hola1
Test123
```

###  Inválidos
```
1abc   (empieza con número)
_var   (empieza con guion bajo)
123    (empieza con número)
```

---

## Diseño del AFD
- **Estados:**
  - `q0`: estado inicial (no se ha leído nada).  
  - `q1`: se leyó una letra válida (estado de aceptación).  
  - `q_err`: estado de error.  

- **Estados de aceptación:** `q1`.  

- **Transiciones:**
  - `q0` → letra → `q1`.  
  - `q0` → dígito → `q_err`.  
  - `q1` → letra o dígito → `q1`.  
  - Otro caso → `q_err`.  

---

## Implementación en Python
```python
class AFD_ID:
    def __init__(self):
        self.q0, self.q1, self.qerr = "q0", "q1", "q_err"
        self.inicial = self.q0
        self.aceptacion = {self.q1}

    def esLetra(self, c):
        return c.isalpha()

    def esDigito(self, c):
        return c.isdigit()

    def transicion(self, q, x):
        if q == self.q0:
            if self.esLetra(x):
                return self.q1
            else:
                return self.qerr
        elif q == self.q1:
            if self.esLetra(x) or self.esDigito(x):
                return self.q1
            else:
                return self.qerr
        return self.qerr

    def acepta(self, cadena):
        q = self.inicial
        for x in cadena:
            q = self.transicion(q, x)
        return q in self.aceptacion


afd = AFD_ID()
pruebas = ["a", "Esteban123", "C9Z", "12Esteban", "*hola"]

for cadena in pruebas:
    if(afd.acepta(cadena)):
        print(f"{cadena}    ->    ACEPTA")
    else:
        print(f"{cadena}    ->     NO ACEPTA")

```

---

## Ejemplo de ejecución
```
a       -> ACEPTA
Esteban123  -> ACEPTA
C9Z     -> ACEPTA
12Esteban    -> NO ACEPTA
*hola    -> NO ACEPTA
```

---

## Conclusión
- El AFD diseñado reconoce correctamente identificadores válidos según la expresión regular `[A-Za-z][A-Za-z0-9]*`.  
- El autómata rechaza identificadores que comienzan con números u otros símbolos no permitidos.  
- La implementación en Python permite validar de manera sencilla cualquier cadena de entrada.
