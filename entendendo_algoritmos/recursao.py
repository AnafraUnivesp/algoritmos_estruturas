# Recursão

# Olhe o que tem dentro da caixa
# Se encontrar uma caixa volte ao passo 01
# Se encontrar a chave, terminou 

def procure_pela_chave(caixa_principal): #  inicia a pilha com a caixa principal
    pilha = [caixa_principal] #crie uma pilha para armazenar as caixas
    while pilha:    # enquanrto houver caixas para verificar - faça enquanto
        caixa = pilha.pop()   # remove o próximo item da lista
        for item in caixa:             
            if item.e_em_caixa():
                pilha.append(item) #adição à pilha
            elif item.e_uma_chave():
                print("Achei a chave")        
    
# Testando o código - sugerido pela IA

#1. Definir as classes necessárias

# Você precisa de classes para representar:

# Caixa (que pode conter outros itens ou caixas)
# Chave (o objetivo da busca)
# Item comum (qualquer outro objeto que não seja caixa nem chave)

class Item:
    def e_em_caixa(self):
        return False
    def e_uma_chave(self):
        return False

class Caixa(list):
    def e_em_caixa(self):
        return True
    def e_uma_chave(self):
        return False

class Chave(Item):
    def e_uma_chave(self):
        return True

# Montando as caixas e itens
chave = Chave()
caixa_interna = Caixa([chave])
caixa_principal = Caixa([Item(), caixa_interna, Item()])

# Testando a função
procure_pela_chave(caixa_principal)

