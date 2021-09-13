import random

#Técnicas de Programação
#Atividade N1

#Grupo G16:
#Alunos: Guilherme Fernandes Mourão Maturana- RA: 21538078 / Guatavo Pinheiro - RA: 21526087/ Guilherme Cardozo - RA: 21574116

caminhoPv = 0  
sala = 1        
interacaoCam = 0  

while True: 
    if sala == 9 and interacaoCam <7:
        print("\nVocês completaram o labirinto com {} interações, você e sua guilda chegaram ao destino final, parabens!".format(interacaoCam))
        break
    elif sala == 9 and interacaoCam >= 7:
        print("\n\tVocê levou 7 ou mais interações para chegar na sala 9")
        print ("Você perdeu, tente novamente!")
        print ("Total de Interações: {}".format(interacaoCam))
        break
    else:
        print ("Você está na sala: {}".format(sala))    
        print ("Escolha seu caminho: ")
        print ("[1] - Caminho vermelho")
        print ("[2] - Caminho preto")
        caminhoPv = int(input())
        while caminhoPv <= 0 or caminhoPv >= 3:
            print("\nCaminho inválido!\n Você Deve escolher um caminho 'vermelho' ou 'preto'\n")
            print ("Você está na sala: {}".format(sala))    
            print ("Escolha seu caminho: ")
            print ("[1] - Caminho vermelho")
            print ("[2] - Caminho preto")
            caminhoPv = int(input())

        while caminhoPv == 1:
            interacaoCam += 1
            if sala == 6:
                print ("\nVocê está na sala: {}, portanto, a sala 6 só possui um caminho preto, que leva à sala 8.".format(sala))
                sala = 8
                caminhoPv = 0
            else:
                sala += 1
                caminhoPv = 0
                
        while caminhoPv == 2:
            interacaoCam +=1
            if sala == 6:
                print ("\nVocê está na sala: {}, portanto, a sala 6 só possui um caminho preto, que leva à sala 8.".format(sala))
                sala = 8
                caminhoPv = 0
            elif sala == 8:
                print ("\n\tNeste caminho escolhido, há um portal e você o atravessa.")
                print ("No entanto, o portal te teletransporta aleatoriamente para uma sala de número 1 a 5\n")
                sala = random.randint(1,5)
                caminhoPv = 0
            else:
                sala += 2
                caminhoPv = 0