
CREATE TABLE "Alunos"(
	"NroMatricula" INT GENERATED ALWAYS AS IDENTIFY,
	"CPF" char(11) NOT NULL UNIQUE,
	"Nome" varchar(255) NOT NULL,
	"Telefone" INT,
	"AnoNasc" DATE,

	PRIMARY KEY("NroMatricula")
	
);
INSERT INTO "Alunos"(
        VALUES ('DEFAULT, '12345678910', 'Davi', '85988887777', '07-05-2002');


CREATE TABLE "Disciplina"(
	"CodDisciplina" INT GENERATED ALWAYS AS IDENTIFY,
	"Nome" varchar (255) NOT NULL,
	"CodCurso" INTO REFERENCES curso (id),

    PRIMARY KEY(CodDisciplina)

);
INSERT INTO "Disciplina"
        VALUES ('DEFAULT', 'Python', '1');


CREATE TABLE "Matriculas"(
	"NroMatricula" INT GENERATED ALWAYS AS IDENTIFY,
	"Semestre" INT,
	"Ano" INT,
	"NroFaltas" INT,

	PRIMARY KEY ("NroMatricula")
);
INSERT INTO "Matriculas"(
        VALUES ('DEFAULT', '4', '2023', '15');
	
CREATE TABLE "Alunos"(
	"NroMatricula" INT GENERATED ALWAYS AS IDENTIFY,
	"CPF" char(11) NOT NULL UNIQUE,
	"Nome" varchar(255) NOT NULL,
	"Telefone" INT,
	"AnoNasc" DATE,

	PRIMARY KEY("NroMatricula")
	
);
INSERT INTO "Alunos"
        VALUES ('DEFAULT, '12345678910', 'Davi', '85988887777', '07-05-2002');


CREATE TABLE "Disciplina"(
	"CodDisciplina" INT GENERATED ALWAYS AS IDENTIFY,
	"Nome" varchar (255) NOT NULL,
	"CodCurso" INTO REFERENCES curso (id),

      PRIMARY KEY(CodDisciplina)

);
INSERT INTO "Disciplina"
        VALUES ('DEFAULT', 'Python', '1');


CREATE TABLE "Matriculas"(
	"NroMatricula" INT GENERATED ALWAYS AS IDENTIFY,
	"Semestre" INT,
	"Ano" INT,
	"NroFaltas" INT,

	PRIMARY KEY ("NroMatricula")
);
INSERT INTO "Matriculas"(
        VALUES ('DEFAULT', '4', '2023', '15');
	