from Model.Programacao import Programacao
from Model.Fornecedor import Fornecedor

class Feira:
    def __init__(self, cod_feira, nome_feira, programacoes=None, fornecedores=None):
        self.cod_feira = cod_feira
        self.nome_feira = nome_feira
        self.programacoes = programacoes if programacoes is not None else []
        self.fornecedores = fornecedores if fornecedores is not None else []

    @property
    def cod_feira(self):
        return self.__cod_feira
    
    @cod_feira.setter
    def cod_feira(self, cod_feira):
        self.__cod_feira = cod_feira

    @property
    def nome_feira(self):
        return self.__nome_feira

    @nome_feira.setter
    def nome_feira(self, nome_feiraNew):
        if not nome_feiraNew or not isinstance(nome_feiraNew, str):
            raise ValueError("O nome da Feira não pode ser vazio ou nulo")
        self.__nome_feira = nome_feiraNew

    @property
    def programacoes(self):
        return self.__programacoes

    @programacoes.setter
    def programacoes(self, programacoesNew):
        if not isinstance(programacoesNew, list):
            raise ValueError("Programações devem ser uma lista")
        if not all(isinstance(p, Programacao) for p in programacoesNew):
            raise ValueError("Todos os itens da lista devem ser instâncias de Programacao")
        self.__programacoes = programacoesNew

    @property
    def fornecedores(self):
        return self.__fornecedores

    @fornecedores.setter
    def fornecedores(self, fornecedoresNew):
        if not isinstance(fornecedoresNew, list):
            raise ValueError("Fornecedores devem ser uma lista")
        if not all(isinstance(f, Fornecedor) for f in fornecedoresNew):
            raise ValueError("Todos os itens da lista devem ser instâncias de Fornecedor")
        self.__fornecedores = fornecedoresNew

    def to_dict(self):
        return {
            "cod_feira": self.cod_feira,
            "nome_feira": self.nome_feira,
            "programacoes": [p.to_dict() for p in self.programacoes],
            "fornecedores": [f.cod_fornecedor for f in self.fornecedores],
        }
