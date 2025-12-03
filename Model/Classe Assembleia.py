class Assembleia:
   def __init__(self,cod_assembleia,data,resumo,ata):
      self.cod_assembleia = cod_assembleia
      self.data = data
      self.resumo = resumo
      self.ata = ata
    
@property
def cod_assembleia(self):
    return self.__cod_assembleia

@property
def data(self):
    return self.data

@data.setter
def data(self,dataNew):
    if not dataNew or not isinstance(dataNew,str):
        raise ValueError("Data não pode ser vazia ou nula")
    self.__data = dataNew


@property
def resumo(self):
    return self.resumo

@resumo.setter
def resumo(self,resumoNew):
    if not resumoNew or not isinstance(resumoNew,str):
        raise ValueError("Resumo não pode ser vazia ou nula")
    self.__resumo = resumoNew

@property
def ata(self):
    return self.ata

@ata.setter
def ata(self,ataNew):
    if not ataNew or not isinstance(ataNew,str):
        raise ValueError("Ata não pode ser vazia ou nula")
    self.__ataNew = ataNew


    