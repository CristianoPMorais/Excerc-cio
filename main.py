sair = 1
nota = 11
prosseguir = 1

titulo = input('digite o nome do filme: ')
while nota not in (0,1,2,3,4,5,6,7,8,9,10):
    try:
        while nota not in (0,1,2,3,4,5,6,7,8,9,10): 
            nota = int(input('Digite a nota de 0 a 10: '))
            if nota not in (0,1,2,3,4,5,6,7,8,9,10):
                print("Valores errados, vamos tentar novamente!")
    except:
        print("Valores errados")

    ordem_filmes = {titulo: nota}
    

while sair != 0:
    novo_titulo = input('digite o nome do filme: ')
    nova_nota = int(input('Digite a nota de 0 a 10: '))
    try:
        while nova_nota not in (0,1,2,3,4,5,6,7,8,9,10): 
            nova_nota = int(input('Digite a nota de 0 a 10: '))
            if nova_nota not in (0,1,2,3,4,5,6,7,8,9,10):
                print("Valores errados, vamos tentar novamente!")
    except:
        print("Valores errados")

    ordem_filmes = {novo_titulo: nova_nota}
    print("Deseja adicionar mais avaliações?")
    try:
        sair = int(input("digite '0' para sair ou '1' inserir outro filme: "))
        print(ordem_filmes)
    except:
        print("Vou entender que queria digitar '1'")

print([max(ordem_filmes, key=ordem_filmes.get)])
