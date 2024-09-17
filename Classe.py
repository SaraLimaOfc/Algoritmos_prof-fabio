class Pessoa:
    def __init__(self, nome='', idade=0, peso=0.0, altura=0.0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos=1):
        if anos < 0:
            return "Anos deve ser um número positivo"
        self.idade += anos
        if self.idade < 21:
            self.altura += 0.5 * anos

    def engordar(self, quilos):
        if quilos < 0:
            return "Quilos deve ser um número positivo"
        self.peso += quilos

    def emagrecer(self, quilos):
        if quilos < 0:
            return "Quilos deve ser um número positivo"
        if quilos > self.peso:
            return "Não é possível emagrecer mais do que o peso atual"
        self.peso -= quilos

    def crescer(self, centimetros):
        if centimetros < 0:
            return "Centímetros deve ser um número positivo"
        self.altura += centimetros

    def __str__(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso}kg, Altura: {self.altura}cm'

if __name__ == '__main__':
    pessoa = Pessoa('Sara', 23, 100, 175)
    print(pessoa)

    pessoa.envelhecer(3)
    print("Após envelhecer 3 anos:", pessoa)

    pessoa.engordar(5)
    print("Após engordar 5kg:", pessoa)

    pessoa.emagrecer(2)
    print("Após emagrecer 2kg:", pessoa)

    pessoa.crescer(2)
    print("Após crescer 2cm:", pessoa)
