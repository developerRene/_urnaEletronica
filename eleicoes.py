import os
#implantando a qtde de aptos a votar.
#adicionado a constante lim para fazer funcionar o for-in.
#Excluído a opção 99 (finalizar) que funcionava no while.
print("="*32)
print("---------- CANDIDATOS ----------")
print("12.Ciro | 13.Lula | 22.Bolsonaro")
print("="*32)

aptos = int(input("Quantidade de aptos a votar:"))
print("-"*32)

votaram = 0
lim = (aptos-votaram)
voto = int
vciro = 0
vlula = 0
vbozo = 0
vnulo = 0

for lim in range(votaram, aptos):

    voto = int(input("Vote: "))

    if voto == 12:
        vciro = vciro + 1
        votaram = votaram + 1
        print("Ciro Gomes | Voto confimado!")
        os.system("cls")
    elif voto == 13:
        vlula = vlula + 1
        votaram = votaram + 1
        print("Lula da Silva | Voto confimado!")
        os.system("cls")
    elif voto == 22:
        vbozo = vbozo + 1
        votaram = votaram + 1
        print("Jair Bolsonaro | Voto confimado!")
        os.system("cls")
    elif voto != 12 and voto != 13 and voto != 22:
        vnulo = vnulo + 1
        votaram = votaram + 1
        print("Voto Nulo | Voto confimado!")
        os.system("cls")

print("TOTALIZAÇÃO DOS VOTOS")
print(f"Ciro Gomes......: {vciro} votos {(vciro/votaram)*100:.2f}%")
print(f"Lula da Silva.....: {vlula} votos {(vlula/votaram)*100:.2f}%.")
print(f"Jair Bolsonaro..: {vbozo} votos {(vbozo/votaram)*100:.2f}%.")
print(f"Nulo............: {vnulo} votos {(vnulo/votaram)*100:.2f} %.")
#print(f"O resultado é: {variavel:.2f} ")
#print(f"Ciro Gomes......: {} votos {((vciro/votaram)*100):.2f} %.")