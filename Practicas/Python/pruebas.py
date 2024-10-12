##Ejercicio 1

num1 = float (input("Introduce el primer numero: "))
num2 = float (input("Introduce el segundo numero: "))
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicacion: {num1 * num2}")
print(f"Division: {num1 / num2}")




##Ejercicio 2 (for)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:  
    if numero % 2 == 0:  
        print(numero)  



#Ejercicio 3 Numeros primos

num = int(input("Introduce un número entero positivo: "))

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"Números primos hasta {num}:")
for i in range(2, num + 1):
    if es_primo(i):
        print(i)


# Ejercicio 4 Funciones

## 1
def saludar ():
    print ("Hola mundo")
    saludar()

## 2
def saludar (nombre = "Mundo"):
    print (f"Hola, {nombre}")
    saludar()
    
# Ejercicio 5 Funciones suma pares

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    

def suma_pares():
    suma = 0  
    for numero in lista:  
        if numero % 2 == 0:  
            suma += numero  
    return suma  


resultado = suma_pares()
print(f"La suma de los números pares es: {resultado}")


# Ejercicio 5 Funciones con while

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    

def suma_pares():
    suma = 0  
    i = 0  

    while i < len(lista):  
        if lista[i] % 2 == 0:  
            suma += lista[i]  
        i += 1  
    
    return suma  

resultado = suma_pares()
print(f"La suma de los números pares es: {resultado}")


# Ejercicio 6 Palindromo


def es_palindromo(cadena):
    
    cadena = cadena.replace(" ", "").lower()
    return cadena == cadena[::-1]

cadena = input("Introduce una palabra o frase: ")


if es_palindromo(cadena):
    print(f"'{cadena}' es un palíndromo.")
else:
    print(f"'{cadena}' no es un palíndromo.")


# Ejercicio 7 Eventos y conjuntos


asistentes_evento_1 = {"Juan", "Ana", "Pedro", "Marta", "Luis"}
asistentes_evento_2 = {"Ana", "Carlos", "Pedro", "María", "Luis"}

## Interseccion
def asistentes_ambos_eventos(evento_1, evento_2):
    return evento_1.intersection(evento_2)

## Union
def asistentes_unicos(evento_1, evento_2):
    return evento_1.union(evento_2)

## Diferencia
def asistentes_solo_evento_1(evento_1, evento_2):
    return evento_1.difference(evento_2)


# Mostrar resultados

print("Asistentes en ambos eventos:")
print(asistentes_ambos_eventos(asistentes_evento_1, asistentes_evento_2))

print("\nAsistentes que solo estuvieron en el primer evento:")
print(asistentes_solo_evento_1(asistentes_evento_1, asistentes_evento_2))

print("\nAsistentes únicos en ambos eventos combinados:")
print(asistentes_unicos(asistentes_evento_1, asistentes_evento_2))


# Ejercicio 8 Diccionarios



 