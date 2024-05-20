# Standard Meta Language (SML)

É uma linguagem de programação conhecida por suas fortes capacidades em programação funcional. Desenvolvida para apoiar a implementação de sistemas de inferência (afirmar a verdade de uma proposição na qual há uma ligação entre essa e outras proposições conehcidas como verdadeiras)

# Uso da linguagem em codigo

## Variaveis

variaveis a,b e c

```sml
val a = 2;
val b = 3;
val c = a + b;
```

## Funcao print

```sml
val _ = print "baldurs gate 3";
```
## Soma de valores em uma lista

```sml
val lis = [1,2,3,4];

fun somaLista [] = 0
  | somaLista (x::xs) = x + somaLista xs;

val execute = somaLista(lis);
```
# Magneto

# Ref Bibliografica
- https://www.cs.princeton.edu/courses/archive/fall08/cos441/notes/lect-SMLNJ.pdf
- https://www.geeksforgeeks.org/what-is-standard-meta-language-sml/
- 
