import argparse
import random

def tieneInverso(numero, modulo):

    try:
        numero == int(numero)
        modulo == int(modulo)
    except:
        return("No has introducido un número")

    return math.gcd(int(numero), int(modulo)) == 1

def euclides(numero, modulo):
    
    n = int(modulo)
    a = int(numero)

    try:
        n == int(modulo)
        a == int(numero)
    except:
        return("No has introducido un número")

    g = [n, a]
    u = [1, 0]
    v = [0, 1]
    y = [None, None]

    i = 1

    while g[i] != 0:
        y.append( g[i-1] // g[i] )
        g.append( g[i-1] - (y[i+1] * g[i]))
        u.append( u[i-1] - (y[i+1] * u[i]))
        v.append( v[i-1] - (y[i+1] * v[i]))
        i += 1
    
    if v[i-1] < 0:
        x = v[i-1] + n
    else:
        x = v[i-1]

    return x

def Euler(numero1, numero2):
    
    Euler = (numero1 - 1) * (numero2 - 1)
    return Euler

def producto(numero1, numero2):

    producto = numero1 * numero2
    return producto

def crear_Primo(v = False, ceros = 8):
    if v:
        print("Generando número primo:")
    contador = 0
    excluidos = (0, 2, 4, 5, 6, 8)
    while True:
        contador += 1
        if v:
            print("{c} número(s) probado(s)".format(c = contador))
        primo=random.randint(10**(ceros-1), 10**ceros)
        print(type(primo))
        if not int(str(primo)[-1]) in excluidos:
            division = 0
            try:
                mitad = primo/2
                if not isinstance(mitad, float):
                    break
            except:
                break
            fibo_1 = 0
            fibo_2 = 1
            fibo_temp = fibo_1 + fibo_2
            while fibo_temp < int(primo/2):
                if primo % fibo_temp == 0:
                    division += 1
                fibo_1 = fibo_2
                fibo_2 = fibo_temp
                fibo_temp = fibo_1 + fibo_2
                if division == 2:
                    break
            if division == 1:
                if v:
                    print("Primo encontrado: {p}".format(p= primo))
                return primo 
                break

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbosity", help = "Indique '-v 1' si quiere información durante la ejecución del programa")
    parser.add_argument("-t", "--tamaño", help = "Indique el número de dígitos que quiere que tengan los números primos. Por defecto es 8. Recuerde que cuanto mayor sea el número más tiempo costará generarlo")
    args = parser.parse_args()

if args.verbosity is not None:
    if args.tamaño is not None:
        p = crear_Primo(v = True, ceros = (int(args.tamaño)))
    else:
        p = crear_Primo(v = True)
else:
    if args.tamaño is not None:
        p = crear_Primo(ceros = (int(args.tamaño)))
    else:
        p = crear_Primo()

if args.verbosity is not None:
    if args.tamaño is not None:
        q = crear_Primo(v = True, ceros = (int(args.tamaño)))
    else:
        q = crear_Primo(v = True)
else:
    if args.tamaño is not None:
        q = crear_Primo(ceros = (int(args.tamaño)))
    else:
        q = crear_Primo() 

n = producto(p, q)
Euler = Euler(p, q)
while True:
    e = random.randint(10**3, 10**6)
    if tieneInverso:
        break

d = euclides(e, Euler)
    
print("Primo número 1: {p} | Primo número 2: {q} | Módulo: {n} | Número de Euler: {E} | Clave pública: {e}".format(p = p, q = q, n = n, E = Euler, e = e))
print("La clave privada es: {d} ¡¡¡AVISO IMPORTANTE!!! Esta clave sólo la puede ver usted. Manténgala a buen recaudo".format(d = d))