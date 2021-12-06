import math
import os
from operator import itemgetter
from CorpoCeleste import CorpoCeleste
from Calculos import Calculos
from Simulacao import Simulacao

#####################################################################################


categorias = ('ESTRELA', 'PLANETA', 'LUA', 'ASTEROIDE')
calculos = Calculos()
simulacao = Simulacao()


while True:
    print('*' * 80)
    print('1-Cadastrar Corpo | 2-Ver Corpos | 3-Mover Corpo | 4-Simulação | 5-Sair')
    print('*' * 80)
    
    try:
        opcao = int(input())
        os.system('cls') or None
    except:
        os.system('cls') or None
        print("Favor digitar somente numeros inteiros!")
        continue
    
    if opcao not in (1, 2, 3, 4, 5) :
        os.system('cls') or None
        print("Opção inválida tente novamente por favor !")
        continue
    

    if(opcao == 1):
        os.system('cls') or None
        print('Dê um nome para o corpo')
        nomeCorpo = input('>>')
        try:
            print('informe a massa')
            massa = float(input('>>'))

            print('informe a coordenada X inicial')
            coordenadaX0 = float(input('>>'))

            print('informe a coordenada X final')
            coordenadaX1 = float(input('>>'))

            print('informe a coordenada Y inicial')
            coordenadaY0 = float(input('>>'))

            print('informe a coordenada Y final')
            coordenadaY1 = float(input('>>'))

            print('informe a coordenada Z inicial')
            coordenadaZ0 = float(input('>>'))

            print('informe a coordenada Z final')
            coordenadaZ1 = float(input('>>'))
        except:
            print("Insira apenas numeros por favor !")
            continue

        while(True):
            print('informe a categoria: Estrela, Planeta, Lua ou Asteroide')
            categoria = input('>>').upper()
            if(categoria in categorias):
                break
            else:
                print("\nCategoria inválida")
        # fim while categoria válida
        
        calculos.insereCorpo(
            CorpoCeleste(
                nomeCorpo, 
                massa, 
                coordenadaX0, 
                coordenadaX1, 
                coordenadaY0, 
                coordenadaY1, 
                coordenadaZ0, 
                coordenadaZ1, 
                categoria
            )
        )

    elif(opcao == 2):
        print(calculos.mostraCorpos(categorias, 0, 0))
        
        print("Calculos: ")       
        print("Média das distâncias: {}".format(calculos.mediaDistancia(0, 0)))
        print("Média das massas: {}".format(calculos.mediaMassas()))    
        print("Desvio padrão das massas: {}".format(calculos.desvioPadrao()))
        print("\nForça gravitacional resultante: ")
        print(calculos.calculoForcaGravitacional(0, 0))

    elif(opcao == 3):

        print(calculos.mostraCorpos(categorias, 0, 0))    

        while(True):
            print("Informe o nome para ser buscado")
            nomeBusca = input(">>")
            if(calculos.existeCorpo(nomeBusca)):
                break
            else:
                print("Esse nome de corpo não existe cadastrado, favor informar outro!")
                continue
        #fim while nome válido

        aux = 0
        for i in range(0, len(calculos.corpos)):
            if(calculos.corpos[i].nomeCorpo == nomeBusca):
                aux = i
                break

        print('informe a coordenada X inicial')
        novaCoordenadaX0 = float(input('>>'))
        
        print('informe a coordenada X final')
        novaCoordenadaX1 = float(input('>>'))

        print('informe a coordenada Y inicial')
        novaCoordenadaY0 = float(input('>>'))

        print('informe a coordenada Y final')
        novaCoordenadaY1 = float(input('>>'))

        print('informe a coordenada Z inicial')
        novaCoordenadaZ0 = float(input('>>'))

        print('informe a coordenada Z final')
        novaCoordenadaZ1 = float(input('>>'))

        calculos.corpos[aux].editarCorpo(
            novaCoordenadaX0, 
            novaCoordenadaX1, 
            novaCoordenadaY0, 
            novaCoordenadaY1, 
            novaCoordenadaZ0,
            novaCoordenadaZ1
        )
        
    elif(opcao == 4):
        if(len(calculos.corpos) < 1):
            os.system('cls') or None
            print ("Não existem corpos cadastrados para a simulação")
            continue

        print('informe o tempo para a translação')
        tempoSimulacao = float(input('>>'))

        print('informe a granulosidade')
        granulosidade = float(input('>>'))

        simulacao.insereAtributos(calculos, tempoSimulacao, granulosidade, categorias)

        print('deseja visualizar a simulacao?')  
        print('1-Sim 2-Não')
        try:
            desejaVisualizar = int(input('>>'))
        except:
            print("Insira apenas numeros por favor !")
            continue

        if(desejaVisualizar == 1):
            print(simulacao.executaSimulacao())
        
        print('deseja salvar a simulacao?')  
        print('1-Sim 2-Não')
        try:
            desejaSalvar = int(input('>>'))
        except:
            print("Insira apenas numeros por favor !")
            continue

        if(desejaSalvar == 1):
            print('informe o nome do arquivo')  
            nomeArquivo = input('>>').replace(" ", "")
            if(".txt" not in nomeArquivo):
                nomeArquivo += ".txt"
            
            simulacao.salvar(nomeArquivo)
            print("Simulação salva com sucesso!")

    elif(opcao == 5):
        print("Saindo do programa...")
        break
       
