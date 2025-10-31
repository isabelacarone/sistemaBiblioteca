from datetime import datetime, timedelta
from TADs.ArrayQueue import ArrayQueue
from TADs.ArrayStack import ArrayStack


class Historico:
    """
    Controla o histórico de empréstimos e reservas de um livro.
    Refatoração: Métodos agora retornam mensagens e expõem dados de forma controlada.
    """

    def __init__(self, livro):
        self._livro = livro
        self._emprestimos = ArrayStack()
        self._reservas = ArrayQueue()

    def get_reservas(self):
        """
        Retorna uma lista dos registros de reserva para visualização.
        Isso evita que o código externo acesse a fila '_reservas' diretamente.

        :return: Uma lista de dicionários, cada um representando uma reserva.
        """
        # A iteração sobre a fila já retorna os itens de forma segura.
        return list(self._reservas)

    def has_reservas(self):
        """
        Verifica se há alguma reserva na fila de espera.

        :return: True se houver reservas, False caso contrário.
        """
        return not self._reservas.is_empty()

    def _notificar_proximo_reserva(self):
        """
        Notifica o primeiro usuário da fila de reservas.
        Retorna a mensagem de notificação para ser usada externamente.
        """
        if self._reservas.is_empty():
            return ""  # Retorna string vazia se não houver ninguém para notificar.

        reserva = self._reservas.dequeue()
        reserva["notificadoEm"] = datetime.now()
        reserva["expiraEm"] = reserva["notificadoEm"] + timedelta(hours=24)

        return (
            f"Notificação: Usuário {reserva['usuario']} foi notificado. "
            f"A reserva para empréstimo é válida até {reserva['expiraEm'].strftime('%d/%m/%Y %H:%M')}."
        )

    def registrar_emprestimo(self, usuario):
        """
        Registra um novo empréstimo e retorna uma mensagem de sucesso.
        """
        registro = {
            "usuario": usuario.nome,
            "dataEmprestimo": datetime.now(),
            "dataDevolucao": None
        }
        self._emprestimos.push(registro)
        return f"Empréstimo de '{self._livro.titulo}' para {usuario.nome} registrado com sucesso."

    def registrar_devolucao(self, usuario):
        """
        Registra uma devolução, notifica o próximo da fila e retorna mensagens de status.
        """
        temp_stack = ArrayStack()
        devolvido = False
        mensagem_notificacao = ""

        while not self._emprestimos.is_empty():
            emp = self._emprestimos.pop()
            if emp["usuario"] == usuario.nome and emp["dataDevolucao"] is None and not devolvido:
                emp["dataDevolucao"] = datetime.now()
                devolvido = True
                mensagem_notificacao = self._notificar_proximo_reserva()
            temp_stack.push(emp)

        while not temp_stack.is_empty():
            self._emprestimos.push(temp_stack.pop())

        if devolvido:
            mensagem_principal = f"Devolução registrada para {usuario.nome}."
            return f"{mensagem_principal}\n{mensagem_notificacao}".strip()
        else:
            return f"Nenhum empréstimo em aberto encontrado para {usuario.nome}."

    def registrar_reserva(self, usuario):
        """
        Registra uma nova reserva e retorna uma mensagem de sucesso.
        """
        reserva = {
            "usuario": usuario.nome,
            "dataReserva": datetime.now(),
            "notificadoEm": None,
            "expiraEm": None
        }
        self._reservas.enqueue(reserva)
        return f"Reserva para '{self._livro.titulo}' registrada para {usuario.nome}. Você foi adicionado à fila de espera."