#include<stdio.h>
#include<stdlib.h>

void sort(unsigned char *);
void mediana(unsigned char *, int, int, unsigned char *); // alterando o tipo de dado para unsigned char para combinar com o modelo uint8 passado em python
int pos(int, int, int);

int pos (int numColunas, int linhaAtual, int colunaAtual)
{ 
    return numColunas * linhaAtual + colunaAtual; // função reescrita para encontrar a posição referente a um pixel numa matriz 2D em uma matriz 1D
}

void sort(unsigned char *vetor) { // função de ordenação 
    int i, j, aux; 
 
    for(i = 1; i < 9; i++){ 
        j = i; 
 
        while((j != 0) && (vetor[j] < vetor[j - 1])) { 
            aux = vetor[j]; 
            vetor[j] = vetor[j - 1]; 
            vetor[j - 1] = aux; 
            j--;     
        } 
    } 
}

void mediana (unsigned char *vetor, int rows, int columns, unsigned char *result) {
    unsigned char mascara[9];

    for (int i = 1; i < rows - 1; i++) {
        for (int j = 1; j < columns - 1; j++){

            mascara[0] = vetor[pos(columns, (i-1), (j-1))]; // definição dos valores da mascara onde será aplicada a ordenação para conseguirmos
            mascara[1] = vetor[pos(columns, (i), (j-1))];   // a mediana referente à vizinhança do pixel na posição (i,j) da imagem
            mascara[2] = vetor[pos(columns, (i+1), (j-1))]; 
            mascara[3] = vetor[pos(columns, (i-1), (j))];
            mascara[4] = vetor[pos(columns, (i), (j))];
            mascara[5] = vetor[pos(columns, (i+1), (j))];

            mascara[6] = vetor[pos(columns, (i-1), (j+1))];  
            mascara[7] = vetor[pos(columns, (i), (j+1))];    
            mascara[8] = vetor[pos(columns, (i+1), (j+1))];  

            sort(mascara); // ordenando a mascara com os valores da vizinhança do pixel desejado

            unsigned char mediana = mascara[4]; // pegando o valor central da mascara

            result[pos(columns, i, j)] = mediana; // aplicando o valor da mediana no pixel correspondente da imagem resultante
        }
    }
}
