from Model.Fornecedor import Fornecedor

class FornecedorController:
    def __init__(self):
        self.fornecedores = []

    def create_fornecedor(self, cod_fornecedor, razao_social, nome_resp, num_doc):
        fornecedor = Fornecedor(cod_fornecedor, razao_social, nome_resp, num_doc)
        self.fornecedores.append(fornecedor)
        return fornecedor

    def get_fornecedor(self, cod_fornecedor):
        for fornecedor in self.fornecedores:
            if fornecedor.cod_fornecedor == cod_fornecedor:
                return fornecedor
        return None

    def update_fornecedor(self, cod_fornecedor, razao_social, nome_resp, num_doc):
        fornecedor = self.get_fornecedor(cod_fornecedor)
        if fornecedor:
            fornecedor.razao_social = razao_social
            fornecedor.nome_resp = nome_resp
            fornecedor.num_doc = num_doc
            return fornecedor
        return None

    def delete_fornecedor(self, cod_fornecedor):
        fornecedor = self.get_fornecedor(cod_fornecedor)
        if fornecedor:
            self.fornecedores.remove(fornecedor)
            return True
        return False
    
    def get_all_fornecedores(self):
        return self.fornecedores
