#tõlgitud eesti keelde
print("*** NUMBRIDEGA MÄNGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = abs(int(input("Sisestage täisarv => "))) #eemaldatud ja lisatud sulgud
        break
    except ValueError:
         print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole mõtet midagi peale hakata")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, kui palju paaris ja mitu paaritu numbrit on arvus")
    print()
    c=b=a # vähendas võrdusmärkide arvu
    paaris=0 # vähendas võrdusmärkide arvu
    paaritu=0 # vähendas võrdusmärkide arvu
    while b > 0: #muutunud ; on :, ja pane "IF" tsüklisse
        if b % 2 == 0: # lisatud =
            paaris += 1 #vahetas märgid ära
        else:
            paaritu += 1 #vahetas märgid ära
        b = b // 10 #välja võetud kaustast "ELSE"
    print("Paarisarvud:", paaris) #lisatud ,
    print("paarituid numbreid:", paaritu) #lisatud ,
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Pöörake * sisestatud number")
    print()
    b=0
    while a > 0: #lisatud :
        number = a % 10
        a = a // 10
        b = b * 10
        b += number #vahetas märgid ära ja sisestatud "WHILE"
    print("*Tagurpidi* number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Syracuse hüpoteesi testimine") #eemaldatud lisasulud
    print()
    if c % 2 == 0: #lisatud =
        print("с - paarisarv. Jagage poolt 2.")
    else:
        print("с - paaritu number. Korrutage 3-ga, lisage 1 ja jagage 2-ga.")
    while c != 1:
            if c % 2 == 0: #lisatud =
                    c = c / 2 #eemaldatud =
            else:
                    c = (3*c + 1) / 2 #eemaldatud =
            print(c, end=" ") #lisas "
    print()
    print("Hüpotees on õiges") #muutis "