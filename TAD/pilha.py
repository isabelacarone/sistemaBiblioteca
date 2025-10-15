class ArrayStack:
    """
    classe que implementa uma Pilha (Stack) usando uma lista.
    a pilha segue a regra LIFO (Last In, First Out).
    """
    def __init__(self):
        self._data = []  

    def __len__(self):
        """
        Retorna o número de elementos na pilha.
        """
        return len(self._data)

    def is_empty(self):
        """
        Retorna True se a pilha estiver vazia, senão False.
        """
        return len(self._data) == 0


    def push(self, e):
        """
        Adiciona o elemento 'e' no topo da pilha.
        """
        self._data.append(e)

    def top(self):
        """
        Retorna o elemento do topo da pilha, sem removê-lo.
        Se a pilha estiver vazia, gera erro.
        """
        if self.is_empty():
            raise Exception("Pilha vazia")
        return self._data[-1]

    def pop(self):
        """
        Remove e retorna o elemento do topo da pilha.
        Se a pilha estiver vazia, gera erro.
        """
        if self.is_empty():
            raise Exception("Pilha vazia")
        return self._data.pop()
