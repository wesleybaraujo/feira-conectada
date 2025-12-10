from datetime import datetime, time

class Programacao:
    def __init__(self, cod_programacao, dia, hora_inicio, hora_fim):
        self.cod_programacao = cod_programacao
        self.dia = dia
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim

    @property
    def cod_programacao(self):
        return self.__cod_programacao
    
    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, diaNew):
        dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]
        if not diaNew or not isinstance(diaNew, str):
            raise ValueError("Dia não pode ser vazio ou nulo")
        if diaNew not in dias:
            raise ValueError(f"Dia deve ser um dos seguintes: {', '.join(dias)}")
        self.__dia = diaNew
    
    @property
    def hora_inicio(self):
        return self.__hora_inicio
    
    @hora_inicio.setter
    def hora_inicio(self, hora_inicioNew):
        if not hora_inicioNew or not isinstance(hora_inicioNew, time):
            raise ValueError("Hora de início não pode ser vazia ou nula")
        self.__hora_inicio = hora_inicioNew
    
    @property
    def hora_fim(self):
        return self.__hora_fim
    
    @hora_fim.setter
    def hora_fim(self, hora_fimNew):
        if not hora_fimNew or not isinstance(hora_fimNew, time):
            raise ValueError("Hora de fim não pode ser vazia ou nula")
        self.__hora_fim = hora_fimNew

    def to_dict(self):
        return {
            "cod_programacao": self.cod_programacao,
            "dia": self.dia,
            "hora_inicio": self.hora_inicio.isoformat(),
            "hora_fim": self.hora_fim.isoformat(),
        }
