from datetime import datetime, timedelta
from TAD.duplamente import DoublyLinkedListIterator

'''
controla o histórico de empréstimos e reservas de um livro, 
utilizando uma lista duplamente encadeada.

self._livro => referência para o livro ao qual o histórico pertence
self._emprestimos => lista duplamente encadeada com os registros de empréstimos
self._reservas => lista duplamente encadeada com os registros de reservas

registrarEmprestimo() => adiciona um novo empréstimo com data e hora atuais
registrarDevolucao() => encerra o empréstimo em aberto de um usuário e notifica a fila
registrarReserva() => adiciona um novo registro de reserva
_notificarProximoReserva() => envia notificação ao primeiro usuário da fila
reservaAtiva() => verifica se a reserva do usuário ainda está dentro do prazo de 24h
exibirHistorico() => mostra todas as operações de empréstimos e reservas do livro
'''
class Historico:

    def __init__(self, livro):
        # cria o histórico vinculado a um livro específico
        self._livro = livro
        self._emprestimos = DoublyLinkedListIterator()  # lista encadeada de empréstimos
        self._reservas = DoublyLinkedListIterator()     # lista encadeada de reservas

    # registra um novo empréstimo
    def registrarEmprestimo(self, usuario):
        # adiciona um novo registro com data atual e sem devolução ainda
        registro = {
            "usuario": usuario.nome,
            "dataEmprestimo": datetime.now(),
            "dataDevolucao": None
        }
        self._emprestimos.last_Node()   # posiciona o iterador no final
        self._emprestimos.addNode(registro)
        print("empréstimo de '" + self._livro.titulo + "' feito por " + usuario.nome + " registrado com sucesso.")

 
    # registra uma devolução
    def registrarDevolucao(self, usuario):
        # percorre a lista do fim para o início buscando empréstimo em aberto
        self._emprestimos.last_Node()
        while self._emprestimos.iterator is not None:
            emp = self._emprestimos.iterator.data
            if emp["usuario"] == usuario.nome and emp["dataDevolucao"] is None:
                emp["dataDevolucao"] = datetime.now()
                print("devolução registrada para " + usuario.nome + ".")
                self._notificarProximoReserva()
                return
            self._emprestimos.antNode()
        print("nenhum empréstimo aberto encontrado para " + usuario.nome + ".")

    # registra uma nova reserva
    def registrarReserva(self, usuario):
        # adiciona novo registro de reserva
        reserva = {
            "usuario": usuario.nome,
            "dataReserva": datetime.now(),
            "notificadoEm": None,
            "expiraEm": None
        }
        self._reservas.last_Node()
        self._reservas.addNode(reserva)
        print("reserva registrada para " + usuario.nome + ".")


    # notifica o próximo usuário da fila de reservas
    def _notificarProximoReserva(self):
        # percorre a lista e notifica o primeiro usuário ainda não notificado
        self._reservas.first_Node()
        while self._reservas.iterator is not None:
            reserva = self._reservas.iterator.data
            if reserva["notificadoEm"] is None:
                reserva["notificadoEm"] = datetime.now()
                reserva["expiraEm"] = reserva["notificadoEm"] + timedelta(hours=24)
                print("usuário " + reserva["usuario"] + " foi notificado. prioridade válida até " +
                      reserva["expiraEm"].strftime("%d/%m %H:%M") + ".")
                return
            self._reservas.nextNode()


    # verifica se a reserva de um usuário ainda é válida
    def reservaAtiva(self, nomeUsuario):
        self._reservas.first_Node()
        while self._reservas.iterator is not None:
            reserva = self._reservas.iterator.data
            if reserva["usuario"] == nomeUsuario and reserva["expiraEm"] is not None:
                return datetime.now() <= reserva["expiraEm"]
            self._reservas.nextNode()
        return False


    # exibe todas as operações de empréstimos e reservas - tipo o __tudoJunto__
    def exibirHistorico(self):
        print("\n===== HISTÓRICO DO LIVRO: " + self._livro.titulo + " =====")

        print("\n--- EMPRÉSTIMOS ---")
        self._emprestimos.first_Node()
        if self._emprestimos.iterator is None:
            print("nenhum empréstimo registrado.")
        else:
            while self._emprestimos.iterator is not None:
                emp = self._emprestimos.iterator.data
                texto = "• " + emp["usuario"] + " — emprestado em " + emp["dataEmprestimo"].strftime("%d/%m/%Y %H:%M")
                if emp["dataDevolucao"] is not None:
                    texto += " | devolvido em " + emp["dataDevolucao"].strftime("%d/%m/%Y %H:%M")
                else:
                    texto += " | em aberto"
                print(texto)
                self._emprestimos.nextNode()

        print("\n--- RESERVAS ---")
        self._reservas.first_Node()
        if self._reservas.iterator is None:
            print("nenhuma reserva registrada.")
        else:
            while self._reservas.iterator is not None:
                res = self._reservas.iterator.data
                texto = "• " + res["usuario"] + " — reservou em " + res["dataReserva"].strftime("%d/%m/%Y %H:%M")
                if res["notificadoEm"] is not None:
                    texto += " | notificado em " + res["notificadoEm"].strftime("%d/%m/%Y %H:%M")
                    texto += " (expira " + res["expiraEm"].strftime("%d/%m %H:%M") + ")"
                print(texto)
                self._reservas.nextNode()
