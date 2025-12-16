from Model.Usuario import Usuario

class Consumidor(Usuario):
    def __init__(self, cod_consumidor, cod_usuario, nome, email, senha, num_documento, endereco, telefone):
        super().__init__(cod_usuario, nome, email, senha, num_documento)
        self.cod_consumidor = cod_consumidor
        self.endereco = endereco
        self.telefone = telefone
        self.historico_compras = []

    @property
    def cod_consumidor(self):
        return self.__cod_consumidor

    @cod_consumidor.setter
    def cod_consumidor(self, codNew):
        if not codNew:
            raise ValueError("Código do consumidor inválido.")
        self.__cod_consumidor = codNew

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, enderecoNew):
        if not enderecoNew:
            raise ValueError("Endereço inválido.")
        self.__endereco = enderecoNew

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefoneNew):
        if not telefoneNew:
            raise ValueError("Telefone inválido.")
        self.__telefone = telefoneNew

    def adicionar_compra(self, compra):
        self.historico_compras.append(compra)

    def listar_compras(self):
        return self.historico_compras

    def exibir_dados(self):
        return (
            f"Consumidor:\n"
            f"  Código do Consumidor: {self.cod_consumidor}\n"
            f"  Código do Usuário: {self.cod_usuario}\n"
            f"  Nome: {self.nome}\n"
            f"  Email: {self.email}\n"
            f"  Documento: {self.num_documento}\n"
            f"  Total de Compras: {len(self.historico_compras)}"
        )

    def salvar(self):
        print(f"Consumidor {self.nome} (ID: {self.cod_consumidor}) salvo com sucesso!")
