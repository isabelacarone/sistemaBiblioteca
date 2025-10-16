from datetime import datetime, timedelta
from TAD.pilha import ArrayStack
from TAD.fila import ArrayQueue

'''
controla o histórico de empréstimos e reservas de um livro 
usando uma pilha e uma fila.

self._livro => referência para o livro ao qual o histórico pertence
self._emprestimos => pilha com os registros de empréstimos
self._reservas => fila com os registros de reservas

registrarEmprestimo() => adiciona um novo empréstimo na pilha
registrarDevolucao() => encerra o empréstimo em aberto de um usuário e notifica a fila
registrarReserva() => adiciona um novo registro de reserva na fila
_notificarProximoReserva() => envia notificação ao primeiro usuário da fila
exibirHistorico() => mostra todas as operações de empréstimos e reservas do livro
'''

class Historico:

    def __init__(self, livro):
        # cria o histórico vinculado a um livro específico
        self._livro = livro
        self._emprestimos = ArrayStack()  # pilha de empréstimos
        self._reservas = ArrayQueue()     # fila de reservas

    def registrarEmprestimo(self, usuario):
        """
        registra um novo empréstimo e adiciona na pilha
        """
        registro = {
            "usuario": usuario.nome,
            "dataEmprestimo": datetime.now(),
            "dataDevolucao": None
        }
        self._emprestimos.push(registro)
        print("empréstimo de '" + self._livro.titulo + "' feito por " + usuario.nome + " registrado com sucesso.")

    def registrarDevolucao(self, usuario):
        """
        percorre a pilha do topo para base buscando empréstimo aberto
        e marca a data de devolução, notificando o próximo da fila se existir
        """
        temp = ArrayStack()
        devolvido = False

        while not self._emprestimos.is_empty():
            emp = self._emprestimos.pop()
            if emp["usuario"] == usuario.nome and emp["dataDevolucao"] is None:
                emp["dataDevolucao"] = datetime.now()
                devolvido = True
                print("devolução registrada para " + usuario.nome + ".")
                self._notificarProximoReserva()
            temp.push(emp)

        # restaura a pilha original
        while not temp.is_empty():
            self._emprestimos.push(temp.pop())

        if not devolvido:
            print("nenhum empréstimo em aberto encontrado para " + usuario.nome + ".")

    def registrarReserva(self, usuario):
        """
        adiciona um novo registro de reserva na fila
        """
        reserva = {
            "usuario": usuario.nome,
            "dataReserva": datetime.now(),
            "notificadoEm": None,
            "expiraEm": None
        }
        self._reservas.enqueue(reserva)
        print("reserva registrada para " + usuario.nome + ".")

    def _notificarProximoReserva(self):
        """
        notifica o primeiro usuário da fila de reservas, se existir
        """
        if self._reservas.is_empty():
            return

        reserva = self._reservas.dequeue()
        reserva["notificadoEm"] = datetime.now()
        reserva["expiraEm"] = reserva["notificadoEm"] + timedelta(hours=24)
        print(
            "usuário " + reserva["usuario"] + " foi notificado. prioridade válida até "
            + reserva["expiraEm"].strftime("%d/%m %H:%M") + "."
        )

    def exibirHistorico(self):
        """
        exibe todas as operações de empréstimos e reservas
        """
        print("\n===== HISTÓRICO DO LIVRO: " + self._livro.titulo + " =====")

        print("\n--- EMPRÉSTIMOS ---")
        if self._emprestimos.is_empty():
            print("nenhum empréstimo registrado.")
        else:
            for emp in self._emprestimos._data:
                texto = "• " + emp["usuario"] + " — emprestado em " + emp["dataEmprestimo"].strftime("%d/%m/%Y %H:%M")
                if emp["dataDevolucao"]:
                    texto += " | devolvido em " + emp["dataDevolucao"].strftime("%d/%m/%Y %H:%M")
                else:
                    texto += " | em aberto"
                print(texto)

        print("\n--- RESERVAS ---")
        if self._reservas.is_empty():
            print("nenhuma reserva registrada.")
        else:
            for res in self._reservas._data:
                texto = "• " + res["usuario"] + " — reservou em " + res["dataReserva"].strftime("%d/%m/%Y %H:%M")
                if res["notificadoEm"]:
                    texto += " | notificado em " + res["notificadoEm"].strftime("%d/%m/%Y %H:%M")
                    texto += " (expira " + res["expiraEm"].strftime("%d/%m %H:%M") + ")"
                print(texto)
