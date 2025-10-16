from catalogo import catalogo
from livro import livro
from usuario import Usuario
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
      print('5 - Ver lista de espera de um livro')
      print('6 - Ver total de empréstimos de um livro')

      print('0 - Sair')

      """
      tratamento de exceção com try e except para caso o usuário insira um número diferente de: 0, 1, 2, 3, 4 e 5
      """
      try:
        opcao = int(input("Escolha: "))
        if opcao < 0 or opcao > 5:
          print('Erro, digite um número entre 0 e 5 ')
          continue
      except ValueError as erro:
        print(f'Erro: {erro}')
        continue


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
          modo = int(input('Escolha o modo de busca: '))
        except ValueError:
          print('entrada inválida')
          continue

        termo = input('Digite o termo de busca: ').strip()

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
            print('nenhum livro encontrado com esse autor')

        elif modo == 3:
          resultados = catalogo.buscarPorEditora(termo)
          if resultados:
            for i in resultados:
              print(i.__tudoJunto__())
          else:
            print('nenhum livro encontrado com essa editora')

        elif modo == 4:
          try:
            ano = int(termo)
          except ValueError:
            print('ano inválido')
            continue
          resultados = catalogo.buscarPorAno(ano)
          if resultados:
            for i in resultados:
              print(i.__tudoJunto__())
          else:
            print('nenhum livro encontrado nesse ano')

        else:
           print('opção inválida, deve ser um número entre 1 e 4 ')

      elif opcao == 2:
        # Solicitar empréstimo
        titulo = input('Digite o título do livro que deseja emprestar: ').strip()
        l = catalogo.buscarPorTitulo(titulo)
        if not l:
          print('livro não encontrado.')
          continue

        nome = input('Seu nome: ').strip()
        email = input('Seu e-mail (opcional): ').strip()
        u = Usuario(nome, email)

        try:
          l.emprestar(u)
        except Exception as e:
          print('erro ao registrar empréstimo:', e)

      elif opcao == 3:
        # Devolver livro
        titulo = input('Digite o título do livro que deseja devolver: ').strip()
        l = catalogo.buscarPorTitulo(titulo)
        if not l:
          print('livro não encontrado.')
          continue

        nome = input('Seu nome: ').strip()
        email = input('Seu e-mail (opcional): ').strip()
        u = Usuario(nome, email)

        try:
          l.devolver(u)
        except Exception as e:
          print('erro ao registrar devolução:', e)

      elif opcao == 4:
        # Entrar na lista de espera
        titulo = input('Digite o título do livro: ').strip()
        l = catalogo.buscarPorTitulo(titulo)
        if not l:
          print('livro não encontrado.')
          continue

        if getattr(l, 'disponiveis', 0) > 0:
          print('há exemplares disponíveis. você pode solicitar o empréstimo na opção 2.')
          continue

        nome = input('Seu nome: ').strip()
        email = input('Seu e-mail (opcional): ').strip()
        u = Usuario(nome, email)

        try:
          l.emprestar(u)  # o método emprestar adiciona à fila se não tiver cópias
        except Exception as e:
          print('erro ao entrar na fila de espera:', e)

      elif opcao == 5:
        # Ver lista de espera de um livro
        titulo = input('Digite o título do livro: ').strip()
        l = catalogo.buscarPorTitulo(titulo)
        if not l:
          print('livro não encontrado.')
          continue

        reservas = getattr(l.historico, "_reservas", None)
        if not reservas or reservas.is_empty():
          print("não há ninguém na lista de espera para este livro.")
        else:
          print("\n--- LISTA DE ESPERA DE '" + l.titulo + "' ---")
          posicao = 1
          for r in reservas._data:
            print(str(posicao) + "º - " + r["usuario"] + " (reserva feita em " + r["dataReserva"].strftime("%d/%m/%Y %H:%M") + ")")
            posicao += 1
      elif opcao == 6:
        # Ver total de empréstimos de um livro
        titulo = input('Digite o título do livro: ').strip()
        l = catalogo.buscarPorTitulo(titulo)
        if not l:
          print('livro não encontrado.')
          continue

        totalEmprestimos = len(l.historico._emprestimos._data)
        print("o livro '" + l.titulo + "' já teve " + str(totalEmprestimos) + " empréstimo(s) registrados no histórico.")

