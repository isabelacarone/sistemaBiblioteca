# main.py
# prepara o ambiente para a interface:
# - cria um objeto Catalogo e o expõe como "catalogo" dentro do módulo catalogo
# - cria um alias "livro" para a classe Livro dentro do módulo livro
# isso garante que os imports do seu interface.py funcionem:
#   from catalogo import catalogo
#   from livro import livro

from catalogo import Catalogo
import catalogo as catalogo_mod

from livro import Livro
import livro as livro_mod

from usuario import Usuario  # caso você use em testes locais

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

if __name__ == "__main__":
    # 1) cria o catálogo
    cat = Catalogo()

    # 2) coloca com dados de exemplo
    carregarDemo(cat)

    # 3) expoe nomes 
    #    - torna o objeto 'cat' acessível como 'catalogo' dentro do módulo catalogo
    #    - cria 'livro' como alias para a classe Livro, para o import "from livro import livro"
    catalogo_mod.catalogo = cat
    livro_mod.livro = Livro

    # 4) agora pode importar e chamar a interface normalmente
    from interface import interface
    interface()
