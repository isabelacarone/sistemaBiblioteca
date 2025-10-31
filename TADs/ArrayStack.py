class ArrayStack:
    """
    Classe que implementa uma Pilha (Stack) usando uma lista simplesmente encadeada.
    A pilha segue a regra LIFO (Last In, First Out).

    Esta implementação cumpre o requisito do PDF de usar uma lista encadeada,
    embora o nome da classe seja 'ArrayStack' conforme especificado.
    """

    # --- Classe aninhada para o nó da lista encadeada ---
    class _Node:
        """
        Classe privada para representar um nó da lista encadeada.
        """
        def __init__(self, element, next_node):
            """
            Construtor do nó.
            :param element: O dado a ser armazenado no nó.
            :param next_node: A referência para o próximo nó.
            """
            # O dado armazenado neste nó.
            self._element = element
            # A referência para o próximo nó na lista.
            self._next = next_node

    # --- Métodos da classe ArrayStack ---
    def __init__(self):
        """
        Construtor. Cria e retorna uma pilha vazia.
        """
        # Ponteiro para o nó no topo da pilha (inicialmente None).
        self._head = None
        # Contador para o número de elementos na pilha.
        self._size = 0

    def __len__(self):
        """
        Retorna quantos elementos estão na pilha.

        :return: O número de elementos na pilha.
        """
        # Retorna o valor do contador de tamanho.
        return self._size

    def is_empty(self):
        """
        Retorna True se a pilha estiver vazia, senão False.

        :return: Booleano indicando se a pilha está vazia.
        """
        # A pilha está vazia se o tamanho for igual a zero.
        return self._size == 0

    def push(self, e):
        """
        Adiciona o elemento 'e' no topo da pilha.

        :param e: O elemento a ser adicionado.
        """
        # O novo nó aponta para o antigo topo (self._head).
        # self._head é então atualizado para ser o novo nó.
        self._head = self._Node(e, self._head)
        # Incrementa o contador de tamanho.
        self._size += 1

    def top(self):
        """
        Retorna o elemento do topo da pilha, sem o remover.

        :raises Exception: Se a pilha estiver vazia.
        :return: O elemento do topo da pilha.
        """
        # Verifica se a pilha está vazia antes de tentar acessar o topo.
        if self.is_empty():
            # Lança uma exceção se a pilha estiver vazia.
            raise Exception("Pilha vazia")
        # Acesso interno: ArrayStack, como classe proprietária, pode acessar
        # com segurança os membros de sua classe auxiliar aninhada _Node.
        return self._head._element

    def pop(self):
        """
        Remove e retorna o elemento do topo da pilha.

        :raises Exception: Se a pilha estiver vazia.
        :return: O elemento removido do topo da pilha.
        """
        # Verifica se a pilha está vazia antes de tentar remover.
        if self.is_empty():
            # Lança uma exceção se a pilha estiver vazia.
            raise Exception("Pilha vazia")
        # Acesso interno: Guarda o elemento do topo para retorná-lo depois.
        answer = self._head._element
        # Acesso interno: Move o ponteiro do topo para o próximo nó da lista.
        self._head = self._head._next
        # Decrementa o contador de tamanho.
        self._size -= 1
        # Retorna o elemento que foi removido.
        return answer

    def __iter__(self):
        """
        Permite a iteração sobre os itens da pilha, do topo para a base.
        """
        # Inicia a travessia a partir do nó do topo.
        current = self._head
        # Continua enquanto houver nós na lista.
        while current:
            # Acesso interno: Retorna o elemento do nó atual.
            yield current._element
            # Acesso interno: Move para o próximo nó.
            current = current._next