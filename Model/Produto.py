class Produto:
    def __init__(self, cod_produto, nome, tipo):
        self.cod_produto = cod_produto
        self.nome = nome
        self.tipo = tipo

    @property
    def cod_produto(self):
        return self.__cod_produto
    
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nomeNew):
        if not nomeNew or not isinstance(nomeNew, str):
            raise ValueError("Nome não pode ser vazio ou nulo")
        self.__nome = nomeNew

    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipoNew):
        if not tipoNew or not isinstance(tipoNew, str):
            raise ValueError("Tipo não pode ser vazio ou nulo")
        self.__tipo = tipoNew