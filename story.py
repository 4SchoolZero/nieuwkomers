def part36():
    print("Je valt in slaap \n [Goed einde]")
def part35():
    print("je beld aan bij zijn huis, hij doet open en begroet je na een lang gesprek bied hij je een slaapkamer aan")
    part36()
def part34():
    print("\nJe herinnert dat je nog een kennis heb in nederland")
    v22 = input("Ga je naar hem toe? y/n")
    if(v22 == "y"):
        part35()
    elif(v22 == "n"):
        part36()
    else:
        print("Weet je niet hoe je moet typen?")
def part33():
    print("Niemand neemt op...")
    part34()
def part32():
    print("Je word op je knieen gebracht en je word neergeschoten \n[slecht einde]")
    p = input("wilt u opnieuw? y/n")
    if(p == "y"):
        start()
    elif(p == "n"):
        start()
    else:
        print("Weet je niet hoe je moet typen?")
def partCall():
    v21 = input("Bel je je vader? y/n")
    if(v21 == "y"):
        part33()
    elif(v21 == "n"):
        part34()
    else:
        print("Weet je niet hoe je moet typen?")
def part31():
    print("Je loopt naar buiten en zoekt naar een plek om te slapen op straat, tijdens het zoeken zie je een telefoon hokje")
    partCall()
def part30():
    print("Je loopt naar je kamer en ziet een telefoon")
    partCall()
def part29():
    print("Je laat het mes vallen")
    v20 = input("Doe je je handen omhoog? y/n")
    if(v20 == "y"):
        part32()
    elif(v20 == "n"):
        part32()
    else:
        print("Weet je niet hoe je moet typen?")
def part28():
    print("Je rent op de linker bewaker af met je mes in je hand en steekt hem in zijn buik, de bewaker valt neer. De andere bewaker schiet maar mist en je steekt hem ook neer")
    v19 = input("Het alarm gaat af, ren je weg? y/n")
    if(v19 == "y"):
        part26()
    elif(v19 == "n"):
        part25()
    else:
        print("Weet je niet hoe je moet typen?")
def part27():
    print("Je blijft staan en je wordt vast gebonden samen met je vader, de volgende dag worden jullie allebij tot de doodstraf beoordeeld.. \n[slecht einde]")
    v = input("wilt u opnieuw? y/n")
    if(v == "y"):
        start()
    elif(v == "n"):
        start()
    else:
        print("Weet je niet hoe je moet typen?")
def part26():
    print("Je rent langs de bewakers naar de uitgang van het kamp! één van de bewaakers pakt een mes en steekt je neer... \n [Slecht einde]")
    y = input("wilt u opnieuw? y/n")
    if(y == "y"):
        start()
    elif(y == "n"):
        start()
    else:
        print("Weet je niet hoe je moet typen?")
def part25():
    print("Je loopt door de stad")
    part24()
def part24():
    print("Je komt aan bij een hotel")
    v18 = input("neem je een kamer? y/n")
    if(v18 == "y"):
        part30()
    elif(v18 == "n"):
        part31()
    else:
        print("Weet je niet hoe je moet typen?")
def part23():
    print("Je pakt het mes en houdt hem achter je rug, de bewakers staan nu voor jullie en commanderen om jullie handen omhoog te doen")
    part32()
def part22():
    print("Je pakt het mes en houdt hem achter je rug, de bewakers staan nu voor jullie en commanderen om jullie handen omhoog te doen")
    v17 = input("Steek je de bewakers neer?")
    if(v17 == "y"):
        part28()
    elif(v17 == "n"):
        part29()
    else:
        print("Weet je niet hoe je moet typen?")
def part21():
    print("Je blijft staan en je wordt vast gebonden samen met je vader, de volgende dag worden jullie allebij tot de doodstraf beoordeeld.. \n[slecht einde...]")
    q = input("wilt u opnieuw? y/n")
    if(q == "y"):
        start()
    elif(q == "n"):
        start()
    else:
        print("Weet je niet hoe je moet typen?")
def part20():
    print("je schiet op de bewakers, kogels vliegen overal heen. \n*klik* *klik*, bijde wapens waren op van jou en de bewakers.")
    v16 = input("Ren je weg? y/n")
    if(v16 == "y"):
        part26()
    elif(v16 == "n"):
        part27()
    else:
        print("Weet je niet hoe je moet typen?")
def part19():
    print("Je gaat met de boot naar nederland, je komt aan bij de haven")
    v15 = input("Neem je de taxi? y/n")
    if(v15 == "y"):
        part24()
    elif(v15 == "n"):
        part25()
    else:
        print("Weet je niet hoe je moet typen?")
def part18():
    print("Je komt aan op schiphol")
    v14 = input("Neem je de taxi? y/n")
    if(v14 == "y"):
        part24()
    elif(v14 == "n"):
        part25()
    else:
        print("Weet je niet hoe je moet typen?")
def part17():
    print("Je doet het mes in je broekzak en loopt naar de uitgang, 2 bewakers zien jullie en lopen met hun zaklampen naar jullie toe")
    v13 = input("Pak je het mes? y/n")
    if(v13 == "y"):
        part22()
    elif(v13 == "n"):
        part23()
    else:
        print("Weet je niet hoe je moet typen?")
def part16():
    print("Je pakt het pistool vast en loopt door naar de uitgang, 2 bewakers zien jullie en je richt je pistool op de bewakers")
    v12 = input("schiet je? y/n")
    if(v12 == "y"):
        part20()
    elif(v12 == "n"):
        part21()
    else:
        print("Weet je niet hoe je moet typen?")
def part15():
    print("Je kiest om naar Nederland te reizen")
    v11 = input("Neem je het vliegtuig?")
    if(v11 == "y"):
        part18()
    elif(v11 == "n"):
        part19()
    else:
        print("Weet je niet hoe je moet typen?")
def part14():
    print("Je herinnerd dat je iemand kent in nederland dus besluit toch naar nederland te gaan")
    part15()
def part13():
    print("je valt in slaap, de volgende dag zie je dat je vader is gevangen door de taliban na de ontsnappings poging hij krijgt de doodstraf...\n [Slecht einde..]")
    z = input("wilt u opnieuw? y/n")
    if(z == "y"):
        start()
    elif(z == "n"):
        start()
    else:
        print("Weet je niet hoe je moet typen?")
def part12():
    print("Om 3 uur in de nacht halen jullie allebij de bewaker neer hij heeft 2 dingen bij zich")
    v10 = input("neem je het pistool? y/n")
    if(v10 == "y"):
        part16()
    elif(v10 == "n"):
        part17()
    else:
        print("Weet je niet hoe je moet typen?")
def part11():
    print("Je bent bij de grens aangekomen")
    v9 = input("Ga je naar turkijë? y/n")
    if(v9 == "y"):
        part14()
    elif(v9 == "n"):
        part15()
    else:
        print("Weet je niet hoe je moet typen?")
def part10():
    print("Je wordt in een cell gezet met je vader, hij heeft een ontsnappings plan")
    v8 = input("Volg je zijn plan?")
    if(v8 == "y"):
        part12()
    elif(v8 == "n"):
        part13()
    else:
        print("Weet je niet hoe je moet typen?")
def part9():
    print("Je vlucht uit het kamp zonder gezien te worden, je weet nog wat je vader zei:'Naar het noorden'. je ziet een paard.")
    v7 = input("neem je het paard? y/n")
    if(v7 == "y"):
        part11()
    elif(v7 == "n"):
        part11()
    else:
        print("Weet je niet hoe je moet typen?")
def part8():
    print("Je komt aan bij hun kamp, er zijn andere vluchtelingen hier. Je ziet een opening om te vluchten")
    v6 = input("Ren je weg? y/n")
    if(v6 == "y"):
        part9()
    elif(v6 == "n"):
        part10()
    else:
        print("Weet je niet hoe je moet typen?")
def part7():
    print("je probeert de tyraps door te knippen met een nagelschaartje die op de grond lag")
    print("Het vaalt en je wordt gesnapt door 1 van de taliban...")
    part8()
def part6():
    print("je richt je wapen op de taliban en schiet. BAM, BAM, BAM! 3 Kogels worden afgevuurd door je pistool, de 2 taliban vallen allebij op de grond van de pijn. Je dacht dat het over was maar 1 van de 2 taliban pakte zijn pistool en schoot op jou, BAM! Alles wordt wazig en je valt van het paard af. Je bent geraakt in je nek door de kogel, je bent dood…  [slecht einde2]")
    x = input("wilt u opnieuw? y/n")
    if(x == "y"):
        start()
    elif(x == "n"):
        start()
    else:
        print("Weet je niet hoe je moet typen?")
def part5():
    print("Je rent weg van de taliban maar hierdoor schieten ze je dood [slecht einde1]")
    y= input("wilt u opnieuw? y/n")
    if(y == "y"):
        start()
    elif(y == "n"):
        start()
    else:
        print("Weet je niet hoe je moet typen?")
def part4():
    print("Je zegt dat ze hun handen omhoog moeten doen. Op dat moment richten de andere 2 taliban hun geweren op jou en dreigen te schieten, je realiseert dat het nuteloos is en stapt van je paard af. Je legt je wapen neer en stapt van je paard af en doet je handen omhoog. De taliban pakken tyraps en binden onze handen vast.")
    print("We zitten in de auto en het is donker")
    v5 = input("knip je de tyraps door?")
    if(v5 == "y"):
        part7()
    elif(v5 == "n"):
        part8()
    else:
        print("Weet je niet hoe je moet typen?")
def part3():
    print("Je schiet, hij raakt de taliban en hij valt naar de grond. De 2 andere taliban pakken hun wapens en richten ze op jou, je vader schreeuwt om weg te rennen met het paard.")
    v4 = input("Ren je weg? y/n")
    if(v4 == "y"):
        part5()
    elif(v4 == "n"):
        part6()
    else:
        print("Weet je niet hoe je moet typen?")
def part2():
    v3 = input("Dreig je met het pistool? y/n")
    if(v3 == "y"):
        part4()
    elif(v3 == "n"):
        part3()
    else:
        print("Weet je niet hoe je moet typen?")
def part1():
    print("Je loopt naar buiten en stapt achter op het paard van je vader, er zijn meer mensen. Hij kijkt je aan en laat een pistool zien, “Hier, gebruik het alleen als er geen andere optie is” zegt je vader.")
    v2 = input("Pak het pistool? y/n")
    print("3 uur later en we zijn bijna bij de grens, toen hoorde wij een auto aankomen. Het waren de taliban! Ze waren sneller dan ons en stopte voor onze groep. Je vader wordt vast gepakt met een pistool naar zijn hooft, ze dreigen hem te schieten als wij niet van het paard af stappen.")
    if(v2 == "y"):
        part2()
    elif(v2 == "n"):
        part3()
    else:
        print("Weet je niet hoe je moet typen?")
def start():
    print("\n Om 3 uur in de nacht wordt je wakker gemaakt door je vader, je moet meteen opstaan en vluchten naar de grens.")
    v1 = input("Knuffel of Familie foto?")
    if(v1 == "knuffel"):
        part1()
    elif(v1 == "familie foto"):
        part1()
    else:
        print("Weet je niet hoe je moet typen?")
start()