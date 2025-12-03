class Endereco:
    def __init__(self, cod_endereco, logradouro, num, cep, bairro, cidade, estado):
        self.cod_endereco = cod_endereco
        self.logradouro = logradouro
        self.num = num
        self.cep = cep
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado

    @property
    def cod_endereco(self):
        return self.cod_endereco
    
    @property
    def logradouro(self):
        return self.logradouro

    @logradouro.setter
    def logradouro(self, logradouroNew):
        if not logradouroNew or not isinstance(logradouroNew, str):
            raise ValueError("O nome do Logradouro não pode ser vazio ou nulo")
        self.__logradouro = logradouroNew

    @property
    def num(self):
        return self.num

    @num.setter
    def num(self, numNew):
        if not numNew or not isinstance(numNew, int):
            raise ValueError("Num não pode ser vazio ou nulo")
        self.__num = numNew

    @property
    def cep(self):
        return self.cep

    @cep.setter
    def cep(self, cepNew):
        if not cepNew or not isinstance(cepNew, str):
            raise ValueError("Cep não pode ser vazio ou nulo")
        self.__cep = cepNew

    @property
    def bairro(self):
        return self.bairro

    @bairro.setter
    def bairro(self, bairroNew):
        if not bairroNew or not isinstance(bairroNew, int):
            raise ValueError("bairro não pode ser vazio ou nulo")
        self.__bairro = bairroNew

    @property
    def cidade(self):
        return self.cidade

    @cidade.setter
    def cidade(self, cidadeNew):
        if not cidadeNew or not isinstance(cidadeNew, int):
            raise ValueError("cidade não pode ser vazio ou nulo")
        self.__cidade = cidadeNew

    @property
    def estado(self):
        return self.estado

    @estado.setter
    def estado(self, estadoNew):
        if not estadoNew or not isinstance(estadoNew, int):
            raise ValueError("estado não pode ser vazio ou nulo")
        self.__estado = estadoNew