'''
Ejercicio 1: Ordenamiento de listas

Requisitos: Escribe una función llamada ordenar_lista que tome una lista de números enteros como argumento y devuelva la lista ordenada en orden ascendente.
Salida esperada: Para ordenar_lista([5, 3, 2, 8, 6, 7]), la salida debería ser [2, 3, 5, 6, 7, 8].

Ejercicio 2: Contador de palabras

Requisitos: Escribe una función llamada contar_palabras que tome una cadena de texto como argumento y 
devuelva un diccionario donde las claves son las palabras únicas en la cadena de texto y los valores son el número de veces que cada palabra aparece.
Salida esperada: Para contar_palabras("hola mundo hola todos"), la salida debería ser {'hola': 2, 'mundo': 1, 'todos': 1}.

Ejercicio 3: Palíndromos

Requisitos: Escribe una función llamada es_palindromo que tome una cadena de texto como argumento y 
devuelva True si la cadena es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda) y False en caso contrario.
La función debe ignorar los espacios, la puntuación y las diferencias entre mayúsculas y minúsculas.
Salida esperada: Para es_palindromo("Anita lava la tina"), la salida debería ser True.

'''



print()
print('---------Ejercicio 1---------------')
print()


def ordenar_lista(lista_numeros):
    lista_ordenada = lista_numeros
    lista_ordenada.sort()
    return lista_ordenada


resultado1 = ordenar_lista([5, 3, 2, 8, 6, 7])

print(f'la lista ordenada en orden ascendente es : {resultado1}')

# * cualquiera de las dos dan el mismo resultado [2, 3, 5, 6, 7, 8]


def ordenar_lista(lista_numeros): return sorted(lista_numeros)


resultado2 = ordenar_lista([5, 3, 2, 8, 6, 7])

print(f'la lista ordenada en orden ascendente es : {resultado2}')



print()
print('---------Ejercicio 2---------------')
print()


def contar_palabras(cadena):

    # * se separa la cadena creando una lista donde cada palabra es un elemento de esa lista
    palabras = cadena.split()

    diccionario = {p: palabras.count(p)
                   for p in palabras if palabras.count(p) > 0}
    # * se esta iterando sobre la lista de palabras y luego se valida que sea mayor a cero, por ultimo se crea un diccionario que contiene a p como llave y el numero de ocurrencias como valor

    if diccionario:
        print("Las palabras y cantidad de veces que aparecen:")
        print(diccionario)
    else:
        print("No hay palabras para contar.")


contar_palabras("hola mundo hola todos")


print()
print('---------Ejercicio 3---------------')
print()


def es_palindromo(cadena):

    # * se pasa toda la frase a minusculas y sin espacios
    frase = cadena.lower().replace(" ", "")

    # * lo que se hace es comparar la frase original con la frase invertida
    if frase == frase[::-1]:
        return True
    else:
        return False


frase = 'Anita lava la tina'

resultado = es_palindromo(frase)

print(
    f'la frase : {frase} deberia ser True si es palindroma, y su salida es: {resultado}')


print()
print('------------------------')
print()