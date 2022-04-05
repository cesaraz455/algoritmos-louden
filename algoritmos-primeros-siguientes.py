import pprint

gramatica = [
    [{ "simbolo": "E", "definicion": ["T", "E'"] }],
    [{ "simbolo": "E'", "definicion": ["+", "T", "E'"] }],
    [{ "simbolo": "E'", "definicion": ["$"] }],
    [{ "simbolo": "T", "definicion": ["F", "T'"] }],
    [{ "simbolo": "T'", "definicion": ["*", "F", "T'"] }],
    [{ "simbolo": "T'", "definicion": ["$"] }],
    [{ "simbolo": "F", "definicion": ["(", "E", ")"] }],
    [{ "simbolo": "F", "definicion": ["id"] }],
]

simbolo_inicial = "E"
not_terminal = ["E","E'","T","T'","F"]
terminal = ["id","+","*","(",")","$"]
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