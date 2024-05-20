# Standard Meta Language (SML)

## O que é ?
É uma linguagem de programação conhecida por suas fortes capacidades em programação funcional. Desenvolvida para apoiar a implementação de sistemas de inferência (afirmar a verdade de uma proposição na qual há uma ligação entre essa e outras proposições conehcidas como verdadeiras)

## Características
- Tem declarações de tipo
- Inferência de tipo (se x e y são int, então x + y = int)

# Uso da linguagem em código

## Variáveis

variáveis a,b e c

```sml
val a = 2;
val b = 3;
val c = a + b;
```

## Função print

```sml
val _ = print "baldurs gate 3";
```

## Operações básicas de lista
- null(x) - retorna "true" se x for uma lista vazia
- hd(x) - retorna a "cabeça" de x
- tl(x) - reorna a "calda" de x
- a::x  - controi uma lista com a cabeça "a" e calda "x"

hd([1,2,3] = 1)
tl()

## Soma de valores em uma lista



x é o começo da lista e xs o final (x::xs)

```sml
val lis = [1,2,3,4];

fun somaLista [] = 0
  | somaLista (x::xs) = x + somaLista xs;

val execute = somaLista(lis);
```

## Fatorial
```sml
fun fou n = 
  if n = 0
  then 1
  else n * fou (n-1);

val execute = fou(4);
```

OU
```sml
fun fou 0 = 1
  | fou n = n * fou (n - 1);

val fou = fou(4);
```

# Magneto

# Ref Bibliográficas
- https://www.youtube.com/watch?v=2sqjUWGGzTo
- 


- https://www.cs.princeton.edu/courses/archive/fall08/cos441/notes/lect-SMLNJ.pdf
- https://www.geeksforgeeks.org/what-is-standard-meta-language-sml/
- 
