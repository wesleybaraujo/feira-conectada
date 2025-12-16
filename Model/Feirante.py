from Model.Usuario import Usuario

class Feirante(Usuario):
    def __init__(self, cod_feirante, cod_usuario, nome, email, senha, num_documento, endereco, telefone, feira):
        super().__init__(cod_usuario, nome, email, senha, num_documento)
        self.cod_feirante = cod_feirante
        self.endereco = endereco
        self.telefone = telefone
        self.feira = feira
        self.produtos = []  # Lista de produtos que o feirante vende

    @property
    def cod_feirante(self):
        return self.__cod_feirante

    @cod_feirante.setter
    def cod_feirante(self, codNew):
        if not codNew:
            raise ValueError("Código do feirante inválido.")
        self.__cod_feirante = codNew

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

    @property
    def feira(self):
        return self.__feira

    @feira.setter
    def feira(self, feiraNew):
        if not feiraNew:
            raise ValueError("Feira inválida.")
        self.__feira = feiraNew

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        return [p.nome for p in self.produtos]

    def exibir_dados(self):
        return (
            f"Feirante:\n"
            f"  Código do Feirante: {self.cod_feirante}\n"
            f"  Código do Usuário: {self.cod_usuario}\n"
            f"  Nome: {self.nome}\n"
            f"  Email: {self.email}\n"
            f"  Documento: {self.num_documento}\n"
            f"  Feira: {self.feira.nome_feira}\n"
            f"  Produtos: {', '.join(self.listar_produtos())}"
        )

    def salvar(self):
        print(f"Feirante {self.nome} (ID: {self.cod_feirante}) salvo com sucesso!")
