class Pessoa:
    olhos=2
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade= idade
        self.filhos=list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    vinicius = Pessoa(nome='Vinicius')
    jeferson=Pessoa(vinicius, nome='Jeferson')
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