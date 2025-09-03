# Punto 1

## Expresión Regular
La expresión regular que define el lenguaje es:

```
a* b* c*
```

Esto significa:
- Cero o más `a`.  
- Seguido de cero o más `b`.  
- Seguido de cero o más `c`.  

Ejemplos válidos:
```
""      (cadena vacía)
aaa
bbb
ccc
abc
aabbc
```

Ejemplos inválidos:
```
ba
cab
acb
```

---

## Diseño del AFD
- **Estados:**
  - `q0`: fase de `a` (estado inicial).  
  - `q1`: fase de `b`.  
  - `q2`: fase de `c`.  
  - `q_err`: estado de error (cualquier secuencia inválida).  

- **Estados de aceptación:** `q0, q1, q2`.  
- **Transiciones:**
  - `q0`: con `a → q0`, con `b → q1`, con `c → q2`.  
  - `q1`: con `b → q1`, con `c → q2`, con `a → q_err`.  
  - `q2`: con `c → q2`, con `a` o `b → q_err`.  

---

## Implementación en Python
```python
class AFD:
    def __init__(self):
        self.estados = {"q0", "q1", "q2", "q_err"}
        self.inicial = "q0"
        self.aceptacion = {"q0", "q1", "q2"}
        self.estado = self.inicial

    def transicion(self, estado, simbolo):
        if estado == "q0":
            if simbolo == "a": return "q0"
            elif simbolo == "b": return "q1"
            elif simbolo == "c": return "q2"
            else: return "q_err"
        elif estado == "q1":
            if simbolo == "b": return "q1"
            elif simbolo == "c": return "q2"
            else: return "q_err"
        elif estado == "q2":
            if simbolo == "c": return "q2"
            else: return "q_err"
        else:
            return "q_err"

    def evaluar(self, cadena):
        self.estado = self.inicial
        for simbolo in cadena:
            self.estado = self.transicion(self.estado, simbolo)
        return self.estado in self.aceptacion



afd = AFD()
cadenas = ["", "aaa", "bbb", "ccc", "aabbc", "abc", "acb", "cab","ab", "bc"]

for cadena in cadenas:
    if(afd.evaluar(cadena)):
        print(f"{cadena}   ->   ACEPTA" )
    else:
        print(f"{cadena}   ->   NO ACEPTA")

```

---

## 📌 Ejemplo de ejecución
```
       -> ACEPTA
aaa    -> ACEPTA
bbb    -> ACEPTA
ccc    -> ACEPTA
aabbc  -> ACEPTA
abc    -> ACEPTA
acb    -> NO ACEPTA
cab    -> NO ACEPTA
ab     -> ACEPTA
bc     -> ACEPTA
```

---

## Conclusion
- La expresión regular `a* b* c*` define correctamente el lenguaje.  
- El AFD implementado en Python valida si una cadena pertenece o no al lenguaje.  
- El autómata acepta cadenas vacías, solo `a`, solo `b`, solo `c`, o combinaciones ordenadas; y rechaza cualquier secuencia fuera del orden.
