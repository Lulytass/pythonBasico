# declaraciones de funciones
# 1- una funcion que muestre por pantalla 'bienvenidos a python'
def saludar():
    return "bienvenidos a python"

# 2- una funcion que reciba un nombre como parametro y muestre por pantalla  el nombre recibido bienvenido a Python
def bienvenido_nombre(nom):
    return f"{nom} bienvenido a python"

# 3- una funcion que reciba 2 numeros y devuelva la suma
# 3bis - mostrar los parametros por valor
# 4- documentar la funcion con "docString" y usarla
def suma(b, a):
    ''' sumando los numeros'''
    return f"{a}+{b}={a+b}"

# 5- una funcion potencia que reciba 1 parametro o 2
def potencia(a, b=2):
    return a**b

# 6- una funcion que reciba un  lista de numeros y devuelva la suma
def sumar_array(arr):
    total=0
    for num in arr:
        total+=num
    # return sum(lista) y no hace falta la funcion
    # en listas duplas etc como se pasan por referencia la posicion de 
    # memoria cualquier cambio hecho en la funcio muta el objeto, lista,etc
    return total


# llamadas a las funciones

res_saludar = saludar()
print(res_saludar)

nombre=input("ingrese su nombre:")
res_bienvenido_nombre = bienvenido_nombre(nombre)
print(res_bienvenido_nombre)

numero1=float(input("ingrese un numero:"))
numero2=float(input("ingrese otro numero:"))
res_suma = suma(numero1, numero2)
print(f"La suma de {numero1} y {numero2} es {suma(numero1, numero2)}")

base=int(input("Ingrese la base: "))
exponente=int(input("Ingrese un exponente: "))
res_potencia = potencia(base, exponente)
print(res_potencia)

num = float(input("ingrese un numero o 0 para salir: "))
numeros_arr = []
while num != 0:
    numeros_arr.append(num) 
    num = float(input("ingrese un numero o 0 para salir: "))
res_sumar_array = sumar_array(numeros_arr)
print(res_sumar_array)

