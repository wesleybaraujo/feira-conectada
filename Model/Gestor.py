from Model.Usuario import Usuario

class Gestor(Usuario):
    def __init__(self, cod_gerente, cod_usuario, nome, email, senha, num_documento):
        super().__init__(cod_usuario, nome, email, senha, num_documento)
        self.cod_gerente = cod_gerente

    @property
    def cod_gerente(self):
        return self.__cod_gerente

    @cod_gerente.setter
    def cod_gerente(self, codGerenteNew):
        if not codGerenteNew:
            raise ValueError
        self.__cod_gerente = codGerenteNew

    def exibir_dados(self):
        return (
            f"Gestor:\n"
            f"  Código do Gerente: {self.cod_gerente}\n"
            f"  Código do Usuário: {self.cod_usuario}\n"
            f"  Nome: {self.nome}\n"
            f"  Email: {self.email}\n"
            f"  Documento: {self.num_documento}"
        )

    def salvar(self):
        print(f"Gestor {self.nome} (Gerente ID: {self.cod_gerente}) salvo com sucesso!")
