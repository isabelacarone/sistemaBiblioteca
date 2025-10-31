class ArrayQueue:
    """
    Implementa uma FILA (estrutura FIFO — First In, First Out)
    usando um vetor circular (array de tamanho fixo que pode ser redimensionado).
    """
    # Capacidade inicial padrão do array interno.
    default_capacity = 10

    def __init__(self):
        """
        Construtor. Cria e retorna uma fila vazia com capacidade padrão.
        """
        # Cria uma lista Python com 'None' para armazenar os elementos da fila.
        self._data = [None] * ArrayQueue.default_capacity
        # Armazena a quantidade de elementos atualmente na fila.
        self._size = 0
        # Guarda o índice do primeiro elemento (a "frente" da fila).
        self._front = 0

    def __len__(self):
        """
        Retorna o número de elementos atualmente na fila.

        :return: O número de elementos na fila.
        """
        # Retorna o valor do contador de tamanho.
        return self._size

    def is_empty(self):
        """
        Retorna True se a fila estiver vazia (sem elementos), senão False.

        :return: Booleano indicando se a fila está vazia.
        """
        # A fila está vazia se o seu tamanho for zero.
        return self._size == 0

    def _resize(self, cap):
        """
        Redimensiona o array interno para uma nova capacidade 'cap'.
        Este é um método privado, usado internamente quando a fila enche.

        :param cap: A nova capacidade desejada para o array.
        """
        # Guarda a referência para o array antigo.
        old = self._data
        # Cria um novo array com a nova capacidade.
        self._data = [None] * cap
        # Inicia um ponteiro 'walk' na posição do primeiro elemento do array antigo.
        walk = self._front

        # Itera sobre os elementos da fila para copiá-los para o novo array.
        for k in range(self._size):
            # Copia o elemento do array antigo para o novo.
            self._data[k] = old[walk]
            # Move o ponteiro 'walk' de forma circular no array antigo.
            walk = (walk + 1) % len(old)

        # Após a cópia, o primeiro elemento da fila está no índice 0 do novo array.
        self._front = 0

    def enqueue(self, e):
        """
        Adiciona um novo elemento 'e' ao final da fila.
        Caso o array esteja cheio, sua capacidade é dobrada automaticamente.

        :param e: O elemento a ser adicionado na fila.
        """
        # Verifica se o número de elementos é igual à capacidade do array.
        if self._size == len(self._data):
            # Se estiver cheio, dobra a capacidade do array.
            self._resize(2 * len(self._data))

        # Calcula a posição disponível para inserção usando aritmética modular.
        avail = (self._front + self._size) % len(self._data)
        # Insere o novo elemento na posição calculada.
        self._data[avail] = e
        # Incrementa o contador de tamanho da fila.
        self._size += 1

    def dequeue(self):
        """
        Remove e retorna o elemento que está na frente da fila.

        :raises Exception: Se a fila estiver vazia.
        :return: O primeiro elemento da fila.
        """
        # Verifica se a fila está vazia antes de tentar remover.
        if self.is_empty():
            # Lança uma exceção se não houver elementos para remover.
            raise Exception("Fila vazia — não é possível remover elementos.")

        # Guarda o elemento da frente para retorná-lo.
        ans = self._data[self._front]
        # Define a posição antiga como None para liberar a referência (boa prática).
        self._data[self._front] = None
        # Atualiza o índice do primeiro elemento, movendo-o circularmente.
        self._front = (self._front + 1) % len(self._data)
        # Reduz o contador de elementos.
        self._size -= 1
        # Retorna o elemento que foi removido.
        return ans

    def first(self):
        """
        Retorna o elemento que está na frente da fila, sem o remover.

        :raises Exception: Se a fila estiver vazia.
        :return: O primeiro elemento da fila.
        """
        # Verifica se a fila está vazia.
        if self.is_empty():
            # Lança uma exceção se não houver primeiro elemento.
            raise Exception("Fila vazia — não há primeiro elemento.")

        # Retorna o elemento localizado no índice '_front'.
        return self._data[self._front]

    def __iter__(self):
        """
        Permite a iteração sobre os itens da fila, do primeiro ao último.
        """
        # Inicia a travessia a partir do índice do primeiro elemento.
        walk = self._front
        # Itera exatamente o número de vezes correspondente ao tamanho da fila.
        for _ in range(self._size):
            # Retorna o elemento na posição atual do 'walk'.
            yield self._data[walk]
            # Move o 'walk' para a próxima posição de forma circular.
            walk = (1 + walk) % len(self._data)