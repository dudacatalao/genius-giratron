class Player():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.points = 0

        #getters
        @property
        def get_nome(self):
            return self.nome

        @property
        def get_idade(self):
            return self.idade

        @property
        def get_points(self):
            return self.points
