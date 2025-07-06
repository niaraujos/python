#declarar
def soma():
  calculo = 10+2
  print(f'a soma é {calculo}')
 #chamar
soma()
#parametros
num1 = 10
num2 = 5

def soma(num1,num2):
  calculo = num1 + num2
  print(f'a soma é {calculo}')


def multi(num1,num2):
  calculo = num1 * num2
  print(f'a multiplicação é {calculo}')

 #chamar
multi(num1, num2)
soma(num1, num2)


#manipulação de arquivos
def soma():
  calculo = 10+2
  file = 'arquivo.txt'

  #abertura de arquivo e escrita

  arquivo_escrita = open(file, "w") # w de write, escrever
  arquivo_escrita.write(f'a adição é {calculo}')
  arquivo_escrita.close()


  #abrir para leitura o texto arquivo modificado
  arquivo_leitura = open(file, "r") # r de read, ler
  leitura = arquivo_leitura.read()
  print(leitura)
  arquivo_leitura.close()

soma()


#tratamentos e exceções
try, except
TypeError as e:

https://docs.python.org/pt-br/3/tutorial/errors.html