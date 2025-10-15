from TAD.node import ListNode
class DoublyLinkedListIterator:

    """
        classe representante de uma Lista Duplamente Encadeada com Iterador.
        Possui ponteiros para o primeiro nó, último nó e um iterador. it a coisa 
    """

    def __init__(self, firstNode=None):
        self.firstNode = firstNode  
        self.lastNode = firstNode    
        self.iterator = firstNode   
        self.size = 0                



    def addNode(self, data):
        """
        adiciona um novo nó DEPOIS da posição do iterador.
        o iterador passa a apontar para o nó recém-inserido.
        """
        newNode = ListNode(data)
        self.size += 1

        if self.firstNode is None:
          self.firstNode = newNode
          self.lastNode = newNode

        elif self.iterator is None or self.iterator == self.lastNode:
          newNode.antNode = self.lastNode
          self.lastNode.nextNode = newNode
          self.lastNode = newNode

        else:
          newNode.nextNode = self.iterator.nextNode
          newNode.antNode = self.iterator
          self.iterator.nextNode.antNode = newNode
          self.iterator.nextNode = newNode

        self.iterator = newNode

    def insNode(self, data):
        """
        insere um novo nó ANTES da posição do iterador.
        o iterador passa a apontar para o nó recém-inserido.
        """
        newNode = ListNode(data)
        self.size += 1

        if self.firstNode is None:
          self.firstNode = newNode
          self.lastNode = newNode

        elif self.iterator is None or self.iterator == self.firstNode:
          newNode.nextNode = self.firstNode
          self.firstNode.antNode = newNode
          self.firstNode = newNode

        else:
          newNode.nextNode = self.iterator
          newNode.antNode = self.iterator.antNode
          self.iterator.antNode.nextNode = newNode
          self.iterator.antNode = newNode

        self.iterator = newNode

    def elimNode(self):
        """
        elimina o nó onde o iterador está posicionado.
        após a remoção, o iterador avança para o próximo nó.
        """
        if self.iterator is None:
          raise ValueError("Iterador indefinido. Impossível eliminar nó.")

        deleteNode = self.iterator
        self.size -= 1

        if deleteNode == self.firstNode and deleteNode == self.lastNode:
          self.firstNode = None
          self.lastNode = None
          self.iterator = None

        elif deleteNode == self.firstNode:
          self.firstNode = deleteNode.nextNode
          self.firstNode.antNode = None
          self.iterator = self.firstNode

        elif deleteNode == self.lastNode:
          self.lastNode = deleteNode.antNode
          self.lastNode.nextNode = None
          self.iterator = self.lastNode

        else:
          deleteNode.antNode.nextNode = deleteNode.nextNode
          deleteNode.nextNode.antNode = deleteNode.antNode
          self.iterator = deleteNode.nextNode


    def first_Node(self):
        """
        coloca o iterador no primeiro nó da lista.
        """
        self.iterator = self.firstNode

    def last_Node(self):
        """
        coloca o iterador no último nó da lista.
        """
        self.iterator = self.lastNode

    def nextNode(self):
        """
        avança o iterador uma posição para frente.
        se já estiver no último nó, o iterador vira None.
        """
        if self.iterator is not None:
            self.iterator = self.iterator.nextNode
        else:
            self.iterator = None

    def antNode(self):
        """
        retrocede o iterador uma posição para trás.
        e já estiver no primeiro nó, o iterador vira None.
        """
        if self.iterator is not None:
            self.iterator = self.iterator.antNode
        else:
            self.iterator = None

    def posNode(self, position):
        """
        coloca o iterador em uma posição específica (1 <= pos <= size).
        caso a posição não seja válida, o iterador vira None.
        """
        if 1 <= position <= self.size:
            self.iterator = self.firstNode
            for _ in range(position - 1):
                self.iterator = self.iterator.nextNode
        else:
            self.iterator = None


    def undefinedIterator(self):
        """
        retorna True se o iterador não estiver posicionado em nenhum nó.
        """
        return self.iterator is None