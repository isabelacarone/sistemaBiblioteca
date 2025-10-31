from Classes.Historico import Historico


class Livro:
    """
    Classe que representa um livro no sistema da biblioteca.
    """

    def __init__(self, titulo, autor, ano, editora, quantidade):
        self.titulo = str(titulo)
        self.autor = str(autor)
        self.ano = int(ano)
        self.editora = str(editora)
        self.quantidade = int(quantidade)
        self.disponiveis = int(quantidade)
        self.emprestados = 0
        self.historico = Historico(self)

    def __str__(self):
        return (
            f"{self.titulo} — {self.autor} ({self.ano}) | "
            f"Editora: {self.editora} | "
            f"Disponíveis: {self.disponiveis}/{self.quantidade} | "
            f"Emprestados: {self.emprestados}"
        )

    def emprestar(self, usuario):
        """
        Realiza o empréstimo ou adiciona à fila de reserva.
        Refatoração: Retorna a mensagem de status da operação.
        """
        if self.disponiveis > 0:
            self.disponiveis -= 1
            self.emprestados += 1
            return self.historico.registrar_emprestimo(usuario)
        else:
            return self.historico.registrar_reserva(usuario)

    def devolver(self, usuario):
        """
        Registra a devolução de um livro.
        Refatoração: Retorna a mensagem de status da operação.
        """
        mensagem = self.historico.registrar_devolucao(usuario)

        # Apenas ajusta os contadores se a devolução foi bem-sucedida.
        if "Devolução registrada" in mensagem:
            if self.emprestados > 0:
                self.disponiveis += 1
                self.emprestados -= 1

        return mensagem