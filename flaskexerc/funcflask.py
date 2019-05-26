from funcionario import funcionario
from funcionarioDAO import FuncionarioDao
from depto import departamento
from deptoDAO import deptoDao
from flask import Flask, redirect, url_for, render_template, request, session, flash
app = Flask(__name__)
app.env='development'

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/index')
def index():
    return render_template("funcionario/index.html")

@app.route('/logar')
def logar():
    return render_template("funcionario/login.html")

@app.route('/login',methods = ['POST', 'GET'])
def login():
    daofunc = FuncionarioDao()
    f = daofunc.procurar(request.form["senha"],request.form["login"])
    if(f == None):
        return ('senha ou login errado')
    else:
        session['logged_in'] = True
        session['login'] = request.form["login"]
        session['senha'] = request.form["senha"]
        session['nome'] = f._nomeFunc
        session['admin'] = True
        if(f.admin == "true"):
            return redirect('/funcionario/listar')
        else:
            return redirect('index')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect('index')

@app.route('/funcionario/listar')
def listar():
    dao = FuncionarioDao()
    lista = dao.listar()
    return render_template("funcionario/listar.html", len = len(lista), lista = lista)

@app.route('/inserir')
def inserir():
    daoA = deptoDao()
    lista = daoA.listar()
    return render_template("funcionario/insert.html", len = len(lista), lista = lista)

@app.route('/tratainsert', methods=["POST"])
def insert():
    dao = FuncionarioDao()
    nome = request.form["nome"]
    email = request.form["email"]
    coddept = request.form["coddept"]
    cpf = request.form["CPF"]
    login = request.form["nome"]
    senha = request.form["senha"]
    admin = request.form["admin"]
    func = funcionario(cpf, email, nome, login, senha, admin)
    func.codDept = coddept
    dao.inserir(func)
    return redirect(url_for('listar'))

@app.route('/funcionario/busca/<int:cod>')
def buscar(cod):
    dao = FuncionarioDao()
    buscando = dao.buscar(cod)
    return render_template("funcionario/buscar.html", buscando = buscando)

@app.route('/excluir/<int:cod>')
def excluir(cod):
    dao = FuncionarioDao()
    dao.excluir(cod)
    return redirect(url_for('listar'))

@app.route('/funcionario/alterar/<int:cod>')
def alter(cod):
    daoA = deptoDao()
    lista = daoA.listar()
    daoF = FuncionarioDao()
    buscar = daoF.buscar(cod)
    return render_template("funcionario/alterar.html", len = len(lista), lista= lista, buscar = buscar)

@app.route('/tratalterar', methods=["POST"])
def alterar():
    dao = FuncionarioDao()
    cod = request.form["cod"]
    nome = request.form["nome"]
    email = request.form["email"]
    coddept = request.form["coddept"]
    cpf = request.form["CPF"]
    login = request.form["nome"]
    senha = request.form["senha"]
    admin = request.form["admin"]
    func = funcionario(cpf, email, nome, login, senha, admin)
    func.codFunc = cod
    func.codDept = coddept
    dao.alterar(func)
    return redirect(url_for('listar'))

if (__name__ == "__main__"):
    app.run(debug=True, port=5000)