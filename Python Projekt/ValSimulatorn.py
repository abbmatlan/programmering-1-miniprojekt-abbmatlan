import random

# parti-skapning och röstnings uträkning per % -->
körIgen = True

while körIgen:        # En dictionairy per parti samlade i en lista
    partier = [
        {"vänster": True, "block": "Småpartierna", "namn": "Gröngölingarna", "partiledare": "Jonas Ostbåge",
         "min_röster": 3, "max_röster": 12, "röster": 0, "index": 0},
        {"vänster": True, "block": "Småpartierna", "namn": "Partikelpartiet", "partiledare": "Hans Majonäs",
         "min_röster": 2, "max_röster": 8, "röster": 0, "index": 1},
        {"vänster": False, "block": "Småpartierna", "namn": "Mälarpartiet", "partiledare": "Pernilla Godisgorilla",
         "min_röster": 8, "max_röster": 18, "röster": 0, "index": 2},
        {"vänster": False, "block": "Småpartierna", "namn": "Sjörövarpartiet", "partiledare": "Arja Samerrna",
         "min_röster": 3, "max_röster": 12, "röster": 0, "index": 3},
        {"vänster": False, "block": "Oljeblocket", "namn": "Extermisterna", "partiledare": "Lennart Lurig",
         "min_röster": 3, "max_röster": 6, "röster": 0, "index": 4},
        {"vänster": True, "block": "Oljeblocket", "namn": "Maskinpartiet", "partiledare": "Robert Rostbiff",
         "min_röster": 12, "max_röster": 22, "röster": 0, "index": 5},
        {"vänster": False, "block": "Oljeblocket", "namn": "Framtidspartiet", "partiledare": "Antwon Släp",
         "min_röster": 12, "max_röster": 18, "röster": 0, "index": 6},
        {"vänster": True, "block": "Inget", "namn": "Allpartiet", "partiledare": "Dan Dan",
         "min_röster": 20, "max_röster": 34, "röster": 0, "index": 7}
    ]

    for parti in partier:                            
        parti["röster"] = random.randrange(         # Skapar randomnummer med minsta/max värden i listan partier
            parti["min_röster"], parti["max_röster"], 1)

    i2 = 0
    sum = 0
    for partier[i2] in partier:
        sum += partier[i2]["röster"]        # lägger in de randomiserade värdena per parti under röster i listan partier
        i2 += 1
    
    if sum <= 100:              # kollar om rösterna för alla partier
        körIgen = False            # om summan av rösterna är över 100 är körigen = false och programmet går vidare
        print(100*"-")
        print(40*" "+"VAL 2020:")
        print(100*"-"+"\n")
        print(*" "+"Resultat")
        print( "I detta val röstade "+str(sum)+"% av befolkningen \n")      #printar antal%som röstade
        r = 0
        n = " "

for parti in partier:               # jämför parterna för att se vilket som är störst
    if parti["röster"] > r:        
        r = parti["röster"]         # den ersätter r med partits röster om det var sttörre än det förra
        n = parti["namn"]           # den gör samma sak med n som är en variabel för namnet av partiet
    else:
        continue

print(*" "+"PARTIET")
print( n+" var det mest gillade partiet med "+str(r)+"% av rösterna\n")     #printar vilket parti som var störst samt %

# Block uträkning -->
block = [0, 0, 0]                  # 0= Oljeblocket, 1= Småpartierna, 2= Inget
Småpartierna = []
Oljeblocket = []


for parti in partier:                # för varje parti med röster över 4% ska man kolla vilket block det tillhör
    if parti["röster"] < 4:
        continue
    else:                                        # här kollas block samt skrivs röster in det i respektive index i listan block
        if parti["block"] == "Oljeblocket":                 
            block[0] += parti["röster"]
            Oljeblocket.append(parti["partiledare"])
        elif parti["block"] == "Småpartierna":
            block[1] += parti["röster"]
            Småpartierna.append(parti["partiledare"])
        else:
            block[2] += parti["röster"]


personer = ""

OljeblocketLängd = len(Oljeblocket)      # justeringar av längden på listan oljeblocket för att kunnas användas i en print-funktion längre ned
L1och = int(OljeblocketLängd)-2
L2och = int(OljeblocketLängd)-1
counter = 0

SmåpartiernaLängd = len(Småpartierna)
L0och = int(SmåpartiernaLängd)-2
Loch = int(SmåpartiernaLängd)-1

print(*" "+"BLOCKET")

if block[0] > block[1]:              # jämför vilket block av oljeblocket och småpartinerna som är störst i röster från listan block
    if block[0] > block[2]:                   # om index 0 är störst kommer namnen på partiledarna i oljeblocket att skrivas ihop
        print( "Blocket som segra var Oljeblocket med " +
              str(block[0])+"% av rösterna")
        for name in Oljeblocket:
            if counter < L1och:
                personer += name+", "
            elif counter < L2och:             # om counter är x kommer programmet plussa till namn, "," och "och" till namnen för att printa en mening korrekt
                personer += name
            else:
                personer += " och "+name
            counter += 1
        print( "Partiledarna", personer,
              "är mycket nöjda med att Oljeblocket är de som ska styra  Sverige de kommande 4 åren.")       # printar uttalande för största blocket, fördjupning
    else:                                                                                                      
        print( "De två blocken som finns röstades ned med " +
              str(block[2])+"% av rösterna")  
        print( "Partiledaren", partier[7]["partiledare"], "är stolt med att", partier[7]["namn"],           # detta printas om partiet "Inget" är störst, fördjupning 
              "lyckades rösta ned de båda blocken med", partier[7]["röster"], "% och kommer att styra Sverige kammade 4 år.")

elif block[1] > block[2]:                                   # kollar om småpartierna, index 1 är större än parti "Iget" 
    print( "Blocket som segra var Småpartierna med " +
          str(block[1])+"% av rösterna")
    for name in Småpartierna:                 # om index 1 är störst kommer namnen på partiledarna i oljeblocket att skrivas ihop 
        if counter < L0och:
            personer += name+", "             # om counter är x kommer programmet plussa till namn, "," och "och" till namnen för att printa en mening korrekt
        elif counter < Loch:
            personer += name
        else:
            personer += " och "+name
        counter += 1
    print( "Partiledarna", personer,
          "är mycket nöjda med att Småpartierna är de som ska styra Sverige de kommande 4 åren.")    # uttalande för småparterna, fördjupning
else:
    print( "De två blocken som finns röstades ned med " +
          str(block[2])+"% av rösterna")
    print( "Partiledaren", partier[7]["partiledare"], "är stolt med att", partier[7]["namn"],        # uttalande för blocket "Inget", fördjupning
          "lyckades rösta ned de båda blocken med", partier[7]["röster"], "% och kommer att styra Sverige kammade 4 år.")


# Vänster och höger uträkning -->
inriktning = [0, 0]  # 0= Vänster  1= Höger
Vänster = []
Höger = []
x = 0
allvotes = len(partier)

for x in range(len(partier)):          # för varje parti kollar den om partit har mer än 4% 
    if partier[x]["röster"] < 4:
        continue
    else:                                      # programmet kollar den inrikning samt plussar på rösterna till höger/vänster
        if partier[x]["vänster"] == True:
            inriktning[0] += partier[x]["röster"]
            Vänster.append(partier[x]["partiledare"])
        else:
            inriktning[1] += partier[x]["röster"]
            Höger.append(partier[x]["partiledare"])
        x += 1
print(" ")
print(*" "+"INRIKNING")

personer1 = ""
VänsterLängd = len(Vänster)
L5och = int(VänsterLängd)-2         # justeringar av längden på listan vänster för att kunnas användas i en print-funktion nedan
L6och = int(VänsterLängd)-1
counter2 = 0

HögerLängd = len(Höger)
L3och = int(HögerLängd)-2
L4och = int(HögerLängd)-1

if inriktning[0] > inriktning[1]:          # kollar om väsntern, index 0 är större än högern
    print( "Vänstern vann med "+str(inriktning[0])+"% av rösterna.")
    for name in Vänster:
        if counter2 < L5och:
            personer1 += name+", "       # om counter2 är x kommer programmet plussa till namn, "," och "och" till namnen för att printa en mening korrekt
        elif counter2 < L6och:
            personer1 += name
        else:
            personer1 += " och "+name
        counter2 += 1
    print( "Partiledarna", personer1,
          "är mycket nöjda med att Vänstern är dominerande")    # uttalande från partiledarna i vänstern, fördjupning

elif inriktning[0] < inriktning[1]:                             # kollar om väsntern, index 0 är större än högern
    print( "Högern van med: "+str(inriktning[1])+"% av rösterna.")
    for name in Höger:
        if counter2 < L3och:
            personer1 += name+", "      # om counter2 är x kommer programmet plussa till namn, "," och "och" till namnen för att printa en mening korrekt
        elif counter2 < L4och:
            personer1 += name
        else:
            personer1 += " och "+name
        counter2 += 1
    print( "Partiledarna", personer1,
          "är mycket nöjda med att Högern är dominerande.")      # uttalande från partiledarna i högern, fördjupning

else:
    print( "Varken högern eller vänstern vann \n Vänstern:" +
          str(inriktning[0])+"% \n Högern"+str(inriktning[0])+".")

störstaröst = [0, 0, 0]
störstaindex = [0, 0, 0]
a = 0

for parti in partier:                    # med hjälp av listorna störstaröst, största index och a hittar man partiet som fick sörst antal röster
    for a in range(len(störstaindex)):

        if parti["röster"] >= störstaröst[a]:
            störstaröst.insert(a, parti["röster"])
            störstaindex.insert(a, parti["index"])               # if-satsen puttar bak det värdet som är mindre och tar bort det sista värdet i listan
            störstaindex.pop()
            störstaröst.pop()
            break

minstaröst = 100               # variabeln minsta röst måste vara höt i början annars kommer for-loopen inte köras pga för att alla patier är större än ex 0
minstaindex = 0

for parti in partier:                  # med hjälp av minstaröst och minsta index hittar man partiet som fick minst antal röster
    if minstaröst >= parti["röster"]:  #om partiets röster är mindre än minsraröst blir dett patri minstaröster
        minstaröst = parti["röster"]                                
        minstaindex = parti["index"]
    else:
        continue
print(" ")
print(100*"-")
print("\n Top 3 Störtsa Partier: \n")
print(partier[störstaindex[0]]["partiledare"], "är mycket nöjd att", partier[störstaindex[0]]
      ["namn"], "fick", partier[störstaindex[0]]["röster"], "% av rösterna och blev det största partiet.")
print(partier[störstaindex[1]]["partiledare"], "är mycket nöjd att",
      partier[störstaindex[1]]["namn"], "fick", partier[störstaindex[1]]["röster"], "%.")        #med hjälp av minstaindex och största index printas de sista uttalandena, fördjupning
print(partier[störstaindex[2]]["partiledare"], "är mycket nöjd att",
      partier[störstaindex[2]]["namn"], "fick", partier[störstaindex[2]]["röster"], "%.")
print(100*"-")
print("\n Minssta Partiet:\n")
print(partier[minstaindex]["partiledare"], "vill inte komentera på att", partier[minstaindex]
      ["namn"], "fick", partier[minstaindex]["röster"], "% och tog THE L...")
print(100*"-")

