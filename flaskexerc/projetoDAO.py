from projeto import projeto
import psycopg2

class ProjetoDao:
    def __init__(self):
        self._dados_con = "dbname=ds2aula host=localhost user=postgres password=postgres port=5432"

    def inserir(self, projeto):
            with psycopg2.connect(self._dados_con) as conn:
                cur = conn.cursor()
                sql = cur.execute('INSERT INTO "projeto" ("nome", "dataPrevista") VALUES (%s, %s) returning "codProjeto"', [projeto.nome, projeto.dataPrevista])
                busca= cur.fetchall()
                projeto.codFunc= busca[0][0]
                conn.commit()
                cur.close()

    def buscar(self, cod):
        with psycopg2.connect(self._dados_con) as conn:
            cur = conn.cursor()
            sql = cur.execute('SELECT * FROM "projeto" WHERE "codProjeto" = (%s)',[cod])
            busca= cur.fetchone()
            proj = projeto(busca[1], busca[2])
            proj.codFunc = busca[0]
            cur.close()
        return proj

    def listar(self):
        vet = []
        with psycopg2.connect(self._dados_con) as conn:
            cur = conn.cursor()
            cur.execute('SELECT "codProjeto","nome", "dataPrevista" FROM "projeto"')
            for linha in cur.fetchall():
                proj = projeto(linha[1], linha[2])
                proj.codFunc = int(linha[0]) 
                vet.append(proj)
            cur.close()
        return vet

    def excluir(self, cod):
            with psycopg2.connect(self._dados_con) as conn:
                cur = conn.cursor()
                sql = cur.execute('DELETE FROM "projeto" WHERE "codProjeto" = (%s)',[cod])
                conn.commit()
                cur.close()

    def alterar(self, projeto):
            with psycopg2.connect(self._dados_con) as conn:
                cur = conn.cursor()
                sql = cur.execute('UPDATE "projeto" SET "nome" = %s, "dataPrevista" = %s WHERE "codProjeto" = (%s)', [projeto.nome, projeto.dataPrevista])
                conn.commit()
                cur.close()