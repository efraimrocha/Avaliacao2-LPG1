#02) 
def NotaZerodez():
    f = True
    while f:
        n = int(input("Digite um valor entre 0 e 10. "))
        if 0 <= n <= 10:
            print(f'Você  valor entre 0 e 10.\nO programa será encerrado\nFIM')
            f = False
            break
        else:
            continue
NotaZerodez()

#04)
def Contador(self):
    s = 0
    while True:
        s = s + 1
        print(s)
        if s == 10:
            break
Contador()
