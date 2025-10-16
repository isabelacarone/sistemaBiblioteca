from datetime import datetime

class Emprestimo:
    """
    classe que representa um empréstimo de um livro feito por um usuário.
    guarda o usuário, a data do empréstimo e, caso já tenha sido devolvido,
    também a data da devolução.
    """

    def __init__(self, usuario, dataEmprestimo=None, dataDevolucao=None):
        """
        construtor da classe Emprestimo.

        parâmetros:
        - usuario: objeto da classe Usuario que representa quem pegou o livro.
        - data_emprestimo: data e hora em que o livro foi emprestado.
          se não for informada, assume o momento atual.
        - data_devolucao: data em que o livro foi devolvido (pode ser None).
        """
        self.usuario = usuario

        # se nenhuma data de empréstimo foi passada, usa o horário atual
        if dataEmprestimo is None:
            self.dataEmprestimo = datetime.now()
        else:
            self.dataEmprestimo = dataEmprestimo

        # a data de devolução só é preenchida quando o livro é devolvido
        self.dataDevolucao = dataDevolucao

    def devolver(self):
        """
        registra a data e hora da devolução do livro.
        """
        self.dataDevolucao = datetime.now()

    def aberto(self):
        """
        retorna True se o empréstimo ainda estiver em aberto,
        ou seja, se a data de devolução ainda não foi registrada.
        """
        return self.dataDevolucao is None

    def __str__(self):
        """ 
        mostra o nome do usuário e o status atual (aberto ou devolvido).
        """
        if self.aberto():
            return self.usuario.nome + " — emprestimo em aberto"
        else:
            dataFormatada = self.dataDevolucao.strftime("%d/%m/%Y")
            return self.usuario.nome + " — devolvido em " + dataFormatada
