class Feira:
    def __init__(self, cod_feira,nome_feira):
        self.cod_feira = cod_feira
        self.nome_feira = nome_feira 
 
    @property
    def cod_feira(self):
       return self.__cod_feira

    @property
    def nome_feira(self):
       return self.__nome_feira
    
    @nome_feira.setter
    def nome_feira(self, nome_feiraNew):
       if not nome_feiraNew or not isinstance(nome_feiraNew, str):
            raise ValueError("O nome da Feira não pode ser vazio ou nulo")
       self.__nome_feira = nome_feiraNew

