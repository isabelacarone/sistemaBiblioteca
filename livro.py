
from TAD.fila import ArrayQueue
from TAD.pilha import ArrayStack
from emprestimo import Emprestimo   # mudar o que tem empretismo para historico 
from reserva import Reserva         # mudar o que tem reserva para historico 
'''
__tudoJunto__() => retorna uma str detalhada para listar tudo 
emprestar() => registra um novo emprestimo se tiver livros disp.. caso contrario vai adiciona o usuário à fila de espera
devolver() => encerra o emprestimo ativo de um usuário
libera um livro e se tiver fila de espera vai avisar o prox usuario
'''
# ta finalizado, nao muda

class Livro:
    """
    classe que representa um livro no sistema da biblioteca.
    cada livro possui informações básicas (titulo, autor, ano, editora e qntd),
    alem de estruturas auxiliares para controle de !emprestimos! e !reservas!
    """

    def __init__(self, titulo, autor, ano, editora, quantidade):
        """
        construtor da classe Livro.
        inicializa os atributos principais e as estruturas de controle
        """
        # declarei tudo pq fiquei com receio kkkkj
        self.titulo = str(titulo)
        self.autor = str(autor)
        self.ano = int(ano)
        self.editora = str(editora)
        self.quantidade = int(quantidade)
        self.disponiveis = int(quantidade)
        self.emprestados = 0

        # pilha para registrar histórico de empréstimos e devoluções
        self.historico = ArrayStack()

        # fila para gerenciar reservas de usuários (ordem de espera)
        self.reservas = ArrayQueue()

    def __str__(self):
        """
        retorna coisas do livro,
        """
        return (
            self.titulo + " — " + self.autor + " (" + str(self.ano) + ") | "
            + "Editora: " + self.editora + " | "
            + "Disponíveis: " + str(self.disponiveis) + "/" + str(self.quantidade) + " | "
            + "Emprestados: " + str(self.emprestados)
        )

    def __tudoJunto__(self):
        """
        a mesma coisa so que no catalogo.py eu usei esse nome...achei mais eficient repetir do que procurar onde tava
        """
        return (
            self.titulo + " — " + self.autor + " (" + str(self.ano) + ") | "
            + "Editora: " + self.editora + " | "
            + "Disponíveis: " + str(self.disponiveis) + "/" + str(self.quantidade)
        )

    def emprestar(self, usuario):
        """
        realiza o emprestimo do livro para um usuário.
        se houver exemplares disponiveis o emprstimo é registrado
        caso contrário, o usuário é adicionado à fila de reservas.
        """
        if self.disponiveis > 0:
            # há exemplares disponíveis
            self.disponiveis -= 1
            self.emprestados += 1
            self.historico.push(Emprestimo(usuario))
            print("empréstimo de '" + self.titulo + "' para " + usuario.nome + " registrado com sucesso.")
        else:
            # nenhum exemplar disponível — adiciona à fila de espera
            self.reservas.enqueue(Reserva(usuario))
            print("não há exemplares disponíveis. " + usuario.nome + " foi adicionado à fila de espera de '" + self.titulo + "'.")

    def devolver(self, usuario):
        """
        registra a devolução de um livro.
        verifica o histórico para encontrar o empréstimo aberto do usuário
        e >>>> caso exista <<<< finaliza o empréstimo e notifica o próximo da fila.
        """
        for registro in reversed(self.historico._data): # percorre tudo ate a base da pilh
            if (
                isinstance(registro, Emprestimo)
                and registro.aberto()
                and registro.usuario.nome == usuario.nome
            ):
                # fecha o empréstimo
                registro.devolver()
                self.disponiveis += 1
                self.emprestados -= 1

                # se houver reservas avisa o prox da fila
                if not self.reservas.is_empty(): # verifica se exiwste alguem 
                    proximo = self.reservas.dequeue()
                    proximo.notificar()
                    print("devolução registrada por " + usuario.nome + ". notificação enviada para " + proximo.usuario.nome + " (24h de prioridade).")
                    return

                print("devolução registrada por " + usuario.nome + ".")
                return

        print("nenhum empréstimo em aberto foi encontrado para este usuário.")
