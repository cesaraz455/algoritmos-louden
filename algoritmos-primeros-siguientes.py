import pprint

# $ es cadena vacia
gramatica = [
    [{ "simbolo": "O", "definicion": ["INT", "SN", "SV"] }],
    [{ "simbolo": "INT", "definicion": ["interrogación"] }],
    [{ "simbolo": "SN", "definicion": ["DET", "N", "PL"] }],
    [{ "simbolo": "SN", "definicion": ["$"] }],
    [{ "simbolo": "PL", "definicion": ["plural"] }],
    [{ "simbolo": "PL", "definicion": ["$"] }],
    [{ "simbolo": "DET", "definicion": ["que"] }],
    [{ "simbolo": "DET", "definicion": ["una"] }],
    [{ "simbolo": "DET", "definicion": ["el"] }],
    [{ "simbolo": "DET", "definicion": ["su"] }],
    [{ "simbolo": "DET", "definicion": ["un"] }],
    [{ "simbolo": "DET", "definicion": ["la"] }],
    [{ "simbolo": "DET", "definicion": ["$"] }],
    [{ "simbolo": "SV", "definicion": ["AUX", "VERBAL", "CIRCUNSTANCIAL"] }],
    [{ "simbolo": "VERBAL", "definicion": ["X", "OI"] }],
    [{ "simbolo": "X", "definicion": ["V", "SN"] }],
    [{ "simbolo": "X", "definicion": ["COP", "PREDNOM"] }],
    [{ "simbolo": "COP", "definicion": ["estar"] }],
    [{ "simbolo": "PREDNOM", "definicion": ["ADJ"] }],
    [{ "simbolo": "ADJ", "definicion": ["encendido"] }],
    [{ "simbolo": "CIRCUNSTANCIAL", "definicion": ["PREP", "SN", "CIRCUNSTANCIAL"] }],
    [{ "simbolo": "CIRCUNSTANCIAL", "definicion": ["$"] }],
    [{ "simbolo": "OI", "definicion": ["a", "SN"] }],
    [{ "simbolo": "OI", "definicion": ["$"] }],
    [{ "simbolo": "N", "definicion": ["yo"] }],
    [{ "simbolo": "N", "definicion": ["usted"] }],
    [{ "simbolo": "N", "definicion": ["tema"] }],
    [{ "simbolo": "N", "definicion": ["conexión"] }],
    [{ "simbolo": "N", "definicion": ["internet"] }],
    [{ "simbolo": "N", "definicion": ["bombillo"] }],
    [{ "simbolo": "N", "definicion": ["router"] }],
    [{ "simbolo": "N", "definicion": ["servicio"] }],
    [{ "simbolo": "N", "definicion": ["mantenimiento"] }],
    [{ "simbolo": "N", "definicion": ["encuesta"] }],
    [{ "simbolo": "N", "definicion": ["satisfacción"] }],
    [{ "simbolo": "AUX", "definicion": ["T"] }],
    [{ "simbolo": "T", "definicion": ["no_pasado"] }],
    [{ "simbolo": "V", "definicion": ["colaborar"] }],
    [{ "simbolo": "V", "definicion": ["tener"] }],
    [{ "simbolo": "V", "definicion": ["desear"] }],
    [{ "simbolo": "V", "definicion": ["responder"] }],
    [{ "simbolo": "PREP", "definicion": ["en"] }],
    [{ "simbolo": "PREP", "definicion": ["de"] }],
]

simbolo_inicial = "O"
not_terminal = [
    "O", 
    "INT",
    "SN",
    "PL",
    "DET",
    "SV", 
    "VERBAL", 
    "X", 
    "COP", 
    "PREDNOM", 
    "ADJ", 
    "CIRCUNSTANCIAL", 
    "OI", 
    "N", 
    "AUX", 
    "T", 
    "V", 
    "PREP"
]
terminal = [
    "$",
    "interrogación",
    "plural",
    "que",
    "una",
    "el",
    "su",
    "un",
    "la",
    "estar",
    "encendido",
    "a",
    "yo",
    "usted",
    "tema",
    "conexión",
    "internet",
    "bombillo",
    "router",
    "servicio",
    "mantenimiento",
    "encuesta",
    "satisfaccion",
    "no_pasado",
    "colaborar",
    "tener",
    "desear",
    "responder",
    "en",
    "de"
]
primeros = {}
siguientes = {}

def is_terminal(X):
    for i in terminal:
        if(i == X):
            return True
    return False

def have_empty_string(array_primeros):
    for i in array_primeros:
        if(i == "$"):
            return True
    return False

def definition_has_A(definicion, A):
    for i in definicion:
        if(i == A):
            return True
    return False

def primero(A):
    if is_terminal(A):
        return [A]
    else:
        conjunto_temp = []
        for produccion in gramatica:
            if(produccion[0]['simbolo'] == A):
                produccion_A = produccion[0]
                n = len(produccion_A["definicion"])
                k = 1
                continuar = True
                while(continuar == True and k <= n):
                    X_sub_k = produccion_A["definicion"][k-1]
                    primero_x_sub_k = primero(X_sub_k)
                    conjunto_temp = conjunto_temp + primero_x_sub_k
                    if not have_empty_string(primero_x_sub_k):
                        continuar = False
                    k = k + 1
        return conjunto_temp

def siguiente(A):
    conjunto_temp = []

    if A == simbolo_inicial:
        conjunto_temp.append("$")

    for produccion in gramatica:
        produccion_A = produccion[0]
        if definition_has_A(produccion_A["definicion"], A):
            i = 1
            n = len(produccion_A["definicion"])
            while(i <= n):
                if produccion_A["definicion"][i-1] == A:
                    if i == n:
                        if(produccion_A["definicion"][i-1] != produccion_A["simbolo"]):
                            conjunto_temp = conjunto_temp + siguiente(produccion_A["simbolo"])
                    else:
                        conjunto_primeros = primero(produccion_A["definicion"][i])
                        conjunto_temp = conjunto_temp + conjunto_primeros
                        if have_empty_string(conjunto_primeros):
                            conjunto_temp = conjunto_temp + siguiente(produccion_A["simbolo"])
                i = i + 1

    return conjunto_temp

def run():
    for A in not_terminal:
        primeros[A] = set(primero(A))

    for A in not_terminal:
        siguientes[A] = set(siguiente(A))

    printer = pprint.PrettyPrinter(indent=1, width=40)
    print("El conjunto primeros es:")
    printer.pprint(primeros)
    print("El conjunto siguientes es:")
    printer.pprint(siguientes)

if __name__ == '__main__':
    run()