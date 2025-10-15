from TAD.duplamente import DoublyLinkedListIterator



class Catalogo:

    def __init__(self):
        # cria uma lista duplamente encadeada vazia - privada
        self._listaCatalogo = DoublyLinkedListIterator()

    def padronizando(self, texto):
        # deixa o texto todo em minúsculas e sem espaços extras
        # Exemplo => exemplo ; e Xem PLO => exemplo
        return str(texto).strip().lower()

    def adicionarLivro(self, livro):
        '''
        diciona um novo livro se ainda não existir no catálogo.
        compara os títulos sem diferenciar maiúsculas ou minúsculas.
        '''
        tituloFormatado = self.padronizando(livro.titulo)