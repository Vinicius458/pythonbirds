class Pessoa:
    olhos=2
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade= idade
        self.filhos=list(filhos)
    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'
    @staticmethod
    def metodo_estatico():
       return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'
class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe=Pessoa.cumprimentar(self) #Ou cumprimentar_da_classe=super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos=3

if __name__ == '__main__':
    vinicius = Mutante(nome='Vinicius')
    jeferson=Homem(vinicius, nome='Jeferson')
    print(Pessoa.cumprimentar(jeferson))
    print(id(jeferson))
    print(jeferson.cumprimentar())
    print(jeferson.nome)
    print(jeferson.idade)

for filho in jeferson.filhos:
    print(filho.nome)
    jeferson.sobrenome='Padua'
    del jeferson.filhos
    jeferson.olhos=1
    del jeferson.olhos

    print(jeferson.__dict__)
    print(vinicius.__dict__)
    Pessoa.olhos=3
    print(Pessoa.olhos)
    print(jeferson.olhos)
    print(vinicius.olhos)
    print(id(Pessoa.olhos), id(jeferson.olhos), id(vinicius.olhos))
    print(Pessoa.metodo_estatico(), jeferson.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), jeferson.nome_e_atributos_de_classe())
    pessoa=Pessoa('Anonimo')
    print(isinstance(pessoa,Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(vinicius, Pessoa))
    print(isinstance(vinicius, Homem))
    print(vinicius.olhos)
    print(jeferson.cumprimentar())
    print(vinicius.cumprimentar())




