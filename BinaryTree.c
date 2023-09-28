#include <stdio.h>
#include <stdlib.h> 

struct Node {
    int valor;
    struct Node* esquerda;
    struct Node* direita;
};

struct Node* criarNovoNo(int valor) {
    struct Node* novoNo = (struct Node*)malloc(sizeof(struct Node));
    novoNo->valor = valor;
    novoNo->esquerda = NULL;
    novoNo->direita = NULL;
    return novoNo;
}

struct Node* inserirNaBST(struct Node* raiz, int valor) {
    if (raiz == NULL) {
        return criarNovoNo(valor);
    }
    if (valor < raiz->valor) {
        raiz->esquerda = inserirNaBST(raiz->esquerda, valor);
    } else if (valor > raiz->valor) {
        raiz->direita = inserirNaBST(raiz->direita, valor);
    }
    return raiz;
}

 // Função para percorrer a árvore em ordem
void percorrerEmOrdem(struct Node* raiz) {
    if (raiz != NULL) {
        percorrerEmOrdem(raiz->esquerda);
        printf("%d ", raiz->valor);
        percorrerEmOrdem(raiz->direita);
    }
} 
 

// Função para percorrer a árvore em pré-ordem
void percorrerPreOrdem(struct Node* raiz) {
    if (raiz != NULL) {
        printf("%d ", raiz->valor);
        percorrerPreOrdem(raiz->esquerda);
        percorrerPreOrdem(raiz->direita);
    }
}

// Função para percorrer a árvore em pós-ordem
void percorrerPosOrdem(struct Node* raiz) {
    if (raiz != NULL) {
        percorrerPosOrdem(raiz->esquerda);
        percorrerPosOrdem(raiz->direita);
        printf("%d ", raiz->valor);
    }
}

int main() {
    struct Node* raiz = NULL;
    
    // Inserindo valores na árvore de busca binária.
    raiz = inserirNaBST(raiz, 50);
    raiz = inserirNaBST(raiz, 30);
    raiz = inserirNaBST(raiz, 20);
    raiz = inserirNaBST(raiz, 40);
    raiz = inserirNaBST(raiz, 70);
    raiz = inserirNaBST(raiz, 60);
    raiz = inserirNaBST(raiz, 80);

    // Testando a função de percorrer em ordem.
    printf("Árvore em in-ordem: ");
    percorrerEmOrdem(raiz);
    
    printf("\nÁrvore em pré-ordem: ");
    percorrerPreOrdem(raiz);
    
    printf("\nÁrvore em pós-ordem: ");
    percorrerPosOrdem(raiz);

    return 0;
}


