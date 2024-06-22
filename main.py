sair = 1
nota = 11
titulo = "titulo"

try:
    titulo = input('digite o nome do filme: ')
    while nota not in (0,1,2,3,4,5,6,7,8,9,10): 
        try:
            nota = int(input('Digite a nota de 0 a 10: '))
            if nota not in (0,1,2,3,4,5,6,7,8,9,10):
                print("Valores errados, vamos tentar novamente")
        except:
            print("Valores errados")
except:
    print("erro insperado")

ordem_filmes = {titulo: nota}

while sair != 0:
    titulo = input('digite o nome de outro filme: ')
    nota = int(input('Digite a nota de 0 a 10: '))
    while nota not in (0,1,2,3,4,5,6,7,8,9,10): 
        try:
            print("Valores errados, vamos tentar novamente")
            nota = int(input('Digite a nota de 0 a 10: '))
            if nota not in (0,1,2,3,4,5,6,7,8,9,10):
                print("Valores errados, vamos tentar novamente")
        except:
            print("Valores errados")
    ordem_filmes[titulo] = nota
    
    try:
        sair = int(input("digite '0' para sair ou '1' inserir outro filme: "))
        print(ordem_filmes)
    except:
        print("Vou entender que queria digitar '1'")

print([max(ordem_filmes, key=ordem_filmes.get)])
