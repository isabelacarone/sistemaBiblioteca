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
def padronizando(texto):
    return str(texto).strip().lower()

class Catalogo:
    """
    Controla o catálogo de livros da biblioteca.
    """
    def __init__(self):
        self._lista_catalogo = DoublyLinkedListIterator()

    def adicionar_livro(self, livro, silencioso=False):
        """
        Adiciona um novo livro ao catálogo.

        :param livro: O objeto Livro a ser adicionado.
        :param silencioso: Se True, não imprime a mensagem de confirmação.
        """
        titulo_formatado = padronizando(livro.titulo)
        atual = self._lista_catalogo.first_node
        while atual is not None:
            if padronizando(atual.data.titulo) == titulo_formatado:
                return  # Se o livro já existe, simplesmente retorna.
            atual = atual.next_node

        if self._lista_catalogo.size == 0:
            self._lista_catalogo.ins_node(livro)
        else:
            self._lista_catalogo.iterator_last_node()
            self._lista_catalogo.add_node(livro)

        if not silencioso:
            print(f"Livro '{livro.titulo}' foi adicionado ao catálogo.")

    def buscar_por_titulo(self, titulo):
        titulo_formatado = padronizando(titulo)
        atual = self._lista_catalogo.first_node
        while atual is not None:
            if padronizando(atual.data.titulo) == titulo_formatado:
                return atual.data
            atual = atual.next_node
        return None

    def buscar_por_autor(self, autor):
        autor_formatado = padronizando(autor)
        resultados = []
        atual = self._lista_catalogo.first_node
        while atual is not None:
            if autor_formatado in padronizando(atual.data.autor):
                resultados.append(atual.data)
            atual = atual.next_node
        return resultados

    def buscar_por_editora(self, editora):
        editora_formatada = padronizando(editora)
        resultados = []
        atual = self._lista_catalogo.first_node
        while atual is not None:
            if editora_formatada in padronizando(atual.data.editora):
                resultados.append(atual.data)
            atual = atual.next_node
        return resultados

    def __len__(self):
        return self._lista_catalogo.size