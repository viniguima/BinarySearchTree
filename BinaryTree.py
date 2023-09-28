# Com base em uma linguagem escolhida a equipe deve mostrar como o conteúdo ministrado em aula pode ser desenvolvido.

# A atividade será avaliada com base em dois critérios:

# - Apresentação da Equipe (que ocorrerá apenas no final do semestre)

# - Escrita de um artigo no formato da SBC explicando o conteúdo passado em aula, de revisão de lista encadeada até Arvores Binárias.

# Entrega 1 - (40% do 1 Bi) 20/09/23

# - Documento no formato SBC com a apresentação inicial da proposta, qual a linguagem e uma introdução sobre o assunto, com referência.



# Entrega 2 (40% do 2 Bi) 08/11/23

# - Finalização do Artigo e Apresentação.

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.esq = None
        self.dir = None

def novoNo(valor):
    return Node(valor)

def inserirNaArvore(raiz, valor):
    if raiz is None:
        return novoNo(valor)
    if valor < raiz.valor:
        raiz.esq = inserirNaArvore(raiz.esq, valor)
    elif valor > raiz.valor:
        raiz.dir = inserirNaArvore(raiz.dir, valor)
    return raiz

def inOrder(raiz):
    if raiz is not None:
        inOrder(raiz.esq)
        print(raiz.valor, end=' ')
        inOrder(raiz.dir)

def preOrder(raiz):
    if raiz is not None:
        print(raiz.valor, end=' ')
        preOrder(raiz.esq)
        preOrder(raiz.dir)

def postOrder(raiz):
    if raiz is not None:
        postOrder(raiz.esq)
        postOrder(raiz.dir)
        print(raiz.valor, end=' ')

def main():
    raiz = None
    valores = [50, 30, 20, 40, 70, 60, 80]
    for valor in valores:
        raiz = inserirNaArvore(raiz, valor)
    
    print("Árvore em in-ordem: ", end='')
    inOrder(raiz)
    
    print("\nÁrvore em pré-ordem: ", end='')
    preOrder(raiz)
    
    print("\nÁrvore em pós-ordem: ", end='')
    postOrder(raiz)

if __name__ == "__main__":
    main()
