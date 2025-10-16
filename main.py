# main.py

from catalogo import Catalogo
import catalogo as catalogo_mod

from livro import Livro
import livro as livro_mod

from usuario import Usuario
from interface import interface


def carregarDemo(cat: Catalogo):
    base = [
        ("Estruturas de Dados em Python","Niklaus Wirth",2020,"TechBooks",3),
        ("Algoritmos: Teoria e Prática","Thomas H. Cormen",2013,"Elsevier",2),
        ("Banco de Dados","Ramez Elmasri",2011,"Pearson",4),
        ("Inteligência Artificial","Stuart Russell",2021,"Pearson",2),
        ("Engenharia de Software","Roger Pressman",2017,"AMGH",3),
        ("Clean Code","Robert C. Martin",2008,"Prentice Hall",2),
        ("Padrões de Projeto","Erich Gamma et al.",1994,"Addison-Wesley",2),
        ("Sistemas Operacionais","Abraham Silberschatz",2018,"Wiley",2),
        ("Arquitetura de Computadores","John L. Hennessy",2017,"Morgan Kaufmann",2),
        ("Redes de Computadores","Andrew S. Tanenbaum",2019,"Pearson",3),
    ]
    for t, a, ano, ed, q in base:
        cat.adicionarLivro(Livro(t, a, ano, ed, q))

    # adiciona o livro "Sociedade do Cansaço" sem exemplares disponíveis
    # para que a tentativa de empréstimo coloque o usuário direto na fila
    livro_han = Livro("Sociedade do Cansaço", "Byung-Chul Han", 2010, "Vozes", 0)
    cat.adicionarLivro(livro_han)

    # coloca Guilherme na fila de espera desse livro
    guilherme = Usuario("Guilherme")
    livro_han.emprestar(guilherme)  # sem cópias -> entra na fila


if __name__ == "__main__":
    # cria catálogo e carrega base + livro solicitado
    cat = Catalogo()
    carregarDemo(cat)

    # expõe nomes como seu interface.py espera:
    #   from catalogo import catalogo
    #   from livro import livro
    catalogo_mod.catalogo = cat
    livro_mod.livro = Livro

    # mostra a notificação ao abrir o sistema
    print("notificação: Guilherme está na lista de espera para 'Sociedade do Cansaço'.")

    # inicia a interface
    interface()
