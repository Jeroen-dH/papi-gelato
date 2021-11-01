def stap2(aantalbollen):
    BakjeOfHorentje = input('Wilt u deze '+str(aantalbollen)+' bolletje(s) in A) een hoorntje of B) een bakje?: ')
    if BakjeOfHorentje == 'A'.lower():
        BakjeOfHorentje = 'bakje'
        stap3(aantalbollen,BakjeOfHorentje)
    elif BakjeOfHorentje == 'B'.lower():
        BakjeOfHorentje = 'horentje'
        stap3(aantalbollen,BakjeOfHorentje)
    else:
        print("Sorry dat snap ik niet...\n")
        stap2()

def stap3(aantalbollen, BakjeOfHorentje ):
    meerbestellen = input("Hier is uw "+ BakjeOfHorentje +" met " + str(aantalbollen) +" bolletje(s). Wilt u nog meer bestellen? (Y/N): ")
    if meerbestellen == 'Y'.lower():
        stap1()
    elif meerbestellen == 'N'.lower():
        print("Bedankt en tot ziens!")
    else:
        print("Sorry dat snap ik niet...\n")
        stap3()


def stap1():
    aantalbollen = int(input("Hoeveel bolletjes wilt u?: "))
    if aantalbollen >= int(9):
        print("sorry, maar u moet minder bollen kiezen\n")
        stap1()
    elif aantalbollen >= int(4):
        print("dan krijgt u van mij een bakje met",aantalbollen,"bollen.\n")
        BakjeOfHorentje = 'bakje'
        stap3(aantalbollen, BakjeOfHorentje)
    elif aantalbollen >= int(1):
        smaken(aantalbollen)
        stap2(aantalbollen)
    
    else:
        print("Sorry dat snap ik niet...\n")
        stap1()

def smaken(aantalbollen):
    a = 1
    while a <= int(aantalbollen):
        hoi = input(" welke smaak wilt u voor bolletje "+ str(a) +" ? Aardbei(a), chocolade(C), munt(m) of vanille(v).: ")
        a = a + 1
        if hoi != "A".lower() and hoi != "C".lower() and hoi != "M".lower() and hoi != "V".lower():
            print("sorry dit snap ik niet....")
            smaken(aantalbollen)

print("*\n*Welkom bij Papi Gelato.\n*")
stap1()

