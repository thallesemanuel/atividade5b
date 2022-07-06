#Faça um programa que leia 4 notas de um aluno, salve as em uma lista e calcule a média das notas.
 

from re import A

n1 = float( input( "informe a nota 1: ") )
n2 = float( input( "informe a nota 2: ") )
n3 = float( input( "informe a nota 3: ") )
n4 = float( input( "informe a nota 4: ") ) 

media = (float(n1) + float(n2) + float(n3) + float(n4) /4)

print("As notas desse aluno foram: ")
print(str(n1))
print(str(n2))
print(str(n3))
print(str(n4))
print("A média da nota desse aluno é " + str(media))