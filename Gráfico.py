import matplotlib.pyplot as plt

# Dados de exemplo em ordem crescente
Altura = [1.50, 1.55, 1.60, 1.70, 1.75]
Peso = [90, 95, 100, 105, 110]

# Criando o gráfico de linha
plt.plot( Altura, Peso, marker= 'o' ) # 'marker' adiciona marcadores nos pontos de dados

# Adicionando títulos e rótulos
plt.title('Gráfico de Peso X Altura')
plt.xlabel('Eixo Altura')
plt.ylabel('Eixo Peso')

#Exibindo o gráfico
plt.show()
