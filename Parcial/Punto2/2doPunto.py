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
