from livro import Livro
from catalogo import Catalogo
from interface import menu_cli
def carregar_demo():
    cat=Catalogo()
    base=[
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
    for t,a,ano,ed,q in base: cat.adicionarLivro(Livro(t,a,ano,ed,q))

    return cat
if __name__=="__main__":
    print("Inicializando sistema de biblioteca...")
    cat=carregar_demo()
    l = cat.buscarPorTitulo("Clean Code")

    if l:
        from app.usuario import Usuario
        print(l.emprestar(Usuario("Alice"))); print(l.emprestar(Usuario("Bruno"))); print(l.emprestar(Usuario("Carla")))
        print(l.devolver(Usuario("Alice")))
    menu_cli(cat)
