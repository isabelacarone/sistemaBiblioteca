class Usuario:
    def __init__(self, nome, email=None):
        self.nome = nome
        self.email = email
        
    def __str__(self): 
        if self.email is not None and self.email != "":
            return "usuario: " + self.nome + " <" + self.email + ">"
        else:
            return "usuario: " + self.nome