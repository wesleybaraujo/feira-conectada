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
            raise ValueError("Código inválido.")
        self.__cod_usuario = codNew

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nomeNew):
        if not nomeNew or not isinstance(nomeNew, str):
            raise ValueError("Nome inválido.")
        self.__nome = nomeNew

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, emailNew):
        if not emailNew or not isinstance(emailNew, str):
            raise ValueError("Email inválido.")
        self.__email = emailNew

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, senhaNew):
        if not senhaNew or not isinstance(senhaNew, str):
            raise ValueError("Senha inválida.")
        self.__senha = senhaNew

    @property
    def num_documento(self):
        return self.__num_documento

    @num_documento.setter
    def num_documento(self, numDocNew):
        if not numDocNew or not isinstance(numDocNew, str):
            raise ValueError("Documento inválido.")
        self.__num_documento = numDocNew

    def autenticar(self, senha_digitada):
        return senha_digitada == self.senha

    def atualizar_dados(self, novos_dados: dict) -> bool:
        try:
            if "nome" in novos_dados:
                self.nome = novos_dados["nome"]

            if "email" in novos_dados:
                self.email = novos_dados["email"]

            if "senha" in novos_dados:
                self.senha = novos_dados["senha"]

            return True

        except ValueError as e:
            print(f"Erro ao atualizar dados: {e}")
            return False

    def exibir_dados(self):
        return (
            f"Usuário:\n"
            f"  Código: {self.cod_usuario}\n"
            f"  Nome: {self.nome}\n"
            f"  Email: {self.email}\n"
            f"  Documento: {self.num_documento}"
        )

    def salvar(self):
        print(f"Usuário {self.nome} (ID: {self.cod_usuario}) salvo com sucesso!")




        



