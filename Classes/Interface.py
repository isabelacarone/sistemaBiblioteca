from Classes.Catalogo import Catalogo
from Classes.Usuario import Usuario


def _obter_livro_do_catalogo(catalogo: Catalogo):
    """
    Função auxiliar para pedir um título ao usuário e buscar no catálogo.
    Lida com o caso de o livro não ser encontrado.
    Retorna o objeto Livro ou None.
    """
    titulo = input("Digite o título do livro: ").strip()
    livro = catalogo.buscar_por_titulo(titulo)
    if not livro:
        print("Livro não encontrado no catálogo.")
        return None
    return livro


def _obter_dados_usuario():
    """
    Função auxiliar para pedir nome e e-mail e retornar um objeto Usuario.
    """
    nome = input("Seu nome: ").strip()
    email = input("Seu e-mail (opcional): ").strip()
    return Usuario(nome, email)


def interface(catalogo: Catalogo):
    """
    Função principal que gerencia a interface de linha de comando (CLI) para o usuário.
    Refatorada para maior clareza e menos repetição de código.
    """
    while True:
        print("\n===== MENU DA BIBLIOTECA =====\n")
        print("1 - Buscar Livro")
        print("2 - Solicitar Empréstimo")
        print("3 - Devolver Livro")
        print("4 - Entrar na Lista de Espera")
        print("5 - Ver Lista de Espera de Um Livro")
        print("0 - Sair")

        try:
            opcao = int(input("Escolha: "))
        except ValueError:
            print("Erro: Entrada inválida. Por favor, digite um número.")
            continue

        if opcao == 0:
            print("Saindo do sistema.")
            break

        elif opcao == 1:
            # Lógica de busca
            termo = input("Digite o termo de busca (título, autor ou editora): ").strip()
            # Busca em todos os campos relevantes e junta os resultados.
            resultados = (catalogo.buscar_por_titulo(termo) or []) + \
                         catalogo.buscar_por_autor(termo) + \
                         catalogo.buscar_por_editora(termo)

            # Remove duplicatas se um livro corresponder a múltiplos critérios
            resultados_unicos = list(dict.fromkeys(resultados))

            if resultados_unicos:
                print("\n--- Resultados da Busca ---")
                for livro in resultados_unicos:
                    print(livro)
            else:
                print("Nenhum livro encontrado com o termo informado.")

        elif opcao == 2:
            # Solicitar empréstimo
            livro = _obter_livro_do_catalogo(catalogo)
            if livro:
                usuario = _obter_dados_usuario()
                mensagem = livro.emprestar(usuario)
                print(mensagem)

        elif opcao == 3:
            # Devolver livro
            livro = _obter_livro_do_catalogo(catalogo)
            if livro:
                usuario = _obter_dados_usuario()
                mensagem = livro.devolver(usuario)
                print(mensagem)

        elif opcao == 4:
            # Entrar na lista de espera
            livro = _obter_livro_do_catalogo(catalogo)
            if livro:
                if livro.disponiveis > 0:
                    print("Há exemplares disponíveis. Use a opção 2 para solicitar o empréstimo.")
                else:
                    usuario = _obter_dados_usuario()
                    mensagem = livro.emprestar(usuario)
                    print(mensagem)

        elif opcao == 5:
            # Ver lista de espera de um livro
            livro = _obter_livro_do_catalogo(catalogo)
            if livro:
                # --- MUDANÇA APLICADA AQUI ---
                # Em vez de acessar '_reservas', usamos os métodos públicos.
                if not livro.historico.has_reservas():
                    print("Não há ninguém na lista de espera para este livro.")
                else:
                    reservas = livro.historico.get_reservas()
                    print(f"\n--- LISTA DE ESPERA DE '{livro.titulo.upper()}' ---")
                    for i, r in enumerate(reservas, 1):
                        print(f'{i}º - {r["usuario"]} (reserva feita em {r["dataReserva"].strftime("%d/%m/%Y %H:%M")})')
                # ---------------------------------

        else:
            print("Erro! Digite um número entre 0 e 5.")