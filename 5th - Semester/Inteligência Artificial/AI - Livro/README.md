# Exercícios do Livro Faceli, Katti, et al. Inteligência Artificial - Uma Abordagem de Aprendizado de Máquina. Disponível em: Minha Biblioteca, (2nd edição). Grupo GEN, 2021.
# Exercícios

## Exercício 1

Discuta as semelhanças e diferenças entre aprendizado supervisionado e não supervisionado.

<h3><ins>Resposta: </ins></h3>
<p>Ambos tipos de aprendizado visam extrair informações e dados para fazer previsões ou inferências com fim de entender esses padrões coletados. O paradigma de aprendizado preditivo tem como objetivo mapear a melhor função para mapear as entradas e saídas, as entradas e saídas são conhecidas, por isso o nome "supervisionado", já no caso do paradigma descritivo, ao invés de predizer um valor, o objetivo é extrair padrões ou agrupamentos dos valores preditivos de um conjunto de dados, explorando sua estrutura, marcante pelas saídas serem desconhecidas.</p>


## Exercício 2

Descreva uma situação em que um algoritmo preditivo pode ser usado em uma tarefa descritiva e uma situação em que um algoritmo descritivo pode ser usado em uma tarefa preditiva.

<h3><ins>Resposta: </ins></h3>
<p>Para um algoritmo preditivo em uma tarefa descritiva seria um que analisa sentimentos em uma rede social, utilizando um modelo supervisionado é possível usar um classificador de sentimentos (Feliz, Neutro, Triste), assim seria possível prever os sentimentos para uma postagem. Esse método seria utilizado de forma descritiva para sumarizar os sentimentos predominantes em um grande número de postagens</p>

<p>Para um algoritmo descritivo em uma tarefa preditiva seria um que preve a demanda de produtos de uma loja, normalmente seria utilizado um algoritmo preditivo de regressão linear, porém vamos utilizar uma análise de agrupamento para identificar segmentos de produtos e depois usar essas informações para prever a demanda futura com segmentos de grupos semelhantes, identificando padrões de comportamento entre diferentes grupos de produtos</p>

## Exercício 3

Pesquise sobre as principais formas de inferência (indução, dedução, abdução) e apresente suas características.

<h3><ins>Resposta: </ins></h3>
<p>A inferência de dedução é a mais simples, pois parte de uma premissa maior para uma menor sem adicionar nada além do que já é conhecimento, é muito útil para aplicar regras gerais a casos particulares. Exemplo: O sol nasceu no leste hoje, o sol nasceu no leste ontem, o sol nasceu no leste no dia anterior a ontem, o sol nasceu no leste nos últimos três dias. Logo o sol sempre nasce no Leste. Esse método sofre de generalizações prematuras ou de excessões.</p>

<p>A inferência de indução ou sintética, é mais do que aplicar uma regra geral a um caso particular, diferente da dedutória, este parte de uma premissa menor para uma maior. A indução parte de uma inferência de uma regra a partir do caso e do resultado. Sendo assim, ela ocorre quando generalizamos a partir de certo número de casos em que algo é verdadeiro e inferimos que a mesma coisa será verdadeira do total da classe. É necessário destacar a diferença entre hipótese e indução, a indução infere a existência de fenômenos semelhantes aps que observamos em casos similares, ao passo que a hipótese supõe algo de tipo diferente do que diretamente observamos e , com frequência, de algo que nos seria impossível observar diretamente. Em resumo, indução é muito mais forte que a hipótese.</p>

<p>A inferência por abdução ou hipótese consiste em estudar fatos e inventar uma teoria para explicá-los. A dedução prova algo que deve ser, a indução mostra algo que atualmente é operatório, já a abdução faz uma mera sugestão de algo que pode ser. Para fins de compreender e apreender fenômenos só o raciocínio abdutivo pode funcionar, este são as hipóteses que formulamos antes da classificação do caso.</p>


## Exercício 4

Caracterize cada uma das tarefas a seguir como preditivas ou descritivas:

a. Diagnóstico de pacientes a partir de seus sintomas;

b. Segmentação de mercado, buscando perfis de clientes de acordo com suas características;

c. Identificação de produtos vendidos frequentemente juntos;

d. Reconhecimento de pessoas por suas faces;

e. Previsão de cotação de moedas.

<h3><ins>Resposta: </ins></h3>
<p>
  <ul>
    <li>a - Preditiva</li>
    <li>b - Descritiva</li>
    <li>c - Descritiva</li>
    <li>d - Preditiva</li>
    <li>e - Preditiva</li>
  </ul>
</p>

## Exercício 5

Segundo Mitchell (1997), um programa aprende a partir de um conjunto de experiência E, em relação a uma classe de tarefas T, com medida de desempenho P, se seu desempenho em T, medido por P, melhora com E. A partir dessa definição, apresente quais são os conjuntos T, P e E nos seguintes casos:

a. Jogar damas;

b. Filtrar mensagens de spam;

c. Reconhecer escrita manual de dígitos;

d. Dirigir um carro (carro autônomo);

e. Decidir a que clientes fornecer crédito;

f. Diagnosticar pacientes a partir de seus sintomas.

<h3><ins>Resposta: </ins></h3>

* A
    * (T) Jogar damas
    * (P) Porcentagem de partidas ganhas
    * (E) Jogar contra uma outra versão de si mesmo
* B
    * (T) Filtrar mensagens por spam
    * (P) Porcentagem de emails classificados de forma correta
    * (E) Agrupamento de conjuntos de mensagens que são classificadas como spam
* C
    * (T) Reconhecer escrita manual de dígitos
    * (P) Porcentagem de digitos escritos de forma correta
    * (E) Agrupamento de digitos escrito de forma correta visando ser inspirado a eles
* D
    * (T) Dirigir um carro
    * (P) Porcentagem de destinos alcançados
    * (E) Análise de diferentes atitudes corretas durante o trânsito
* E
    * (T) Decidir a que clientes fornecer crédito
    * (P) Sistema de recompensar a máquina por clientes avaliados de forma correta
    * (E) Comparar 
* F
    * (T) Diagnosticar pacientes a partir de sintomas
    * (P) Porcentagem de pacientes avaliados corretamente
    * (E) Observação da relação entre sintomas e doenças pela probabilidade de ter a doença, retirados de um conjunto de pacientes

