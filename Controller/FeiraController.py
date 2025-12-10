from Model.Feira import Feira
from Model.Fornecedor import Fornecedor
from Model.Programacao import Programacao

class FeiraController:
    def __init__(self):
        self.feiras = []

    def create_feira(self, cod_feira, nome_feira):
        feira = Feira(cod_feira, nome_feira)
        self.feiras.append(feira)
        return feira

    def get_feira(self, cod_feira):
        for feira in self.feiras:
            if feira.cod_feira == cod_feira:
                return feira
        return None

    def update_feira(self, cod_feira, nome_feira):
        feira = self.get_feira(cod_feira)
        if feira:
            feira.nome_feira = nome_feira
            return feira
        return None

    def delete_feira(self, cod_feira):
        feira = self.get_feira(cod_feira)
        if feira:
            self.feiras.remove(feira)
            return True
        return False
    
    def get_all_feiras(self):
        return self.feiras

    def adicionar_fornecedor_a_feira(self, cod_feira, fornecedor: Fornecedor):
        feira = self.get_feira(cod_feira)
        if feira:
            feira.fornecedores.append(fornecedor)
            return True
        return False
    
    def remover_fornecedor_da_feira(self, cod_feira, fornecedor: Fornecedor):
        feira = self.get_feira(cod_feira)
        if feira:
            feira.fornecedores.remove(fornecedor)
            return True
        return False
        
    def adicionar_programacao_a_feira(self, cod_feira, programacao: Programacao):
        feira = self.get_feira(cod_feira)
        if feira:
            feira.programacoes.append(programacao)
            return True
        return False
        
    def remover_programacao_da_feira(self, cod_feira, programacao: Programacao):
        feira = self.get_feira(cod_feira)
        if feira:
            feira.programacoes.remove(programacao)
            return True
        return False
