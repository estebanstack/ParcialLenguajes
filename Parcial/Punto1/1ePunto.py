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
