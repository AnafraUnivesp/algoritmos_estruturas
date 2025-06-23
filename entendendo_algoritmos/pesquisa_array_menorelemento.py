# Encontre o menor elemento de um Array 

def buscarMenor(arr): # Define uma função chamada buscarMenor que recebe um array (lista) como parâmetro.
    menor = arr[0]      # Inicializa a variável 'menor' com o primeiro elemento do array.
    menor_indice = 0    # Inicializa a variável 'menor_indice' com 0 (índice do primeiro elemento).
    for i in range(1,len(arr)): # Percorre o array a partir do segundo elemento até o final /  o correto seria colocar o arr entre parenteses e não colchetes pois o len é uma função
        if arr[i] < menor:   # Se o elemento atual for menor que o menor encontrado até agora...
            menor = arr[i]   # Atualiza o valor de 'menor' para o novo menor elemento.
            menor_indice = i # Atualiza o índice do menor elemento encontrado.
    return menor_indice    # Retorna o índice do menor elemento do array.
# Testando o código
meu_array = [10, 5, 3, 8, 4, 2, 7] # Retorna o índice do menor elemento do array.
menor_indice = buscarMenor(meu_array) # A função buscarMenor(meu_array) é chamada para encontrar o índice do menor elemento da lista.
print(f"O menor elemento está no índice: {menor_indice}") # printa a posição do indice do menor elemento do array neste caso o número 2 está na posição 5
print(f"O menor elemento é: {meu_array[menor_indice]}") # print qual é o menor elemento do array, nestew caso o 2 é o menor número do array
