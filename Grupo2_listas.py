#01)
def addElementos():
    import random
    lista = []
    for i in range(0,10,1):
        n = random.randint(1,52)
        lista.append(n)
    print (lista)
addElementos()

#------------------------------------------------------------------------------------------------------
#04)
def SO(self):
    print("Qual o melhor Sistema Opera'cional para uso de servidores? ")
    print("As possíveis respostas são:")
    lista_so = ["1 - Windows Server","2 - Unix","3 - Linux","4 - Netware","5 - Mac OS","6 - Outros" ]
    lista_notas = []
    lista_porcento = []
    somatotal = 0

    for x in range(len(lista_so)):
        print(f'{lista_so[x]}')
        nota = int(input(f"Digite o a quantidade de votos do SO {lista_so[x]} "))
        print("\n")
        if nota == 0:
            print("=-"*15,"\n","  O prpograma foi encerrado.\n","-="*15)
            break
        lista_notas.append(nota)
        somatotal += nota
    for x in range(len(lista_notas)):
        porcetagem = (lista_notas[x]*100)/somatotal
        lista_porcento.append(round(porcetagem))
        nota_max = max(lista_notas)
        id_max = lista_notas.index(nota_max)
    print('\n')
    print('Sistema Operacional',' '*5,'Votos',' '*3,'%')
    print('-'*19,' '*5,'-'*5,' '*3,'-'*3)
    print(f'{lista_so[0]}'+' '*11+f'{lista_notas[0]}'+' '*5+f'{lista_porcento[0]}%')
    print(f'{lista_so[1]}'+' '*21+f'{lista_notas[1]}'+' '*5+f'{lista_porcento[1]}%')
    print(f'{lista_so[2]}'+' '*20+f'{lista_notas[2]}'+' '*5+f'{lista_porcento[2]}%')
    print(f'{lista_so[3]}'+' '*18+f'{lista_notas[3]}'+' '*5+f'{lista_porcento[3]}%')
    print(f'{lista_so[4]}'+' '*19+f'{lista_notas[4]}'+' '*5+f'{lista_porcento[4]}%')
    print(f'{lista_so[5]}'+' '*20+f'{lista_notas[5]}'+' '*5+f'{lista_porcento[5]}%')
    print('-'*19,' '*5,'-'*5,' '*3,'-'*3)
    print(f'Total'+' '*22+f'{somatotal}\n')
    print(f'O Sistema Operacionl mais votado foi o {lista_so[id_max]}, com {nota_max} votos, correspondendo a {lista_porcento[id_max]}% dos votos.')
