'''
Autores primeira atividade pratica Compiladores
Joao Pedro Issmael Vieira - 22252263
Eric Gomes Barreto - 22250196
'''
text = input("Texto: ")

total_characters = 0
total_spaces = 0
no_spaces = ""

for ch in text:
    if ch == " ":
        total_spaces += 1
    else:
        total_characters += 1
        no_spaces += ch

print(f"1. - Total de caracteres encontrados: {total_characters}")
print(f"2. - Total de espacos em branco encontrados: {total_spaces}")
print(f"3. - Total de caracteres com espacos em branco encontrados: {total_characters + total_spaces}")
print(f'4. - Saida sem espacos: "{no_spaces}"')