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
            raise ValueError("O código do gerente não pode ser vazio")
        self.__cod_gerente = codGerenteNew
