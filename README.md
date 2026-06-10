📦 Sistema de Controle de Estoque

Descrição

O Sistema de Controle de Estoque é um projeto desenvolvido em Python com o objetivo de auxiliar no gerenciamento de produtos, permitindo o cadastro, controle de entradas e saídas, consulta de estoque e registro de movimentações.

As informações são armazenadas em arquivos de texto, garantindo a persistência dos dados mesmo após o encerramento do programa.

---

Tecnologias Utilizadas

- Python 3
- Arquivos TXT para armazenamento de dados
- Git
- GitHub

---

Como Executar o Programa

Requisitos

- Python 3 instalado no computador.

Passos para Execução

1. Baixe ou clone o projeto.
2. Abra o terminal na pasta do projeto.
3. Execute o arquivo principal:

python main.py

4. O menu principal será exibido no terminal.
5. Escolha uma das opções disponíveis digitando o número correspondente.

---

Funcionalidades Implementadas

1. Cadastro de Produtos

- Cadastro de produtos por categoria.
- Geração automática de código do produto.
- Armazenamento das informações em arquivo de texto.

2. Listagem de Produtos

- Exibição de todos os produtos cadastrados.
- Apresentação de código, nome, quantidade, preço e categoria.

3. Entrada de Produtos

- Atualização da quantidade em estoque.
- Registro da movimentação de entrada.

4. Saída de Produtos

- Redução da quantidade em estoque.
- Verificação da disponibilidade em estoque.
- Registro da movimentação de saída.

5. Histórico de Movimentações

- Consulta de todas as entradas e saídas registradas.

6. Persistência de Dados

- Utilização do arquivo "produtos.txt" para armazenar os produtos.
- Utilização do arquivo "movimentacoes.txt" para armazenar as movimentações.

7. Relatórios

- Relatório de produtos em estoque.
- Relatório de produtos com baixo estoque.
- Relatório de movimentações realizadas.
- Consulta da quantidade disponível de cada produto.
- Exibição organizada das informações para auxiliar o controle do estoque.

---

Estrutura dos Arquivos

projeto/
│
├── main.py
├── produtos.txt
├── movimentacoes.txt
├── README.md
└── demais arquivos do sistema

produtos.txt

Armazena:

- Código
- Nome
- Quantidade
- Preço
- Categoria

movimentacoes.txt

Armazena:

- Tipo da movimentação (ENTRADA ou SAÍDA)
- Código do produto
- Quantidade movimentada

---

Integrantes do Grupo

Integrante 1 – Ruan

Responsável pela implementação do cadastro de produtos, geração automática de códigos e salvamento dos dados em arquivo.

Integrante 2 – Luiz Felipe

Responsável pela implementação da listagem de produtos e leitura dos dados armazenados.

Integrante 3 – Maria Clara e Luiz Felipe

Responsável pela implementação das funcionalidades de entrada e saída de produtos, incluindo a atualização do estoque.

Integrante 4 – Jasiel Aguiar

Responsável pela implementação dos relatórios do sistema, incluindo:

- Relatório de produtos em estoque;
- Relatório de produtos com baixo estoque;
- Relatório de movimentações;
- Consulta de quantidades disponíveis;
- Organização e exibição das informações para análise do estoque.

---

Projeto Acadêmico

Projeto desenvolvido para fins acadêmicos no curso de Análise e Desenvolvimento de Sistemas (ADS) do IFPE - Campus Jaboatão, sob a orientação da prof. Viviane Cristina Oliveira Aureliano, com o objetivo de aplicar conceitos de programação em python.