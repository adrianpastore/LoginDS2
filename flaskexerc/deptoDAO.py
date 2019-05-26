from depto import departamento
import psycopg2

class deptoDao:
    def __init__(self):
        self._dados_con = "dbname=ds2aula host=localhost user=postgres password=postgres port=5432"

    def inserir(self, departamento):
            with psycopg2.connect(self._dados_con) as conn:
                cur = conn.cursor()
                sql = cur.execute('INSERT INTO "departamento" (nome, "dataHoraAtualizacao") VALUES (%s, now()) returning codDepartamento', [departamento.nome])
                adicionado = cur.fetchone()
                departamento.codDepartamento = adicionado[0]
                conn.commit()
                cur.close()

    def excluir(self, cod):
        #try:
            with psycopg2.connect(self._dados_con) as conn:
                cur = conn.cursor()
                sql = cur.execute('DELETE FROM "departamento" WHERE "codDepartamento" = (%s)',[cod])
                conn.commit()
                cur.close()
        #except ValueError:
        #    print('Valor não encontrado.')
    
    def alterar(self, departamento):
        #try:
            with psycopg2.connect(self._dados_con) as conn:
                cur = conn.cursor()
                sql = cur.execute('UPDATE "departamento" SET nome = %s, "dataAtualizacao" = now() WHERE "codDepartamento" = (%s)',[departamento.nome, departamento.codDepartamento])
                conn.commit()
                cur.close()
        #except psycopg2.Error as e:
        #    print(e.pgerror)

    def buscar(self, cod):
        #try:
        with psycopg2.connect(self._dados_con) as conn:
            cur = conn.cursor()
            sql = cur.execute('SELECT * FROM "departamento" WHERE "codDepartamento" = (%s)',[cod])
            busca = cur.fetchall()
            Departamento = departamento(busca[0][1])
            Departamento.codDept = cod
            cur.close()
            return Departamento
        #except Exception:
        #    print('Deu ruim')
        #   raise e

    def salvar(self, departamento):
        newDao = deptoDao()
        if (departamento.codDepartamento != None):
            print('Alterando departamento...')
            newDao.alterar(departamento)
            print('Alterando com sucesso!')
        else:
            print('Inserindo departamento...')
            newDao.inserir(departamento)
            print('Inserido com sucesso!')

    def listar(self):
        vet = []
        with psycopg2.connect(self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM "departamento"')
            for linha in cur.fetchall():
                depto = departamento(linha[1])
                depto.codDept = int(linha[0]) 
                vet.append(depto)
            cur.close()
        return vet
