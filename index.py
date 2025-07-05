# variáveis
"""
para declarar uma variavel em python, escreve apenas o nome da variável, como ex: idade = 10, idade ='10 anos', velho = False
"""

# comentários em python

#comentar várias linhas de código usa 3 aspas
""" #tipos de variáveis
inteiro, float, string, booleano"""

# tipo inteiro - numero inteiro ex: 10, 1, 10000
""" numero = int(input("Digite um número: "))
print(numero)"""

# tipo float - numero decimal ou flutuante ex: 10.5, 1.2, 1000.5
""" numero = float(input("Digite um número: "))
print(numero)"""

#tipo string "texto, frase ou palavra"
# por padrao o input recebe o valor string
"""frase = input("Digite sua frase: ") 
print(frase)"""

#input
"""
input('faça algo aqui':)
entrada de dados, valores digitados pelo usuário
"""

# a conversão pode ser feita tanto na variavel ou na sua chamada dentro do print, ex print(int())

#operadores matemáticos
"""
soma +
subtração -
multiplicação *
divisão /  # 10/2  saida: 5.0
divisão inteira //  # 10//2  saida: 5
"""

#divisão inteira //

"""numero1 = int(input("Digite um número 01: "))
numero2 = int(input("Digite um número 02: "))
numero = numero1 // numero2
print(numero)"""


# incremento +=
# decremento -=
"""
valor = 5
valor += 1
print(valor)
#saida = 6
valor -+
print(valor)
"""
# resto %

"""resto = 10%3
print(resto)"""

#ordem de precedencia, igual a da amtematica basica

#operadores relacionais
"""igual ==
maior que >
maior que ou igual >=
menor <
menor ou igual <=
diferente !="""

#formatação de texto com variáveis, (tipo template string do javascript)
#print(f'texto{variavel}')
"""resto = 10%3
print(f 'o resto da conta é {resto}')"""

#quantidades de numeros apos o ponto
"""
valor =45.3455
print(f'{valor:.2f}')
"""
#variaveis sem estar declaradas
"""print('Oi {}, voce tem {} anos'.format('Niedja',33))"""