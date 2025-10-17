/*
Nome: João Pedro Issmael Vieira | RA: 22252263
Nome: Diogo Borges de Moura | Ra: 22250783
Data: 25/08/2025
*/

#include <stdio.h>
#include <string.h>
#include <ctype.h>

void funcao1(char texto[]) {
    printf("Digite uma string (pode conter letras maiúsculas ou minúsculas): ");
    fgets(texto, 100, stdin);

    size_t len = strlen(texto);
    if (len > 0 && texto[len - 1] == '\n') {
        texto[len - 1] = '\0';
    }
}

void funcao2(char texto[]) {void funcao2(char texto[]) {

    char minusculo[100], maiusculo[100], invertido[100];
    int i;

    for (i = 0; texto[i] != '\0'; i++) {
        minusculo[i] = tolower((unsigned char)texto[i]);
    }
    minusculo[i] = '\0';

    for (i = 0; texto[i] != '\0'; i++) {
        maiusculo[i] = toupper((unsigned char)texto[i]);
    }
    maiusculo[i] = '\0';

    for (i = 0; texto[i] != '\0'; i++) {
        if (islower((unsigned char)texto[i])) {
            invertido[i] = toupper((unsigned char)texto[i]);
        } else if (isupper((unsigned char)texto[i])) {
            invertido[i] = tolower((unsigned char)texto[i]);
        } else {
            invertido[i] = texto[i]; 
        }
    }
    invertido[i] = '\0';

    printf("\nResultados:\n");
    printf("Minúscula: %s\n", minusculo);
    printf("Maiúscula: %s\n", maiusculo);
    printf("Invertido: %s\n", invertido);
}

int main() {
    char entrada[100];

    funcao1(entrada);
    funcao2(entrada);

    return 0;
}
