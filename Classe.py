class Pessoa:
    def __init__(self, nome='', idade=0, peso=0.0, altura=0.0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos=1):
        self.idade += anos
        if self.idade < 21:
            self.altura += anos * 0.5

    def engordar(self, peso):
        self.peso += peso

    def emagrecer(self, peso):
        self.peso -= peso
        if self.peso < 0:
            self.peso = 0

    def crescer(self, altura):
        self.altura += altura

    def __str__(self):
        return (f'Nome: {self.nome}, Idade: {self.idade}, Peso: {self.peso}kg, Altura: {self.altura}cm')

if __name__ == '__main__':
    pessoa = Pessoa(nome='Sara', idade=23, peso=100.0, altura=1.75)
    print(pessoa)
    
    pessoa.envelhecer()
    print("Após envelhecer:")
    print(pessoa)
    
    pessoa.engordar(5)
    print("Após engordar:")
    print(pessoa)
    
    pessoa.emagrecer(3)
    print("Após emagrecer:")
    print(pessoa)
    
    pessoa.crescer(2)
    print("Após crescer:")
    print(pessoa)
