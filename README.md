# Sistema de Gerenciamento de Biblioteca

## Contexto Acadêmico
Este projeto foi desenvolvido como parte da disciplina **Estrutura de Dados I**, ministrada pelo **Professor Saulo**, no curso de **Sistemas de Informação** da **Universidade Vila Velha (UVV)**.  
O objetivo é aplicar conceitos de **Listas Duplamente Encadeadas**, **Pilhas** e **Filas** em um sistema funcional de gerenciamento de biblioteca, utilizando **Python** e **Programação Orientada a Objetos (POO)**.

---

## Descrição Geral
O **Sistema de Gerenciamento de Biblioteca** permite gerenciar o catálogo de livros, empréstimos, devoluções e reservas de forma estruturada e eficiente.  
O sistema foi projetado para demonstrar o uso prático das estruturas de dados clássicas em um contexto real, com interação via **linha de comando (CLI)**.

O programa realiza:
- Cadastro e listagem de livros;
- Busca de livros por título, autor, editora ou ano;
- Registro de empréstimos e devoluções;
- Controle de fila de espera (reservas);
- Registro histórico de todas as operações realizadas.

---

## Estruturas de Dados Utilizadas

### Lista Duplamente Encadeada
- Gerencia o **catálogo de livros**.  
- Cada nó contém informações sobre um livro.  
- Permite inserção, remoção e busca em ambas as direções.

### Pilha (ArrayStack)
- Controla o **histórico de atividades** de cada livro (empréstimos e devoluções).  
- Mantém as operações em ordem cronológica, com acesso rápido à última ação.

### Fila (ArrayQueue)
- Gerencia a **fila de reservas** de usuários para livros indisponíveis.  
- Quando um exemplar é devolvido, o primeiro usuário da fila é notificado e tem 24 horas de prioridade para realizar o empréstimo.

---

## Estrutura do Projeto
```
sistemaBiblioteca/
├── TAD/
│ ├── fila.py # Implementação da fila (ArrayQueue)
│ └── pilha.py # Implementação da pilha (ArrayStack)
├── catalogo.py # Catálogo de livros (lista duplamente encadeada)
├── historico.py # Controle de empréstimos, devoluções e reservas
├── interface.py # Interface de linha de comando (CLI)
├── livro.py # Classe Livro e métodos principais
├── usuario.py # Classe Usuário
├── main.py # Ponto de entrada do sistema
└── README.md # Documentação do projeto
```


---

## Requisitos do Trabalho
Conforme as orientações da disciplina **Estrutura de Dados I**, o projeto atende aos seguintes requisitos:

1. **Implementação das Estruturas de Dados**
   - Lista Duplamente Encadeada para o catálogo de livros;
   - Pilha para o histórico de empréstimos e devoluções;
   - Fila para o controle de reservas.

2. **Documentação do Código**
   - Todas as funções possuem comentários explicativos sobre seu funcionamento, parâmetros e retornos.
   - O código é documentado linha a linha, conforme as exigências do trabalho.

3. **Organização Modular**
   - Cada classe foi implementada em um arquivo separado;
   - O arquivo principal (`main.py`) contém a função `__main__`, responsável por instanciar os objetos e executar o sistema.

4. **Interface de Usuário**
   - Interface simples e funcional, executada via terminal;
   - Permite realizar operações de busca, empréstimo, devolução e reserva de livros.

---

## Instruções de Execução

### Pré-requisitos
- Python 3.8 ou superior instalado.

### Passos para executar
1. Clonar o repositório:
   ```bash
   git clone https://github.com/isabelacarone/sistemaBiblioteca.git
   cd sistemaBiblioteca

2. Executar o programa:
   ```
   python main.py
   ```
3. Interagir com o menu:
   ```
   ===== MENU DA BIBLIOTECA =====
    1 - Buscar livro
    2 - Solicitar empréstimo
    3 - Devolver livro
    4 - Entrar na lista de espera
    0 - Sair
  

