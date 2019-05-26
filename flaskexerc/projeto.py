from datetime import date
class projeto:
    def __init__(self, nome, dataPrevista):
        self._nome = nome
        self._dataPrevista = dataPrevista
        self._codProj = None

    def __str__(self):
        return "PROJETO - Código:{}, nome:{}, data prevista de entrega:{}".format(self._codProj, self._nome, self._dataPrevista)

    @property
    def codProj(self):
        return self._codProj
    
    @codProj.setter
    def codProj(self, codProj):
        self._codProj = codProj

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def dataPrevista(self):
        return self._dataPrevista
    
    @dataPrevista.setter
    def dataPrevista(self, dataPrevista):
        self._dataPrevista = dataPrevista
    

proj = projeto("meu projetinho", date(2019, 8, 21))
print(proj)