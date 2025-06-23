# Pesquisa Binária
# Neste primeiro exemplo o código utilizará arrays. 

# Podemos armazenar uma sequência de elementos em uma linha de buckets(quadradinho/baldes) consecutivos que se chamam arrays.
# Os buckets são numerados a partir de 0 
# O primeiro bucker está na posução #0, o segundo na posição #1 e o terceiro na posição #2 e assim por diante.

# Passo 01 A função pesquisa_binaria pega um array ordenado e um item.
#Se o item está no arrar a função retonar a posição do mesmo.
# Desta forma é possível continuar procurando o elemento

#baixo = 0 (primeiro elemento)
#alto = len(lista) - 1 (último elemento da lista)

#A cada tentativa você testa para o elemento central

#baixo = 0
#alto = len(lista) - 1

# A cada tentativa você testa para o elemento central 

#meio = (baixo + alto) / 2
#chute = lista[meio]

# o meio será arredondado para baixo (baixo + alto) em python se não for um número par

#se o chute for muito baixo você atualizará a variável abaixo
#if chute < item:
#   baixo = meio + 1

# se o chute for muito alto você atualizará a variável alto

#baixo e alto acompanha ( faz parte) da lista de pesquisa binária
def pesquisa_binaria(lista,item): #a funcção chama a lista e o item
    baixo = 0
    alto = len(lista)-1           # retorna o tamanho da lista, ou seja, a quantidade de elementos que ela possui.
    while baixo <= alto:           
        meio = (baixo+alto)//2    #verifica o elemento central lembrando que ao dividir devo colocar um float representado por //
        chute = lista[meio]       #Pega o valor do elemento na posição central da lista para comparar com o valor que você está procurando.
        if  chute == item:           # acha o item
            return  meio
        if chute > item:           # se o chute for mais alto do que o item retorne o meio -1 da lista 
             alto = meio - 1 
        else:
             baixo = meio + 1          #se o chute for menor que o item faça meio + 1 
    return None               # se o item não existir retorne nulo
      
minha_lista = [1,3,5,7,9]

print (pesquisa_binaria(minha_lista, 3)) 

print (pesquisa_binaria(minha_lista, 9))  

# nota no livro o autor não coloco a variavel pesquisa binária dentro de parenteses 
# arrumar identacao correta 
# o return none precisa estar fora do laço do while para retornar o null

# Resultado, neste exemplo o item da lista 3 está na segunda posição 1 e o item 09 está na quarta posição