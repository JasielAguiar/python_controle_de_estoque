def menu():
    print('\n---Controle de Estoque---')
    print('1 - Cadastrar produto')
    print('2 -listar produtos')
    print('3 - Entrada de produto ')
    print('4 - Saida de Produto')
    print('5 -  Salvar dados')
    print('6 - Carregar dados')
    print('0 - Sair')

def cadastrar (produtos):
    codigo = input('Codigo do produto: ')
    nome  = input ('Nome do produto: ')
    quantidade = int(input('Quantidade: '))
    preco = float(input('Preço do produto: '))


    produto = {
        'codigo': codigo,
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade

    }

    produtos.append(produto)
    print('Produto cadastrado com sucesso!')

def listar (produtos):
     if not produtos:
         print('Nenhum produto cadastrado!')
         return

     for p in produtos:
         print(f'{p['codigo']} - {p["nome"]} | Qtd: {p["quantidade"]} | R$: {p["preco"]}')

def entrada(produtos):
    codigo = input('Codigo do produto: ')

    for p in produtos:
        if p['codigo'] == codigo:
            qtd = int(input('uantidade: '))
            p['quantidade'] += qtd
            print('Entrada com sucesso!')
            return
    print('Nenhum produto cadastrado')

def saida(produtos):
    codigo = input('Codigo do produto: ')

    for p in produtos:
        if p['codigo'] == codigo:
            qtd = int(input('Quantidade:'))

            if qtd > p['quantidade']:
                print('Quantidade menor')

            else:
                p['quantidade'] -= qtd
                print('Saida realizada com sucesso!')
            return
    print('Nenhum produto encontrado')

def salvar(produtos):
    with open('estoque.txt' , 'w') as f:
        for p in produtos:
            linha = f'{p['codigo']},{p['nome']}, {p['quantidade']}, {p['preco']}\n'
            f.write(linha)
    print('Produtos salvos com sucesso!')

def carregar():
    produtos = []

    try:
        with open('estoque.txt', "r") as f:
            for linha in f:
                codigo, nome, quantidade, preco = linha.strip().split(',')

                produtos.append({
                    'codigo': codigo,
                    'nome': nome,
                    'quantidade': int(quantidade),
                    'preco': float(preco)


                })

        print('Produtos carregados com sucesso!')
    except:
        print('Nenhum produto encontrado')
    return produtos

def main():
    produtos = []


    while True:
        menu()
        op = input('Escolha:')

        if op == '1':
            cadastrar(produtos)
        elif op == '2':
            listar(produtos)
        elif op == '3':
            entrada(produtos)
        elif op == '4':
            saida(produtos)
        elif op == '5':
            salvar(produtos)
        elif op == '6':
            produtos = carregar()
        elif op == '0':
            break

if __name__ == '__main__':
    main()