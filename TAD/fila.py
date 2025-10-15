from TAD.node import ListNode

class ArrayQueue:
    """
        implementa uma FILA (estrutura FIFO — First In, First Out)
        usando um vetor circular (array de tamanho fixo que pode ser redimensionado)
    """

    default_capacity = 10

    def __init__(self):
        """
        Inicializa a fila com capacidade padrão
        """
        self._data = [None] * ArrayQueue.default_capacity  # lista que armazenará os elementos
        self._size = 0                                     # quantidade de elementos na fila
        self._front = 0                                    # índice do primeiro elemento


    def __len__(self):
        """
        retorna o número de elementos atualmente na fila
        """
        return self._size

    def is_empty(self):
        """
        retorna True se a fila estiver vazia (sem elementos)
        """
        return self._size == 0


    def enqueue(self, e):
        """
        adiciona um novo elemento ao final da fila
        caso o vetor esteja cheio, a capacidade é dobrada automaticamente
        """
        # Verifica se a fila está cheia
        if self._size == len(self._data):
            self._resize(2 * len(self._data))  # dobra o tamanho do array

        # Calcula a posição disponível (circular)
        avail = (self._front + self._size) % len(self._data)

        # Insere o novo elemento na posição calculada
        self._data[avail] = e

        # Incrementa o tamanho da fila
        self._size += 1


    def dequeue(self):
        """
        rmove e retorna o elemento que está na frente da fila
        se a fila estiver vazia, lança uma exceção
        """
        if self.is_empty():
            raise Exception("Fila vazia — não é possível remover elementos.")

        # Pega o elemento que está na frente
        ans = self._data[self._front]

        # Libera a posição antiga (boa prática)
        self._data[self._front] = None

        # Atualiza o índice do primeiro elemento (movendo circularmente)
        self._front = (self._front + 1) % len(self._data)

        # Reduz a contagem de elementos
        self._size -= 1

        # Retorna o elemento removido
        return ans


    def first(self):
        """
        retorna o elemento que está na frente da fila ((sem removê-lo
        se a fila estiver vazia, lança uma exceção
        """
        if self.is_empty():
            raise Exception("Fila vazia — não há primeiro elemento.")

        # Retorna o elemento que está na frente (posição _front)
        return self._data[self._front]



    def _resize(self, cap):
        """
        Aumenta a capacidade da fila para 'cap' posições.
        Copia os elementos na ordem correta (começando do _front).
        """
        old = self._data                 # armazena o array atual
        self._data = [None] * cap        # cria um novo array maior
        walk = self._front               # começa do primeiro elemento

        # Copia os elementos antigos para o novo array na ordem correta
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)  # anda de forma circular

        # Após copiar, redefine o início (_front)
        self._front = 0
