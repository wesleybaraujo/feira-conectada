class Usuario:
    def __init__(self, cod_usuario, nome, email, senha, num_documento):
        self.cod_usuario = cod_usuario
        self.nome = nome
        self.email = email
        self.senha = senha
        self.num_documento = num_documento

    @property
    def cod_usuario(self):
        return self.__cod_usuario

    @cod_usuario.setter
    def cod_usuario(self, codNew):
        if not codNew:
            raise ValueError("O código do usuário não pode ser vazio ou nulo")
        self.__cod_usuario = codNew

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nomeNew):
        if not nomeNew or not isinstance(nomeNew, str):
            raise ValueError("O nome não pode ser vazio ou nulo")
        self.__nome = nomeNew

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, emailNew):
        if not emailNew or not isinstance(emailNew, str):
            raise ValueError("O email não pode ser vazio ou nulo")
        self.__email = emailNew

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senhaNew):
        if not senhaNew or not isinstance(senhaNew, str):
            raise ValueError("A senha não pode ser vazia ou nula")
        self.__senha = senhaNew

    @property
    def num_documento(self):
        return self.__num_documento

    @num_documento.setter
    def num_documento(self, numDocNew):
        if not numDocNew or not isinstance(numDocNew, str):
            raise ValueError("O documento não pode ser vazio ou nulo")
        self.__num_documento = numDocNew
