class Aluno:
       def __init__(self, matricula, nome, sexo, idade):
        self.matricula = matricula
        self.nome = nome
        self.sexo =  sexo
        self.idade = idade

if __name__ == "__main__":
    aluno1 = Aluno("0001234" , "Ana", "Femenino", "16")
    aluno2 = Aluno("0005678", "john", "masculino", "17" )
    print(aluno1.matricula, aluno1.nome, aluno1.sexo, aluno1.idade)
    print(aluno2.matricula, aluno2.nome, aluno2.sexo, aluno2.idade)
