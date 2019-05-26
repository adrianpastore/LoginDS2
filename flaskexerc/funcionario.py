from depto import departamento

class funcionario:    
    def __init__(self, cpf, email, nomeFunc, login, senha = None, admin = 'false'):
        self._nomeFunc = nomeFunc
        self._cpf = cpf
        self._codFunc = None
        self._deptFunc = None
        self._email = email
        self._login = login
        self._senha = senha
        self._admin = admin


    def __str__(self):
        return "codFunc:{}, cpf:{}, email:{}, nomeFunc:{}, deptFunc:{}, login:{}, admin:{}".format(self._codFunc, self._cpf, self._email, self._nomeFunc, self._deptFunc, self._login, self._admin)

    @property
    def codFunc(self):
        return self._codFunc
    
    @codFunc.setter
    def codFunc(self, codFunc):
        self._codFunc = codFunc

    @property
    def nomeFunc(self):
        return self._nomeFunc
    
    @nomeFunc.setter
    def nomeFunc(self, nomeFunc):
        self._nomeFunc = nomeFunc

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf    
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email

    @property
    def deptFunc(self):
        return self._deptFunc
    
    @deptFunc.setter
    def deptFunc(self, deptfunc):
        self._deptFunc = deptfunc
    
    @property
    def login(self):
        return self._login
    
    @login.setter
    def login(self, login):
        self._login = login

    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, senha):
        self._senha = senha

    @property
    def admin(self):
        return self._admin
    
    def eadmin(self):
        self._admin = 'true'