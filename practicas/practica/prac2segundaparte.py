#testPrime() que verifique si un numero es primo#

def testPrime(n):
    if n<2:
        return False
    elif n==2:
        return True
    else:
        for i in range(2, n):
            if n%i== 0:
                return False
            elif n%i!=0:
                return True

#prime() que genere los primos menores o iguales que n en los N#

def prime(n):
    if n<2:
        return False
    elif n==2:
        return True
    else:
        for i in range(2, n):
            if n%i== 0:
                return False
            elif n%i!=0:
                return True
num=int(input("De un numero"))
w=2
contador=1
while contador<=n:
    if prime(w):
        print(contador, w)
        contador= contador +1
    w=w+1
    
    #(mcm() que regrese el minimo comun multiplo de dos enteros#

def MCM(r, m):
    if r > m:
        mayor = r
    else:
        mayor = m 

    while(True):
        if((mayor % x == 0) and (mayor % y == 0)):
            MCM = mayor
            break

        mayor += 1

    return MCM

    numero1 = int(input("Inserte un numero"))
numero2 = int(input("Inserte un segundo numero"))

print("El mcm de ", numero1," y ", numero2, "es", MCM(numero1, numero2))


#MCD() que regrese el maximo comun divisor de dos enteros#

def MCD(g, h):
    resto = 0
    while(h>0):
        resto = h
        h = g % h
        g = resto
    return g

numero1 = int(input("Inserte un numero entero: "))
numero2= int(input("Inserte otro numero entero: "))

print("El MCD de ", numero1," y ",numero2," es ", MCD(numero1, numero2))


#twinPrime() que regrese una tupla con los primos gemelos menores o igules que n en los N#

def testPrime(n):
    if n<2:
        return False
    elif n==2:
        return True
    else:
        for i in range(2, n):
            if n%i== 0:
                return False
            elif n%i!=0:
                return True
def twinsprime(comienzo, final):
    for i in range(comienzo, final):
        j=1+2
        if(testPrime(i) and testPrime(j)):
            print(("{:d} y {:d}". format(i, j)))


#theoremArihtmetic() que regrese una lista con la descomposicion en potencias de primos para cualquier n en lo N#

def theoremArihtmetic(n):
    i=2
    factores=[]
    while i*i <= n:
        if n%i:
            1+=1
        else:
            n//=i
            factores.append(n)
            return factores
