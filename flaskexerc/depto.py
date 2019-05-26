class departamento:
    def __init__(self, nome):
        self._nome = nome
        self._codDept = None
        self._funcionarios = []
        self._gerente = ''

    def __str__(self):
        return "codDept:{}, nome:{}, gerente:{}".format(self._codDept, self._nome, self._gerente)

    @property
    def codDept(self):
        return self._codDept
    
    @codDept.setter
    def codDept(self, codDept):
        self._codDept = codDept

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def gerente(self):
        return self._gerente
    
    @gerente.setter
    def gerente(self, gerente):
        self._gerente = gerente
    
    @property
    def funcionarios(self):
        return self._funcionarios
    
    @funcionarios.setter
    def funcionarios(self, funcionarios):
        self._funcionarios = funcionarios
    
    def alocaFuncionario(self, funcionario):
        self._funcionarios.append(funcionario)

