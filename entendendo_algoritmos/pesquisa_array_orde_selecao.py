# Escreva a ordenação por seleção

#A função implementa o algoritmo de ordenação por seleção, criando uma nova lista ordenada ao remover repetidamente o menor elemento da lista original.


def buscarMenor(arr): # Define uma função chamada buscarMenor que recebe um array (lista) como parâmetro.
    menor = arr[0]      # Inicializa a variável 'menor' com o primeiro elemento do array.
    menor_indice = 0    # Inicializa a variável 'menor_indice' com 0 (índice do primeiro elemento).
    for i in range(1,len(arr)): # Percorre o array a partir do segundo elemento até o final /  o correto seria colocar o arr entre parenteses e não colchetes pois o len é uma função
        if arr[i] < menor:   # Se o elemento atual for menor que o menor encontrado até agora...
            menor = arr[i]   # Atualiza o valor de 'menor' para o novo menor elemento.
            menor_indice = i # Atualiza o índice do menor elemento encontrado.
    return menor_indice    # Retorna o índice do menor elemento do array.

#utiliza-se o código do exercicio anterior

def ordenacaoporSelecao(arr): # função para ordenação por seleção utilizando um array
    novoArr = []    # cria-se uma nova lista vazia, para armazenar elemmentos em ordem crescente           
    for i in range(len(arr)):  #laço para repetir o processo 
        menor = buscarMenor(arr)     # busca o menor elemento do array
        novoArr.append(arr.pop(menor)) #busca do indice do menor elemento da lista atual / remove e retorna o menor elemento
    return novoArr   #retorno da lista ordenada
# Teste exemplo
print (ordenacaoporSelecao([5, 1, 6, 2, 10,20,30,50]))







