# -*- coding: utf-8 -*-

class Usuario:
    """
    Representa um usuário da biblioteca.
    """

    def __init__(self, nome, email=None):
        """
        Construtor da classe Usuario.

        :param nome: O nome do usuário (string).
        :param email: O e-mail do usuário (string, opcional).
        """
        # Atribui o nome do usuário.
        self.nome = nome
        # Atribui o e-mail do usuário.
        self.email = email

    def __str__(self):
        """
        Retorna uma representação em string do objeto Usuario.

        :return: Uma string formatada com as informações do usuário.
        """
        # Verifica se o e-mail foi fornecido e não está vazio.
        if self.email is not None and self.email != "":
            # Retorna o formato "usuario: Nome <email@exemplo.com>".
            return "usuario: " + self.nome + " <" + self.email + ">"
        else:
            # Retorna o formato "usuario: Nome".
            return "usuario: " + self.nome