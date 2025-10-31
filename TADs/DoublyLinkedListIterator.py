from TADs.ListNode import ListNode

class DoublyLinkedListIterator:
    """
    Classe que implementa uma Lista Duplamente Encadeada com um iterador.

    Esta estrutura gerencia uma coleção de nós, permitindo a navegação
    bidirecional (para frente e para trás). Ela mantém referências para o
    primeiro nó, o último nó, e um iterador que aponta para um nó específico.
    """

    def __init__(self, first_node=None):
        """
        Construtor da classe DoublyLinkedListIterator.

        :param first_node: O nó inicial da lista (opcional, padrão: None).
        """
        # Ponteiro que referencia o primeiro nó da lista.
        self.first_node = first_node
        # Ponteiro que referencia o último nó da lista.
        self.last_node = first_node
        # Ponteiro especial (iterador) que aponta para um nó atual.
        self.iterator = first_node
        # Armazena o número total de nós (elementos) na lista.
        self.size = 0

    def add_node(self, data):
        """
        Adiciona um novo nó com o dado fornecido DEPOIS da posição atual do iterador.
        Após a inserção, o iterador passa a apontar para o nó recém-criado.

        :param data: O dado a ser armazenado no novo nó.
        """
        # Cria uma nova instância de ListNode com o dado informado.
        new_node = ListNode(data)
        # Incrementa o contador de tamanho da lista.
        self.size += 1

        # Caso 1: A lista está vazia.
        if self.first_node is None:
            # O novo nó se torna tanto o primeiro quanto o último.
            self.first_node = new_node
            self.last_node = new_node
        # Caso 2: O iterador está no final da lista ou indefinido.
        elif self.iterator is None or self.iterator == self.last_node:
            # O nó anterior do novo nó aponta para o antigo último nó.
            new_node.ant_node = self.last_node
            # O próximo nó do antigo último nó aponta para o novo nó.
            self.last_node.next_node = new_node
            # Atualiza o ponteiro do último nó para ser o novo nó.
            self.last_node = new_node
        # Caso 3: O iterador está em uma posição intermediária.
        else:
            # O próximo nó do novo nó aponta para o nó que estava após o iterador.
            new_node.next_node = self.iterator.next_node
            # O nó anterior do novo nó aponta para a posição do iterador.
            new_node.ant_node = self.iterator
            # O nó anterior do antigo próximo nó agora aponta para o novo nó.
            self.iterator.next_node.ant_node = new_node
            # O próximo nó do iterador agora aponta para o novo nó.
            self.iterator.next_node = new_node

        # Atualiza o iterador para apontar para o nó recém-adicionado.
        self.iterator = new_node

    def ins_node(self, data):
        """
        Insere um novo nó com o dado fornecido ANTES da posição atual do iterador.
        Após a inserção, o iterador passa a apontar para o nó recém-criado.

        :param data: O dado a ser armazenado no novo nó.
        """
        # Cria uma nova instância de ListNode com o dado informado.
        new_node = ListNode(data)
        # Incrementa o contador de tamanho da lista.
        self.size += 1

        # Caso 1: A lista está vazia.
        if self.first_node is None:
            # O novo nó se torna tanto o primeiro quanto o último.
            self.first_node = new_node
            self.last_node = new_node
        # Caso 2: O iterador está no início da lista ou indefinido.
        elif self.iterator is None or self.iterator == self.first_node:
            # O próximo nó do novo nó aponta para o antigo primeiro nó.
            new_node.next_node = self.first_node
            # O nó anterior do antigo primeiro nó agora aponta para o novo nó.
            self.first_node.ant_node = new_node
            # Atualiza o ponteiro do primeiro nó para ser o novo nó.
            self.first_node = new_node
        # Caso 3: O iterador está em uma posição intermediária.
        else:
            # O próximo nó do novo nó aponta para a posição atual do iterador.
            new_node.next_node = self.iterator
            # O nó anterior do novo nó aponta para o nó que estava antes do iterador.
            new_node.ant_node = self.iterator.ant_node
            # O próximo nó do nó anterior ao iterador agora aponta para o novo nó.
            self.iterator.ant_node.next_node = new_node
            # O nó anterior do iterador agora aponta para o novo nó.
            self.iterator.ant_node = new_node

        # Atualiza o iterador para apontar para o nó recém-inserido.
        self.iterator = new_node

    def elim_node(self):
        """
        Elimina o nó onde o iterador está posicionado atualmente.
        Após a remoção, o iterador avança para o próximo nó da lista.

        :raises ValueError: Se o iterador for None (indefinido).
        """
        # Verifica se o iterador está posicionado sobre um nó válido.
        if self.iterator is None:
            # Lança uma exceção se não houver nó para eliminar.
            raise ValueError("Iterador indefinido.")

        # Guarda a referência do nó a ser deletado.
        delete_node = self.iterator
        # Decrementa o contador de tamanho da lista.
        self.size -= 1

        # Caso 1: O nó a ser removido é o único na lista.
        if delete_node == self.first_node and delete_node == self.last_node:
            # A lista se torna vazia.
            self.first_node = None
            self.last_node = None
            self.iterator = None
        # Caso 2: O nó a ser removido é o primeiro da lista.
        elif delete_node == self.first_node:
            # O segundo nó se torna o novo primeiro nó.
            self.first_node = delete_node.next_node
            # O ponteiro anterior do novo primeiro nó é definido como None.
            self.first_node.ant_node = None
            # O iterador avança para o novo primeiro nó.
            self.iterator = self.first_node
        # Caso 3: O nó a ser removido é o último da lista.
        elif delete_node == self.last_node:
            # O penúltimo nó se torna o novo último nó.
            self.last_node = delete_node.ant_node
            # O ponteiro próximo do novo último nó é definido como None.
            self.last_node.next_node = None
            # O iterador se move para o novo último nó.
            self.iterator = self.last_node
        # Caso 4: O nó a ser removido está em uma posição intermediária.
        else:
            # O nó anterior ao deletado aponta para o nó seguinte ao deletado.
            delete_node.ant_node.next_node = delete_node.next_node
            # O nó seguinte ao deletado aponta para o nó anterior ao deletado.
            delete_node.next_node.ant_node = delete_node.ant_node
            # O iterador avança para o próximo nó.
            self.iterator = delete_node.next_node

    def iterator_first_node(self):
        """
        Posiciona o iterador no primeiro nó da lista.
        """
        # O iterador passa a apontar para o mesmo nó que o 'first_node'.
        self.iterator = self.first_node

    def iterator_last_node(self):
        """
        Posiciona o iterador no último nó da lista.
        """
        # O iterador passa a apontar para o mesmo nó que o 'last_node'.
        self.iterator = self.last_node

    def iterator_next_node(self):
        """
        Avança o iterador uma posição para frente (para o próximo nó).
        Se o iterador já estiver no último nó, ele se torna None.
        """
        # Verifica se o iterador não é None.
        if self.iterator is not None:
            # Move o iterador para o próximo nó.
            self.iterator = self.iterator.next_node
        else:
            # Se já for None, mantém-se None.
            self.iterator = None

    def iterator_ant_node(self):
        """
        Retrocede o iterador uma posição para trás (para o nó anterior).
        Se o iterador já estiver no primeiro nó, ele se torna None.
        """
        # Verifica se o iterador não é None.
        if self.iterator is not None:
            # Move o iterador para o nó anterior.
            self.iterator = self.iterator.ant_node
        else:
            # Se já for None, mantém-se None.
            self.iterator = None

    def iterator_position_node(self, position):
        """
        Posiciona o iterador em um nó específico com base em sua posição (base 1).
        Se a posição for inválida (fora do intervalo [1, size]), o iterador se torna None.

        :param position: A posição (base 1) para onde o iterador deve ser movido.
        """
        # Verifica se a posição solicitada está dentro dos limites válidos da lista.
        if 1 <= position <= self.size:
            # Começa a busca a partir do primeiro nó.
            self.iterator = self.first_node
            # Loop para avançar o iterador até a posição desejada.
            for _ in range(position - 1):
                # Move o iterador para o próximo nó.
                self.iterator = self.iterator.next_node
        else:
            # Se a posição for inválida, define o iterador como None.
            self.iterator = None

    def undefined_iterator(self):
        """
        Verifica se o iterador está indefinido (não está posicionado em nenhum nó).

        :return: True se o iterador for None, False caso contrário.
        """
        # Retorna o resultado da comparação booleana.
        return self.iterator is None