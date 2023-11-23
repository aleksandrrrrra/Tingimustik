#Esimene ülesanne
name=input("Teie nimi on Juku?: ")
if name == "jah" or name=="да" or name=="yes" or name=="da".lower():
    print("Lähme kinno!!")
    vanus =int(input("Sisestage vanus: "))
    if  vanus < 0 or vanus > 100:
        print("Viga: sisestage kehtiv vanus.")
    if vanus < 6:
        print("Juku, su pilet on tasuta.")
    if 6 <= vanus <= 14:
        print("Juku, sul on vaja lapsepiletit.")
    if 15 <= vanus <= 65:
        print("Juku, sul on vaja täispiletit.")
    elif vanus >65 and vanus < 100:
        print("Juku, sul on sooduspiletit vaja.")
else:
    print("Sa ei ole mu sõber :c")

#Teine ülesanne
name1 = input("Sisestage esimese inimese nimi: ")
name2 = input("Sisestage teise inimese nimi: ")

if name1 and name2:
    print(f"{name1} ja {name2} nad on täna pinginaabrid")
else:
    print("Sisestage mõlema inimese õiged nimed.")

#Kolmas ülesanne
pikkus = float(input("Sisestage ruumi pikkus meetrites: "))
laius = float(input("Sisestage ruumi laius meetrites: "))

põranda_pindala = pikkus * laius

print(f"Ruumi põrandapind: {põranda_pindala} ruutmeetrit")

valik = input("Kas soovite teha renoveerimistöid? (jah/ei): ").lower()

if valik == "jah":
    kulu_ruutmeetri_kohta = float(input("Sisesta ruutmeetri hind: "))
    summa = kulu_ruutmeetri_kohta * põranda_pindala
    print(f"Põranda vahetuse kogumaksumus: {summa} eurot")
else:
    print("Tänan teid vastuse eest. Kui soovite tulevikus remonti teha, võtke meiega ühendust.")

#Neljas ülesanne
hind = float(input("Sisesta alghind:"))

if hind > 700:
    soodus = 0.3  
    soodushind = hind * (1 - soodus)

    print(f"Hind 30% allahindlusega: {soodushind} eurot")
else:
    print("Hind ei ületa 700 eurot, allahindlust ei kohaldata.")

#Viies ülesanne
temperatuur = float(input("Sisestage temperatuur:"))

if temperatuur > 18:
    print("Temperatuur on üle kaheksateist kraadi.")
else:
    print("Temperatuur ei ületa kaheksateist kraadi.")

#Kuues ülesanne
pikkus = float(input("Sisestage inimese pikkus sentimeetrites: "))
lühike = 150
pikk = 180

if pikkus < lühike:
    print("Lühike pikkus.")
elif lühike <= pikkus < pikk:
    print("Keskmine pikkus.")
else:
    print("Kõrge pikkus.")

#Seitsmes ülesanne
pikkus = float(input("Sisestage inimese pikkus sentimeetrites: "))
sugu = input("Sisestage isiku sugu (m/n): ").lower()

lühike_piir_mees = 165
pikk_piir_mees = 190
lühike_piir_naine = 150
pikk_piir_naine = 175

if sugu == "m":
    if pikkus < lühike_piir_mees:
        print("Mees on lühike.")
    elif lühike_piir_mees <= pikkus < pikk_piir_mees:
        print("Mehe keskmine pikkus.")
    else:
        print("Mees on pikk.")
elif sugu == "n":
    if pikkus < lühike_piir_naine:
        print("Naine on lühike.")
    elif lühike_piir_naine <= pikkus < pikk_piir_naine:
        print("Naise keskmine pikkus.")
    else:
        print("Naine on pikk.")
else:
    print("Sugu sisestati valesti. Sisestage 'm' meeste jaoks või 'n' naiste jaoks.")

#Kaheksas ülesanne 
piima_hind = 2.5
saia_hind = 1.0
leiba_hind = 1.5

on_vaja_piima = input("Kas soovite piima osta? (jah/ei): ").lower()

on_vaja_leiba = input("Kas soovite leiba osta? (jah/ei): ").lower()

on_vaja_saia = input("Kas soovite saia osta? (jah/ei): ").lower()

summa = 0

if on_vaja_piima == 'jah':
    summa += piima_hind

if on_vaja_leiba == 'jah':
    summa += leiba_hind

if on_vaja_saia == 'jah':
    summa += saia_hind

print(f"Teie ostude kogumaksumus: {summa} eurot.")

#Üheksas ülesannne
külg_1 = float(input("Sisestage esimese külje pikkus: "))
külg_2 = float(input("Sisestage teise külje pikkus: "))
külg_3 = float(input("Sisestage kolmanda külje pikkus: "))
külg_4 = float(input("Sisestage neljanda külje pikkus: "))

if külg_1 == külg_2 == külg_3 == külg_4:
    print("See on ruut.")
else:
    print("See ei ole ruut.")

#Kümnes ülesanne
arv_1 = float(input("Sisestage esimene number: "))
arv_2 = float(input("Sisestage teine ​​number: "))

toiming = input("Valige toiming (+, -, *, /): ")

if toiming == '+':
    tulemus = arv_1 + arv_2
    print(f"Lisamise tulemus: {tulemus}")
elif toiming == '-':
    результат = arv_1 - arv_2
    print(f"Lahutamise tulemus: {tulemus}")
elif toiming == '*':
    tulemus = arv_1 * arv_2
    print(f"Korrutamise tulemus: {tulemus}")
elif toiming == '/':
  
    if arv_2 != 0:
        tulemus = arv_1 / arv_2
        print(f"Jagamise tulemus: {tulemus}")
    else:
        print("Viga: Ei saa nulliga jagada.")
else:
    print("Viga: vale tegevus. Valige +, -, *, /.")

#11 ülesanne
from datetime import datetime

sünnikuupäev = input("Sisestage oma sünnikuupäev vormingus PP-KK-AAAA: ")

sünnikuupäev = datetime.strptime(sünnikuupäev, "%d-%m-%Y")

praegune_kuupäev = datetime.now()

if praegune_kuupäev.month == sünnikuupäev.month and praegune_kuupäev.day == sünnikuupäev.day:
    print("Palju õnne sünnipäevaks! See on teie aastapäev!")
else:
    print("Täna pole teie aastapäev.")

#12 ülesanne
