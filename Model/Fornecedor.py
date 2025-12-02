class Fornecedor:
    def __init__(self, cod_fornecedor,razao_social,nome_resp, num_doc):
        self.cod_fornecedor = cod_fornecedor
        self.razao_social = razao_social 
        self.nome_resp = nome_resp
        self.num_doc = num_doc
  
    @property
    def cod_fornecedor(self):
       return self.__cod_fonecedor
    
    @property
    def razao_social(self):
       return self.__razao_social
    
    @razao_social.setter
    def razao_social(self, razao_socialNew):
        if not razao_socialNew or not isinstance(razao_socialNew, str):
            raise ValueError("Razão social não pode ser vazia ou nula")
        self.__razao_social = razao_socialNew

    @property
    def nome_resp(self):
        return self.__nome_resp
        
    @nome_resp.setter
    def nome_resp(self, nome_respNew):
        if not nome_respNew or not isinstance(nome_respNew, str):
            raise ValueError("Nome Responsável não pode ser vazio ou nulo")
        self.__nome_resp = nome_respNew

    @property
    def num_doc(self):
       return self.__num_doc
    
    @num_doc.setter
    def num_doc(self, num_docNew):
        if not num_docNew or not isinstance(num_docNew, str):
            raise ValueError("Numero do documento não pode ser vazio ou nulo")
        self.__num_doc = num_docNew



