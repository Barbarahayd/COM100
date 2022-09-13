# Algoritmo de Ordenacao - Por selecao (Selection Sort)
# Para cada posicao do array de elementos procurar o menor elemento e colocar na posicao atual

def sort (array):
    for index in range(0, len(array)):   # para cada posicao iniciando em 0 ate a extencao do array
        menor_elem = index  # atribuir o valor do menor elemento a posicao atual

        for right in range(index +1, len(array)):  # percorrer o restante do array em busca do menor elemento
            if array[right] < array[menor_elem]:  # se o elemento direita for menor que o elem atual
                menor_elem = right  # o indice menor recebera o item da direita

        array[index], array[menor_elem] = array[menor_elem], array[index] # troca do menor na pos. atual

array = [5, 9, 12, 7, 3, 15, 22, 6]
sort(array)
print(array)