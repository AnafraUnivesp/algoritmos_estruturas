# Pesquisa Binária - Exercicio 01 
# Neste primeiro exemplo o código utilizará arrays. 

# SUPONHA QUE VOCÊ TENHA UMA LISTA COM 128 NOMES E ESTEJA  FAZENDO A PESQUISA BINARIA. 
# QUAL SERÁ O NUMERO MÁXIMO DE ETAPAS QUE VOCE LEVARIA PARA ENCONTRAR O NOME DESEJADO

def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    etapas = 0  # contador de etapas
    while baixo <= alto:
        etapas += 1
        meio = (baixo + alto) // 2
        chute = lista[meio]
        if chute == item:
            print(f"Total de etapas: {etapas}")
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    print(f"Total de etapas: {etapas}")
    return None

minha_lista = list(range(1, 129))  # lista de 1 até 128

print(pesquisa_binaria(minha_lista, 128))


# nota no livro o autor não coloco a variavel pesquisa binária dentro de parenteses 
# arrumar identacao correta 
# o return none precisa estar fora do laço do while para retornar o null

# Resultado, neste exemplo o item da lista 3 está na segunda posição 1 e o item 09 está na quarta posição