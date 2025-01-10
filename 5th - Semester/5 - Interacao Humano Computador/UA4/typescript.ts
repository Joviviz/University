// A
class Produto {
  nome: string;
  preco: number;
  descricao: string;
  quantidade_estoque: number;
  data_recebida: Date;

  constructor(
    nome: string, 
    preco: number, 
    descricao: string, 
    quantiade_estoque: number, 
    data_recebida: Date)
    {
      this.nome = nome;
      this.preco = preco;
      this.descricao = descricao;
      this.quantidade_estoque = quantiade_estoque;
      this.data_recebida = data_recebida;
    }
}

// B

class Venda{
  produtos: Produto[];

  constructor(produtos: Produto[])
  {
    this.produtos = produtos;
  }

  somarValores() : number{
    let total = 0;

    for (const produto of this.produtos){
      total += produto.preco;
    }

    return total;
  }

}

// C
const produto1 = new Produto(
  "Ventilador", 
  30, 
  "Ventilador preto com 3 velocidades", 
  2,
  new Date('2024-10-09')
);

const produto2 = new Produto(
  "Escova de Dente",
  5,
  "Escova de dente rosa",
  1,
  new Date('2024-09-28')
)

const venda = new Venda([produto1, produto2])

const totalVenda = venda.somarValores();
console.log("Total da soma = ", totalVenda);