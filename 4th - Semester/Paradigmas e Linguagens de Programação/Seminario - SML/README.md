# Standard Meta Language (SML)

## O que é ?
É uma linguagem de programação conhecida por suas fortes capacidades em programação funcional. Desenvolvida para apoiar a implementação de sistemas de inferência (afirmar a verdade de uma proposição na qual há uma ligação entre essa e outras proposições conehcidas como verdadeiras)

## Características
- Tem declarações de tipo
- Inferência de tipo (se x e y são int, então x + y = int)
- Fortemente tipada
  - O tipo de todo nome e expressão é determinado na hora de compilação
  - Diferente de Python que é dinâmico


# Uso da linguagem em código

## Variáveis

variáveis a,b e c

```sml
val a = 2;
val b = 3;
val c = a + b;
```

## Operações básicas de lista
- null(x) - retorna "true" se x for uma lista vazia
- hd(x) - retorna a "cabeça" de x
- tl(x) - reorna a "calda" de x
- a::x  - controi uma lista com a cabeça "a" e calda "x"

### Exemplos

- hd([1,2,3]) = 1
- tl([1,2,3]) = [2,3]
- 1::[2,3] = [1,2,3]


## Funções em ML

- Definidas usando a sintaxe:
  - fun [nome] [parametros] = [corpo]

- Exemplo:
```sml
fun teste n = n+1;
(*Chamar a funcao = teste(x) ou teste x *)
teste(3)
```

## Funcoes de listas lineares
- A maioria das funcoes de lista operam em cada item dentro de uma lista: 
  fun f(x) = 
  if lista x esta vazia then ...
  else something involvendo hd(x), tl(x)

- Exemplo:
```sml
fun tamanhoLista(x) = 
  if null(x) then 0
  else 1 + tamanhoLista(tl(x));

tamanhoLista([0,1,2]);
```

## Operacoes de lista

- append(x,z)
    - adicionar uma lista ou um valor  a uma lista
    - append ([1,2],[3,4,5]) = [1,2] @ [3,4,5]

```sml
val x : int list = [1,2];
val z = [3,4,5];

val xz = x@z;
```

- Criando funcao de append
```sml
val x : int list = [1,2];
val z = [3,4,5];

fun append(x,z) = 
  if null(x) then z
  else hd(x) :: append(tl(x),z);

append(x,z);
```
- Funcoes recursivas sao compostas de um caso base e um caso recursivo
append ([1,2],[3,4,5])

- Exemplo da ordem de recursividade do codigo acima

1. append([1,2],[3,4,5])

2. 1 :: append([2],[3,4,5])
3. 1 :: 2 :: append([],[3,4,5])
4. 1 :: 2 :: [3,4,5]
5. 1 :: [2,3,4,5] = [1,2,3,4,5]

- Reverse(x,y)
  - reverter x e acrescentar em z
  - reverse([2,3,4],[1]) = [4,3,2,1]
- No ML a funcao se chama rev
  - rev(x) = revese(x,[])

```sml
rev([1,2,3,4]);
```

- Criando a funcao reverse
```sml
val x = [2,3,4];
val z = [1];

fun reverse(x,z) = 
  if null(x) then z
  else reverse(tl(x), hd(x)::z);

reverse(x,z);
```

1. reverse([2,3,4][1])
2. reverse([3,4], 2::[1]) -> reverse([3,4], [2,1])
3. reverse([4], 3::[2,1]) -> reverse([4], [3,2,1])
4. reversse([], 4::[3,2,1]) -> reverse([],[4,3,2,1])
5. [4,3,2,1]

- Tempo = O(n) onde n é o tamanho de x

- Implementando reverse usando append

```sml
val x = [1,2,3,4];

fun reverse(x) = 
  if null(x) then nil
  else reverse(tl(x)) @ [hd(x)];

reverse(x);
```

1. reverse [1,2,3,4]
2. reverse [2,3,4] @ [1]
3. reverse [3,4] @ [2] @ [1]
4. reverse [4] @ [3] @ [2] @ [1]
5. reverse [] @ [4] @ [3] @ [2] @ [1]
6. [] @ [4] @ [3] @ [2] @ [1]
7. [4] -> [4,3] -> [4,3,2] -> [4,3,2,1]

- Tempo = O(n^2) onde n é o tamanho de x
  - append = O(n)
  - reverse -> executado n vezes

## Casos e padroes
- Funcoes de lista sao compostas por 2 casos:
  - Caso Base -> para a lista vazia
  - Caso Recursivo -> para a lista não vazia

- tamanho([]) == 0
- tamanho(a::y) == 1 + tamanho(y)

- relembrando a funcao do comeco
```sml
fun tamanhoLista(x) = 
  if null(x) then 0
  else 1 + tamanhoLista(tl(x));

tamanhoLista([0,1,2]);
```

- Podemos reescrever assim: 
```sml
fun tamanhoLista([]) = 0
  | tamanhoLista(a::y) = 1 + tamanhoLista(y);

tamanhoLista([0,1,2]);
```

- Reescrevendo a funcao append:
- Funcao sem padrao
```sml
val x = [1,2];
val z = [3,4,5];

fun append(x,z) = 
  if null(x) then z
  else hd(x) :: append(tl(x),z);

append(x,z);
```

- Funcao com padrao
```
val x = [1,2];
val z = [3,4,5];

fun append([],z) = z
  if null(x) then z
  else hd(x) :: append(tl(x),z);

append(x,z);
```




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

## Função print

```sml
val _ = print "baldurs gate 3";
```

# Magneto

# Ref Bibliográficas
- https://www.youtube.com/watch?v=2sqjUWGGzTo
- 


- https://www.cs.princeton.edu/courses/archive/fall08/cos441/notes/lect-SMLNJ.pdf
- https://www.geeksforgeeks.org/what-is-standard-meta-language-sml/
- 
