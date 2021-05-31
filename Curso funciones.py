print("--------- EJEMPLO 1 ---------\n")
def MuestraNombre(nombre, edad):
    print(f"Saludos {nombre}, yo soy el Arquero, emisario de los gorgonitas.")

    if edad < 18:
        print("Abrete como pistache, morro")
    else:
        print("Adelante camarada mayor de edad")

nombre = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))
MuestraNombre(nombre, edad)

print("\n--------- EJEMPLO 2 ---------\n")
#TABLA DE MULTIPLICAR

def tablaMulti(num):
    print(f"Tabla de multiplicar del número {num}")

    for contador in range(11):
        operacion = num*contador
        print(f"{num} x {contador} = {operacion}")        
tablaMulti(2)
print("\n")

#TABLAs DE MULTIPLICAR

for numero_tabla in range(20,25):
    print('\n')
    tablaMulti(numero_tabla)


print("\n--------- EJEMPLO 3 ---------\n")
#parametros opcionales

def getEmpleado(nombre,dni = None): #Se iguala para ser opcional
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")
    else:
        print("Sin DNI")
getEmpleado("Toño", "332")    # SI NO SE TIENE EL DNI SE SALTA EL IF

print("\n--------- EJEMPLO 4 ---------\n")

#Calculadora

def calculadora(num1, num2, basicas = False):
    suma = num1+num2
    resta = num1-num2
    multi = num1*num2
    division = num1/num2
#montar cadena de texto
    cadena = ""
#concatenando
    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:   
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División: " + str(division)

    return cadena
print(calculadora(3, 9, False))


print("\n--------- EJEMPLO 5 ---------\n")

def usantNomo(nomo):
    texto = f"Te llamas {nomo}"
    return texto

def Apellido(apellidos):    
    texto = f"Tus apellidos son {apellidos}"
    return texto

def devuelveTodo(nomo,apellidos):
    texto = usantNomo(nomo)+"\n"+Apellido(apellidos)
    return texto

print(devuelveTodo("Carlos","Santana"))


print("\n--------- EJEMPLO 5 ---------\n")
#FUNCIÓN LAMBDA, ES ANONIMA hecha para pequeñas funciones

what_year_it_is = lambda year: f"Estamos en el año {year*50-600}"

print(what_year_it_is(5448))

#Variables globlaes vs locales
# Las locales siempre están dentro de una función y acceds a ella mediante la función
# La variable global la puedes acceder desde cualquier parte del código

# se usa el comando global XXXX para volver una función global

# FUNCIONES PREDEFINIDAS
#print()
#type()

print("\n--------- EJEMPLO 6 ---------\n")
#DETECTAR EL TIPADO
Comprueba = isinstance(nombre,int) #La función comprueba que la variable (dentro del parentesis) es el tipo de dato que coloqué después de la coma
if Comprueba:
    print("Es un string")
else:
    print("Es un integer")
    
print("\n--------- EJEMPLO 7 ---------\n")    

# LIMPIAR ESPACIOS

frase1="     Mucho   espacio      .d  "
print(frase1.strip())

print("\n--------- EJEMPLO 8 ---------\n")

# ELIMINAR VARIABLES CON del
año = 2020
del año
# EN EL print MARCA ERROR PORQUE año YA FUE BORRADA Y NO EXISTE
#print(año)

print("\n--------- EJEMPLO 9 ---------\n")

#COMPROBAR VARIABLE VACIA

frase2 = "ff  "
if len(frase2) == 0:
    print("la variable está vacia")
else:
    print("No está vacia, contiene ", len(frase2), "caracteres")

print("\n--------- EJEMPLO 10 ---------\n")

# ENCONTRAR CARACTERES
frase3 = "Perra loca, NO te cruces la calle"
print(frase3.find("calle"))
#IMPRIME EL INDICE DE LA PRIMERA LETRA DE LA COINCIDENCIA

print("\n--------- EJEMPLO 11 ---------\n")

cambia_frase = frase3.replace("Perra loca", "Porfirio")
print(cambia_frase)

#MAYUSCULAS Y MINUSCULAS

print(cambia_frase.lower())
print(cambia_frase.upper())








    












    
