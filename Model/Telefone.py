class Telefone:
    def __init__(self,cod_telefone,ddd,numero):
       self.cod_telefone = cod_telefone
       self.ddd = ddd
       self.numero = numero
    
    @property
    def cod_telefone(self):
        return self.__telefone
    
    @property
    def ddd(self):
        return self.__ddd
    
    @ddd.setter
    def ddd(self,dddNew):
        if not dddNew or not isinstance(dddNew,str):
            raise ValueError("DDD não pode ser vazia ou nula")
        self.__ddd = dddNew

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def mumero(self,numeroNew):
        if not numeroNew or not isinstance(numeroNew,str):
            raise ValueError("Número não pode ser vazia ou nula")
        self.__numero = numeroNew
        
        


    
