from catalogo import catalogo
from livro import livro
from datetime import datetime # para registro automático da data de empréstimo e devolução no histórico

def interface(): # sistema a ser feito ainda, refere-se ao sistema da biblioteca
    """
    Interface de navegação do usuário
    """
    def today():
      return datetime.now().strftime("%d/%m/%Y") # retorna dia-mês-ano

    while True:

      print('\n===== MENU DA BIBLIOTECA =====')
      print('1 - Buscar livro (por título, autor ou editora)')
      print('2 - Solicitar empréstimo')
      print('3 - Devolver livro')
      print('4 - Entrar na lista de espera')
      print('0 - Sair')

      """
      tratamento de exceção com try e except para caso o usuário insira um número diferente de: 0, 1, 2, 3 e 4
      """
      try:
        opcao = print("Escolha: ")
        if opcao < 0 or opcao > 4:
          print('Erro, digite um número entre 0 e 4 ')
      except ValueError as erro:
        print(f'Erro: {erro}')


      # início do menu

      if opcao == 0:
        print('Saindo do sistema.')
        break

      elif opcao == 1:
        print('escolha o método de busca:')
        print('1 - por título ')
        print('2 - por autor')
        print('3 - por editora ')
        print('4 - por ano ')

        try:
          modo = int(input)('')
        except ValueError:
          print('entrada inválida')
          continue

        termo = int(input('digite o número: ')).strip()

        if modo == 1:
          livroEncontrado = catalogo.buscarPorTitulo(termo)
          if livroEncontrado:
            print(livroEncontrado.__tudoJunto__())
          else:
            print('nenhum livro encontrado com esse título')

        elif modo == 2:
          resultados = catalogo.buscarPorAutor(termo)
          if resultados:
            for i in resultados:
              print(i.__tudoJunto__())
          else:
            print('nenhum livro encontrado com essa editora')

        elif modo == 3:
          resultados = catalogo.buscarPorEditora(termo)
          if resultados:
            for i in resultados:
              print(i.__tudoJunto__())
          else:
            print('nenhum livro encontrado nesse ano')

        else:
           print('opção inválida, deve ser um número entre 1 e 4 ')

      elif opcao == 2:

            # continuar 