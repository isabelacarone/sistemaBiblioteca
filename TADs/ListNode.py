class ListNode:
    """
    Representa um nó individual em uma lista duplamente encadeada.

    Cada nó contém um dado (data) e referências para o nó seguinte (next_node)
    e para o nó anterior (ant_node).
    """

    def __init__(self, data, next_node=None, ant_node=None):
        """
        Construtor da classe ListNode.

        :param data: O dado a ser armazenado no nó.
        :param next_node: A referência para o próximo nó na lista (padrão: None).
        :param ant_node: A referência para o nó anterior na lista (padrão: None).
        """
        # Armazena o dado ou conteúdo do nó.
        self.data = data
        # Armazena a referência (ponteiro) para o próximo nó da lista.
        self.next_node = next_node
        # Armazena a referência (ponteiro) para o nó anterior da lista.
        self.ant_node = ant_node