aantalbollen = 0
horentje = 0
bakje = 0
liter = 0

def toppings(aantalbollen,BakjeOfHorentje):
    topping = input ("Wat voor topping wilt u: A) Geen, B) Slagroom, C) Sprinkels of D) Caramel Saus?")
    if topping == 'a':
        stap3(aantalbollen,BakjeOfHorentje,topping)
    elif topping == 'b':
        topping = 'slagroom'
        stap3(aantalbollen,BakjeOfHorentje,topping)
    elif topping == 'c':
        topping = 'Sprinkels'
        stap3(aantalbollen,BakjeOfHorentje,topping)
    elif topping == 'd':
        topping = 'Caramel Saus'
        stap3(aantalbollen,BakjeOfHorentje,topping)
    else: 
        print("Dat snap ik niet....")
        toppings(aantalbollen,BakjeOfHorentje)

def stap2(aantalbollen):
    BakjeOfHorentje = input('Wilt u deze '+str(aantalbollen)+' bolletje(s) in A) een hoorntje of B) een bakje?: ')
    if BakjeOfHorentje == 'B'.lower():
        BakjeOfHorentje = 'bakje'
        toppings(aantalbollen,BakjeOfHorentje)
    elif BakjeOfHorentje == 'A'.lower():
        BakjeOfHorentje = 'horentje'
        toppings(aantalbollen,BakjeOfHorentje)
    else:
        print("Sorry dat snap ik niet...\n")
        stap2(aantalbollen)

def stap3(aantalbollen, BakjeOfHorentje, topping):
    meerbestellen = input("Hier is uw "+ str(BakjeOfHorentje) +" met " + str(aantalbollen) +" bolletje(s). Wilt u nog meer bestellen? (Y/N): ")
    if meerbestellen == 'Y'.lower():
        stap1()
    elif meerbestellen == 'N'.lower():
        bonnetje(aantalbollen, BakjeOfHorentje, topping)
        print("Bedankt en tot ziens!")
    else:
        print("Sorry dat snap ik niet...\n")
        stap3(aantalbollen,BakjeOfHorentje,topping)


def stap1():
    bollen = input("Hoeveel bolletjes wilt u?: ")
    bollen2 = int(bollen)
    global aantalbollen
    aantalbollen += bollen2
    if aantalbollen >= int(9):
        print("sorry, maar u moet minder bollen kiezen\n")
        stap1()
    elif aantalbollen >= int(4):
        print("dan krijgt u van mij een bakje met",aantalbollen,"bollen.\n")
        BakjeOfHorentje = 'bakje'
        smaken(aantalbollen)
        stap3(aantalbollen, BakjeOfHorentje)
    elif aantalbollen >= int(1):
        smaken(aantalbollen)
        stap2(aantalbollen)
    
    else:
        print("Sorry dat snap ik niet...\n")
        stap1()






def begin():
    a = input("Ben u A. particulier of B. zakelijk? : ")
    if a == 'A'.lower():
        stap1()
    elif a == 'B'.lower():
        stapZ()
    else:
        print("Dat snap ik niet....")
        begin()

def smaken(aantalbollen):
    a = 1
    while a <= int(aantalbollen):
        hoi = input(" welke smaak wilt u voor bolletje "+ str(a) +" ? Aardbei(a), chocolade(C), munt(m) of vanille(v).: ")
        a = a + 1
        if hoi != "A".lower() and hoi != "C".lower() and hoi != "M".lower() and hoi != "V".lower():
            print("sorry dit snap ik niet....")
            smaken(aantalbollen)

def smaakzakelijk(liters):
    a = 1
    while a <= int(liters):
        hoi = input("Welke smaak wilt u voor liter " + str(a) + "Aardbei(a), chocolade(C), munt(m) of vanille(v).: ")
        if hoi != "A".lower() and hoi != "C".lower() and hoi != "M".lower() and hoi != "V".lower():
            print("sorry dit snap ik niet....")
            smaakzakelijk(liter)
        else: 
            a = a + 1

def stapZ():
    liters = input("\nHoeveel liters wilt u bestellen? : ")
    if liters >= '1':
        smaakzakelijk(liters)
        bonnetje2(liters)
    else:
        print("Sorry dat snap ik niet....\n")
        stapZ()

 

def bonnetje(aantalbollen, BakjeOfHorentje, topping):
    print("---------------","papi-gelato","---------------\n")
    if aantalbollen >= 1:
        print("Bolletjes       ", str(aantalbollen),"x €1.10    =", aantalbollen * 1.10)
    if BakjeOfHorentje == 'bakje':
        print("Bakje            1 x €0.75    =",1*0.75)
    elif BakjeOfHorentje == 'horentje':
        print("horentje         1 x €1.25    =",1*1.25)
    if topping == 'slagroom':
        print("topping          1 x €0.50    =",(1*0.50))
        print("                              ------- +\ntotaal                        =",(aantalbollen * 1.10 + 1.25 + 0.50) )
    elif topping == 'Sprinkels':
        print("topping          1 x €0.30    =",(1*0.50))
        print("                              ------- +\ntotaal                        =",(aantalbollen * 1.10 + 1.25 + 0.30) )
    elif topping == 'Caramel Saus':
        print("topping          1 x €0.90    =",(1*0.50))
        print("                              ------- +\ntotaal                        =",(aantalbollen * 1.10 + 1.25 + 0.90) )

def bonnetje2(liters):
    som = (float(liters) * 9.80)
    print("---------------","papi-gelato","---------------\n")
    print(liters + ". Liter         "+ liters + "x €9,80    =", (float(liters) * 9.80))
    print("                               ------- +\ntotaal                        =", som)
    print("BTW (9%)                      =", som/100*9)
    print("Bedankt en tot ziens!")
    
print("*\n*Welkom bij Papi Gelato.\n*")
begin()