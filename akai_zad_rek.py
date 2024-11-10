# Zadanie rekrutacyjne AKAI

# Z podanego zbioru danych wyselekcjonuj 5 o największej wartości na jednostkę, znając kategorię obiektu
# Dane znajdują się w folderze "dane" w pliku "zbiór_wejściowy.json" oraz "kategorie.json"
# Wynik przedstaw w czytelnej formie na standardowym wyjściu


from json import load

#Wczytanie danych z plików
with open("dane/zbiór_wejściowy.json", "r", encoding="utf8") as plik:
    zbior_wejsciowy = load(plik)
#print(zbior_wejsciowy)

with open("dane/kategorie.json", "r", encoding="utf8") as plik:
    kategorie = load(plik)
#print(kategorie)

kategorie_map = {}
for kat in kategorie:
    typ = kat["Typ"]
    czystosc = kat["Czystość"]
    wartosc = kat["Wartość za uncję (USD)"]
    kategorie_map[(typ, czystosc)] = wartosc

#Obliczenia
CT_TO_OUNCE = 0.00705479239
G_TO_OUNCE = 0.0352739619
def przelicz(masa):
    if "ct" in masa:
        return float(masa.replace("ct","").replace(",","."))*CT_TO_OUNCE
    elif "g" in masa:
        return float(masa.replace("g","").replace(",","."))*G_TO_OUNCE
    return 0

#Lista obiektów 
zb_wejsciowy_wartosci = []

for ob in zbior_wejsciowy:
    typ = ob["Typ"]
    masa = ob["Masa"]
    czystosc = ob["Czystość"]
    wartosc_na_jednostke = kategorie_map.get((typ, czystosc))
                                             

    if wartosc_na_jednostke:
        masa_jednostka = przelicz(masa)
        wartosc_koncowa = masa_jednostka * wartosc_na_jednostke
        zb_wejsciowy_wartosci.append({
            "Typ": typ,
            "Czystość": czystosc,
            "Właściciel": ob["Właściciel"],
            "Wartość (USD)": wartosc_koncowa,
            "Barwa": ob["Barwa"],
            "Pochodzenie": ob["Pochodzenie"]
        })

#Sortowanie
top_5 = sorted(zb_wejsciowy_wartosci, key=lambda x: x["Wartość (USD)"], reverse=True) [:5]

#Wyświetlanie
print("Oto 5 obiektów o najwyższej wartości na jednostkę:")
for ob in top_5:
    print("Typ:", ob['Typ'], " Czystość:", ob['Czystość'], " Właściciel:", ob['Właściciel'], " Barwa:", ob['Barwa'], " Pochodzenie:", ob['Pochodzenie'], " Wartość (USD):", ob['Wartość (USD)'])

