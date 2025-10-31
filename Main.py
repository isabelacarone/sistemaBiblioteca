import random
from Classes.Catalogo import Catalogo
from Classes.Livro import Livro
from Classes.Usuario import Usuario
from Classes.Interface import interface
from Dados.BaseLivros import BASE_LIVROS
from Dados.BaseUsuarios import NOMES_USUARIOS

def carregar_livros(catalogo: Catalogo):
    """
    Função para carregar a base de livros no catálogo de forma silenciosa.
    """
    print("Carregando base de dados de livros...")
    for titulo, autor, ano, editora, qtd in BASE_LIVROS:
        catalogo.adicionar_livro(Livro(titulo, autor, ano, editora, qtd), silencioso=True)
    print(f"{len(BASE_LIVROS)} livros foram carregados com sucesso.")


def simular_mvp_detalhado(catalogo: Catalogo):
    """
    Executa a simulação de MVP detalhada, com nomes de usuários reais para as
    devoluções e um output mais limpo e espaçado.
    """

    todos_os_titulos = [livro_info[0] for livro_info in BASE_LIVROS]
    titulos_para_simulacao = random.sample(todos_os_titulos, 12)

    livro_grupo_a = catalogo.buscar_por_titulo(titulos_para_simulacao[0])
    livro_grupo_b = catalogo.buscar_por_titulo(titulos_para_simulacao[1])
    livros_espalhados = [catalogo.buscar_por_titulo(t) for t in titulos_para_simulacao[2:]]
    livros_da_simulacao = [livro_grupo_a, livro_grupo_b] + livros_espalhados

    # Dicionário para guardar quem pegou qual livro "emprestado" na simulação.
    emprestimos_fantasmas = {}

    for livro in livros_da_simulacao:
        if livro:
            livro.disponiveis = 0
            livro.emprestados = livro.quantidade

            usuarios_para_fila = random.sample(NOMES_USUARIOS, 10)
            for nome in usuarios_para_fila:
                livro.emprestar(Usuario(nome))

            # Seleciona 5 usuários únicos da base para serem os "doadores" deste livro.
            doadores_deste_livro = [Usuario(nome) for nome in random.sample(NOMES_USUARIOS, 5)]
            emprestimos_fantasmas[livro.titulo] = doadores_deste_livro

            # Injeta os empréstimos fantasmas usando os nomes reais selecionados.
            for doador in doadores_deste_livro:
                livro.historico._emprestimos.push({
                    "usuario": doador.nome,
                    "dataEmprestimo": "2025-10-01 10:00:00",
                    "dataDevolucao": None
                })

    # Grupo A: 5 notificações para o mesmo livro
    print(f"\n-- Processando 5 devoluções para '{livro_grupo_a.titulo}', {livro_grupo_a.autor} --\n")
    doadores_grupo_a = emprestimos_fantasmas[livro_grupo_a.titulo]
    for i, doador in enumerate(doadores_grupo_a, 1):
        print(livro_grupo_a.devolver(doador))
        print()

    # Grupo B: 5 notificações para o segundo livro.
    print(f"\n-- Processando 5 devoluções para '{livro_grupo_b.titulo}', {livro_grupo_b.autor} --\n")
    doadores_grupo_b = emprestimos_fantasmas[livro_grupo_b.titulo]
    for i, doador in enumerate(doadores_grupo_b, 1):
        print(livro_grupo_b.devolver(doador))
        print()

    # Grupo C: 10 notificações espalhadas.
    print("\n-- Processando 10 devoluções espalhadas --")
    for livro in livros_espalhados:
        if livro and livro.historico.has_reservas():
            # Pega o primeiro "doador" da lista daquele livro para a devolução.
            doador_designado = emprestimos_fantasmas[livro.titulo][0]
            mensagem = livro.devolver(doador_designado)
            print(f"'{livro.titulo}', {livro.autor}:\n{mensagem}")
            print()

# Bloco de execução principal.
if __name__ == "__main__":
    print("Inicializando o sistema da biblioteca...")
    cat = Catalogo()

    carregar_livros(cat)
    simular_mvp_detalhado(cat)

    interface(cat)