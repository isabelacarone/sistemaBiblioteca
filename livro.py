from historico import Historico

'''
__tudoJunto__() => retorna uma str detalhada para listar tudo 
emprestar() => registra um novo emprestimo se tiver livros disp.. caso contrario vai adiciona o usuário à fila de espera
devolver() => encerra o emprestimo ativo de um usuário
libera um livro e se tiver fila de espera vai avisar o prox usuario
'''

class Livro:
    """
    classe que representa um livro no sistema da biblioteca.
    cada livro possui informações básicas (titulo, autor, ano, editora e qntd),
    alem de estruturas auxiliares para controle de emprestimos e reservas
    """

    def __init__(self, titulo, autor, ano, editora, quantidade):
        """
        construtor da classe Livro.
        inicializa os atributos principais e a estrutura de historico
        """
        self.titulo = str(titulo)
        self.autor = str(autor)
        self.ano = int(ano)
        self.editora = str(editora)
        self.quantidade = int(quantidade)
        self.disponiveis = int(quantidade)
        self.emprestados = 0

        # historico que usa pilha e fila internamente
        self.historico = Historico(self)

    def __str__(self):
        """
        retorna uma string com as informações do livro
        """
        return (
            self.titulo + " — " + self.autor + " (" + str(self.ano) + ") | "
            + "Editora: " + self.editora + " | "
            + "Disponíveis: " + str(self.disponiveis) + "/" + str(self.quantidade) + " | "
            + "Emprestados: " + str(self.emprestados)
        )

    def __tudoJunto__(self):
        """
        a mesma coisa so que no catalogo.py eu usei esse nome
        """
        return (
            self.titulo + " — " + self.autor + " (" + str(self.ano) + ") | "
            + "Editora: " + self.editora + " | "
            + "Disponíveis: " + str(self.disponiveis) + "/" + str(self.quantidade)
        )

    def emprestar(self, usuario):
        """
        realiza o emprestimo do livro para um usuário.
        se houver exemplares disponiveis o emprestimo é registrado
        caso contrário, o usuário é adicionado à fila de reservas.
        """
        if self.disponiveis > 0:
            self.disponiveis -= 1
            self.emprestados += 1
            self.historico.registrarEmprestimo(usuario)
        else:
            self.historico.registrarReserva(usuario)

    def devolver(self, usuario):
        """
        registra a devolução de um livro.
        verifica o histórico para encontrar o empréstimo aberto do usuário
        e caso exista finaliza o empréstimo e notifica o próximo da fila.
        """
        self.historico.registrarDevolucao(usuario)
        self.disponiveis += 1
        self.emprestados -= 1
