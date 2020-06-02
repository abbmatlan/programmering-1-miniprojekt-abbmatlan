# Tekniklektioner
#2020-03-23
## Legobil:
Idag tog jag ned färdig kod för hemsidan och mikrokontrollen. Jag ändrade i båda koderna så att de skulle vara kompatibla med varandra och sedan kopplade ihp dem. En del av tiden gick åt att koppla ihop min egna MQTT med de bårda partnerna och felsöka i processen.

## Python projekt:
Jag fortsatte med min dictionairy och kan nu hämta siffror för partiernas max-min antal röster och använda dem i mina tot röster för partierna.

## Nästa lektion:
Jag tänker fortsätta med Python och hantering av min dictinairy.

----------------------------------------------------------------------------------------------------------------------------------------

#2020-03-24
## Legobil:
Idag ändrade jag lite i hemsida-koden i Visual studio Code för att det skulle vara mera "användarvänligt".

## Python projekt:
Jag fortsatte med att skapa loopar för hantering av informationen i min dictionairy. Jag trodde jag skulle bli klar med alla funktioner så jag kunde börja fokusera på en mer effektiv kod, men stötte på ett okänt fel. 

## Nästa lektion:
Jag vill fortsätta och eventuellt bli klar med grunfunktionerna i Python-projektet. Efter det kan jag fokusera på bilen.

----------------------------------------------------------------------------------------------------------------------------------------

#2020-03-31
## Legobil:
Idag började jag ändra i hemsida-koden i Visual studio Code för att för att skapa en ny design som jag tycker så bra ut. De första två passen lekte jag runt och planerade hur jag ville ha den samt försökte att skriva om koden till det. Jag stötte tyvärr in i så mycket problem så det sista passe kopierade jag våran ganlma lamp-kod till expectrumhemsidan som jag har skapadt. Jag kommer använda den layouten som grund och lägga in componenter till bilen från min andra kod.

## Nästa lektion:
Jag vill fortsätta och eventuellt bli klar med grunfunktionerna i Python-projektet. Jag ska fortsätta med hemsidan för bilen.

----------------------------------------------------------------------------------------------------------------------------------------
# Driverbot
Projektet handlar om en handbyggd lego-bil konstuerad av tekniklego. Bilen ska kunnas köras från en hemsida och på denna ska man kunna ange fram, bak, hastighet och svängning. Detta gör bilen elektroniskt med ett Arduinokort och motorer. Motorerna styrs med kortet som sedan är laddad med drivrutiner. Dessa är mikroprosessorkoden vilket kommunicerar med MQTT och då samtidigt hemsidan. Allt detta görs via olika koder eller "medelanden" som skickas från hemsidan hela vägen till Arduino. Meddelandena kan exempel vara F500 som tas in och omvandlas till "framåt" med hastigheten "500".

## Planering
Min planering består av en Psuedo-kod som ligger på startsidan och heter "psuedoKOD-driverbot.dock" Där kan man hitta ett enkelt överlag på vad jag förväntas att ha med samt mina egna krav på hemsidan och porjektet. Denna är också markerad med röd/grön för att man tydligt ska kunna se vad som är uppnått och inte.

## Utvärdering

### Det jag hade gjort annorlunda:
Sett till så att anpasningen av komponenterna fungerade bättre. Jag hade lekt med ett batteri och försökt få det att fungera. Jag hade fyllt upp alla mina views med den information/funktion som ska finnas. I min mikroprossesorkod hade jag testat att mixtra med övergångarna mellan frm och bak med något typ av räkningsprogramm. Det sista jag hade gjort skulle vart utbyggnad på bilen med någon siren/lampa eller annan funktion. Denna hade jag då också behövt skriva arduinokod för samt sätta in på "settings"-viewn vilket man kommer åt på startsidan.

### Problem jag stötte på:
Det fanns några problem jag stötte på under arbetandet:

1. Koppla ihop allt, jag var tvungen att ändra lite i VisualStudioCode med t.ex. vart i MQTT:n värdena som den tog imot skulle skrivas ut.

2. Att flytta över alla komopnenter 8frn Jockes kod) och använda dem i min kod var lite kronligt då många saker som sökvägar osv inte fungerade, men det löste sig med lite kodgranskning och felsökning.

3. I min "drive"-view var de readn existerande iconerna för att svänga osv inte kompatibla med vue utan attjag behövde lada ned en funktionn till det. Detta fick mig att vända mitt till vuetifys egna mdi-icons som löste problemet.

4. Mina mdi-icons som fanns i drive ville inte lägga sig rätt i mitt kort. Jag höll på en länngre srund med detta för att hitta den rätta placeringsmetoden som tillslut blev margins och colums. 

### Hur gick det?
Det gick rätt så bra! 
Jag lyckades med mitt övergripande mål, vilket var att göra en mer användarvänlig hemsida som hade samma funktionsmängd bara att hemsidan var byggd efter min layout och är enkel att bygga vidare på i framtiden.
