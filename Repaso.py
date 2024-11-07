
s = "Hello world"
palabras = s.split(' ')
palabras.reverse()
# print(palabras)

abecedario = 'abcdefg'
abecedario.replace('hola','bebe')
# print(abecedario)

espacios = "       H O L A    "
espacios = espacios.strip(' ')
espacios = espacios.split(' ')
# print(espacios)



dos_decimales = round(19.3434,2)
# print(dos_decimales)




def populate_dictionary(arr):
    for i in range(len(arr)):
        if i < len(valores):
            diccionario[valores[i]].append(arr[i])
            print(diccionario)


valores = ['a','b','c']
producto1 = ['nestle', 'jugo', 'mango']
producto2 = ['coca', 'arroz']
diccionario = {key: []  for key in valores}
# print(diccionario)
# populate_dictionary(producto1)
# populate_dictionary(producto2)
# print(diccionario)

# maxima_productos = 0
# if len(producto1)>len(producto2): maxima_productos=len(producto1) 
# else: maxima_productos=producto2

# for items in range(maxima_productos):
#     str =  ' and '.join()
#     #diccionario[valores[i]] 



pila = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f'
]

nueva_pila = ['j', 'k', 'l', 'm','n']

# print(pila.pop())
# pila.append('g')
# pila.extend('h')

# pila.pop()
# print(pila)
# pila.extend(nueva_pila)
# print(pila)

from collections import deque
cola = deque()
cola.append(1)
cola.append(1)
cola.append(2)
print(cola)
cola.popleft()
print(cola)