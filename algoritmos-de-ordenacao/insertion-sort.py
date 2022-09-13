# Algoritmo de Ordenacao - Por Insercao (Insertion Sort)
'''Para cada posicao no array verificar se o item da esquerda eh maior, enquanto o item da esquerda
for maior ele muda uma posicao. '''

def sort(array):
    for index in range(0, len(array)):
        current_element = array[index]

        while index > 0 and array[index-1] > current_element:
            array[index] = array[index-1]
            index-=1

            array[index] = current_element

array = [5, 9, 12, 7, 3, 15, 22, 6]

sort(array)

print(array)
