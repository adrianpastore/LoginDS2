CREATE TABLE  "departamento" (	
	"codDepartamento" serial, 
	"nome" VARCHAR(100),
	"dataAtualizacao" date, 
	"codGerente" integer,
	CONSTRAINT "DepartamentoPK" PRIMARY KEY ("codDepartamento")
);

CREATE TABLE "funcionario"(
	"codFuncionario" serial,
	"codDepartamento" integer,
	"CPF" varchar(15) UNIQUE, 
	"email" varchar(50) UNIQUE, 
	"nome" varchar(50) NOT NULL,
	"login" varchar(50) NOT NULL,
	"senha" varchar(50) NOT NULL,
	"admin" boolean,
	CONSTRAINT "FuncionarioPK" PRIMARY KEY ("codFuncionario"),
	CONSTRAINT "FuncionarioFKDepartamento" FOREIGN KEY ("codDepartamento")
		REFERENCES "departamento" ("codDepartamento")
			on delete set null
			on update cascade
);

ALTER TABLE "departamento" ADD CONSTRAINT  "DepartamentoFKGerente"  FOREIGN KEY ("codGerente") 
	REFERENCES "funcionario" ("codFuncionario")
		ON DELETE SET NULL
		ON UPDATE CASCADE 


CREATE TABLE  "projeto" (	
	"codProjeto" serial, 
	"nome" VARCHAR(100),
	"dataPrevista" date, 
	CONSTRAINT "projetoPK" PRIMARY KEY ("codProjeto")
);

CREATE TABLE "funcProj"(
	"codProjeto" integer,
	"codFuncionario" integer,
	CONSTRAINT "projFK" FOREIGN KEY ("codProjeto")
		REFERENCES "projeto" ("codProjeto")
			on delete set null
			on update cascade,
	CONSTRAINT "funcFK" FOREIGN KEY ("codFuncionario")
		REFERENCES "funcionario" ("codFuncionario")
			on delete set null
			on update cascade
);

SELECT * FROM "departamento"
SELECT * FROM "funcionario"
SELECT * FROM "projeto"

INSERT INTO "departamento"("nome","dataAtualizacao") VALUES
('Design Gráfico', now()), 
('Gestão Empresarial', now()), 
('RH', now()), 
('Gestão de Projetos', now());


INSERT INTO "funcionario"("codDepartamento", "CPF", "email","nome","login","senha","admin") VALUES
(7, 02489721, 'joao_e_maria@gmail.com','João Maria Hanson', 'jãoria', 12345, true),
(5, 9287318, 'elvis@yahoo.com.br','Elvis Presley','presley', 0987, true),
(6, 923928321, 'malia_mory@gmail.com','Maria Molly', 'molly', 12345, false);