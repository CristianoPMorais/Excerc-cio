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
            print("Digite apenas números inteiros")
except:
    print("erro inesperado")

ordem_filmes = {titulo: nota}

while sair != 0:
    
    try:
        titulo = input('digite o nome de outro filme: ')
        nota = 11
        while nota not in (0,1,2,3,4,5,6,7,8,9,10): 
            try:
                nota = int(input('Digite a nota de 0 a 10: '))
                if nota not in (0,1,2,3,4,5,6,7,8,9,10):
                    print("Valores errados, vamos tentar novamente")

            except:
                print("Digite apenas números inteiros")
        ordem_filmes[titulo] = nota

    except:
        print("erro insperado")
        
    try:
        sair = int(input("digite '0' para sair ou '1' inserir outro filme: "))
        if sair == 1:
            print("Ok \n")
        elif sair == 0:
            print("Segue abaixo os filmes avaliados com suas respectivas notas: \n")
            print(ordem_filmes)
            print("O filme melhor avaliado na sequencia foi o filme abaixo! \n")
            print([max(ordem_filmes, key=ordem_filmes.get)])
    except:
        print("Vou entender que queria digitar '1' \n")

