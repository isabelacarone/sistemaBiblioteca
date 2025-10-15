from TAD.duplamente import DoublyLinkedListIterator

'''
controla os livros do catalogo, usa uma lista duplamente encadeada para armazenar, buscar e remover livros...



self._listaCatalogo => armazena a lista dup onde ficam os livros
padronizando() => muda textos p/ minúsculos e sem espaço buscando evitar duplicações
adicionarLivros() => adiciona liivro no catalogo SE ele não existir
buscarPorTitulo() => busca pelo nome
buscarPorAutor => busca todos os livros de tal autor
buscarPorEditora => busca todos os livros da tal editora
buscarPorAno() => buscar todos os livrvos em tal ano
listarTodos() => mostra todos os livros cadastrados
removerLivro() => apaga um livro do catalogo

'''
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

        # percorre a lista pra ver se o título já existe
        atual = self._listaCatalogo.firstNode
        while atual is not None:
            # compara o título formatado pra evitar duplicação
            if self.padronizando(atual.data.titulo) == tituloFormatado:
                print(f" livro '{livro.titulo}' já tá cadastrado")
                return
            atual = atual.nextNode

        # se a lista estiver vazia, adiciona no início
        if self._listaCatalogo.size == 0:
            self._listaCatalogo.insNode(livro)
        # senão, adiciona no fim
        else:
            self._listaCatalogo.last_Node()
            self._listaCatalogo.addNode(livro)

        print(f"livro '{livro.titulo}' foi adicionado")

    def buscarPorTitulo(self, titulo):
        '''
        busca um livro pelo título (ignora letras maiúsculas/minúsculas)
        retorna o livro se encontrar senão retorna None
        '''
        tituloFormatado = self.padronizando(titulo)
        atual = self._listaCatalogo.firstNode
        while atual is not None:
            if self.padronizando(atual.data.titulo) == tituloFormatado:
                return atual.data
            atual = atual.nextNode
        return None

    def buscarPorAutor(self, autor):
        '''
        busca livros pelo nome do autor
        retorna uma lista com todos os válid
        '''
        autorFormatado = self.padronizando(autor)
        resultados = []
        atual = self._listaCatalogo.firstNode
        while atual is not None:
            if autorFormatado in self.padronizando(atual.data.autor):
                resultados.append(atual.data)
            atual = atual.nextNode
        return resultados

    def buscarPorEditora(self, editora):
        '''
        busca livros pelo nome da editora
        retorna uma lista com todos os válid
        '''
        editoraFormatada = self.padronizando(editora)
        resultados = []
        atual = self._listaCatalogo.firstNode
        while atual is not None:
            if editoraFormatada in self.padronizando(atual.data.editora):
                resultados.append(atual.data)
            atual = atual.nextNode
        return resultados

    def buscarPorAno(self, ano):
        '''
        busca livros publicados no ano xxxx
        '''
        resultados = []
        atual = self._listaCatalogo.firstNode
        while atual is not None:
            if atual.data.ano == int(ano):  # compara com número inteiro!!!!!!!
                resultados.append(atual.data)
            atual = atual.nextNode
        return resultados

    def listarTodos(self):
        '''
        mostra todos os livros cadastrados no catálogo
        '''
        atual = self._listaCatalogo.firstNode
        if atual is None:
            print("nenhum livro cadastrado")
            return
        while atual is not None:
            # mostra as informações do livro no formato definido
            print(atual.data.__tudoJunto__())
            atual = atual.nextNode

    def removerLivro(self, titulo):
        '''
        remove um livro do catálogo (sem diferenciar letras maiúsculas/minúsculas)
        '''
        tituloFormatado = self.padronizando(titulo)
        atual = self._listaCatalogo.firstNode
        while atual is not None:
            if self.padronizando(atual.data.titulo) == tituloFormatado:
                # posiciona o iterador no livro e remove o nó
                self._listaCatalogo.iterator = atual
                self._listaCatalogo.elimNode()
                print(f"o livro '{titulo}' foi removido")
                return
            atual = atual.nextNode
        print(f"livro '{titulo}' não foi encontrado")

    def __len__(self):
        '''
        retorna o número total de livros cadastrados
        '''
        return self._listaCatalogo.size
