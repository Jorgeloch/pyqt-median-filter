#include<stdio.h>
#include<stdlib.h>

void sort(int *);
void mediana(int *, int, int, int *);
int pos(int, int, int);

int pos (int numColunas, int linhaAtual, int colunaAtual)
{
    return numColunas * linhaAtual + colunaAtual;
}

void sort(int *vetor) {
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

void mediana (int *vetor, int rows, int columns, int *result) {
    int mascara[9];

    for (int i = 1; i < rows - 1; i++) {
        for (int j = 1; j < columns - 1; j++){

            mascara[0] = vetor[pos(columns, (i-1), (j-1))];
            mascara[1] = vetor[pos(columns, (i), (j-1))];
            mascara[2] = vetor[pos(columns, (i+1), (j-1))];

            mascara[3] = vetor[pos(columns, (i-1), (j))];
            mascara[4] = vetor[pos(columns, (i), (j))];
            mascara[5] = vetor[pos(columns, (i+1), (j))];

            mascara[6] = vetor[pos(columns, (i-1), (j+1))];  // definição das mascara onde será aplicada a ordenação para conseguirmos
            mascara[7] = vetor[pos(columns, (i), (j+1))];    // a mediana referente ao pixel na posição (i,j) da imagem
            mascara[8] = vetor[pos(columns, (i+1), (j+1))];  

            sort(mascara);

            int mediana = mascara[4];

            result[pos(columns, i, j)] = mediana;
        }
    }
}
