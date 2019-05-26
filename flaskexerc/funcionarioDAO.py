from funcionario import funcionario
from depto import departamento
from deptoDAO import deptoDao
import psycopg2

class FuncionarioDao:
    def __init__(self):
        self._dados_con = "dbname=ds2aula host=localhost user=postgres password=postgres port=5432"

    def inserir(self, funcionario):
            with psycopg2.connect(self._dados_con) as conn:
                cur = conn.cursor()
                sql = cur.execute('INSERT INTO "funcionario" ("CPF", email, nome, "codDepartamento") VALUES (%s, %s, %s, %s) returning "codFuncionario"', [funcionario.cpf, funcionario.email, funcionario.nomeFunc, funcionario.deptFunc])
                busca= cur.fetchall()
                funcionario.codFunc= busca[0][0]
                conn.commit()
                cur.close()

    def buscar(self, cod):
        with psycopg2.connect(self._dados_con) as conn:
            cur = conn.cursor()
            sql = cur.execute('SELECT * FROM "funcionario" WHERE "codFuncionario" = (%s)',[cod])
            busca= cur.fetchone()
            func = funcionario(busca[2], busca[3], busca[4], busca[5], busca[6], busca[7])
            func.codFunc = busca[0]
            func.deptFunc = busca[1]
            cur.close()
        return func

    def listar(self):
        vet = []
        with psycopg2.connect(self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM "funcionario"')
            for linha in cur.fetchall():
                func = funcionario(linha[2], linha[3], linha[4], linha[5], linha[6], linha[7])
                func.codFunc = int(linha[0]) 
                vet.append(func)
            cur.close()
        return vet

    def excluir(self, cod):
            with psycopg2.connect(self._dados_con) as conn:
                cur = conn.cursor()
                sql = cur.execute('DELETE FROM "funcionario" WHERE "codFuncionario" = (%s)',[cod])
                conn.commit()
                cur.close()

    def alterar(self, funcionario):
            with psycopg2.connect(self._dados_con) as conn:
                cur = conn.cursor()
                sql = cur.execute('UPDATE "funcionario" SET "CPF" = %s, email = %s, nome = %s, "codDepartamento" = %s WHERE "codFuncionario" = (%s)', [funcionario.cpf, funcionario.email, funcionario.nomeFunc, funcionario.deptFunc, funcionario.codFunc])
                conn.commit()
                cur.close()
    
    def procurar(self,senha,login):
        with psycopg2.connect(self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * from funcionario WHERE senha = (%s) AND login = %s',[senha,login])
            linha = cur.fetchone()
            print(linha)
            if(linha == None):
                return None
            else:
                if(linha[7] == True):
                    func = funcionario(linha[2],linha[3],linha[4],linha[5])
                    func.codigo = linha[0]
                    func.eadmin()
                else:
                    func = funcionario(linha[2],linha[3],linha[4],linha[5])
                    func.codigo = linha[0]
                return func
            conn.commit()
            cur.close()

#dao = FuncionarioDao()
#f = dao.procurar('987', 'presley')
#print(f)