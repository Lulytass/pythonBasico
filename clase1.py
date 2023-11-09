print ("Hola Mundo")
print(3+3-2)

#no hace falta estacios ya que python pone los espacios entre los valores
print("hola", "como estas")

#str parsea a string
print("hola", str(58)) 

#distintas formas de imprimir variables 
age = 35
print(f"edad: {age}")
print("edad:", age)
name = "Lucia"
print(f"Nombre: {name}")

#la funcion input permite ingresar datos por teclado y retorna strings
pedirName = input("Ingrese su Nombre:")
print(pedirName) 

#asi parseamos a int lo que ingresa por teclado el usuario
age = int(input("Ingrese su edad:" ))
print(age)

#con end="" escribimos todo en una linea entro de las "" podemos usar el separador que queremos
print("mi nombre es:",name,end=" ") 
print("Mi edad es:", age)

#con type podemos saber el tipo de dato que le pasamos por parametro
print(type(name))

#operador in y not in para saber si el valor pasado esta en la cadena
print("L" in name)
print("C" not in name) 

#potencia
print(8**2)

# Los bloques se indican por indentacion, no se usan llaves en funciones

# Para sentencias de mas de 72 caracteres usamos barra invertida para indicar que sigue abajo o pongo los numeros entro de []

# Las variables no se escriben con camelCase se separan las palabras con _

# Usamos mayusculas para indicarnos entre programadores las constantes, en python no existen las constantes HOLA

# En vez de usa i++ se usa i+=1

# los parametros de range son(desde donde, hasta donde, de a cuanto)
for i in range(20,0,-1): 
    print(i)

for ltra in name:
    print (ltra)
