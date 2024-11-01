# Zadanie rekrutacyjne AKAI

# Z podanego zbioru danych wyselekcjonuj 5 o największej wartości na jednostkę, znając kategorię obiektu
# Dane znajdują się w folderze "dane" w pliku "zbiór_wejściowy.json" oraz "kategorie.json"
# Wynik przedstaw w czytelnej formie na standardowym wyjściu


from json import load

#Wczytanie danych z plików
with open("dane/zbiór_wejściowy.json", "r", encoding="utf8") as plik:
    zbior_wejsciowy = load(plik)

with open("dane/kategorie.json", "r", encoding="utf8") as plik:
    kategorie = load(plik)

#Sortowanie
top_5 = sorted(kategorie, key=lambda x: x["Wartość za uncję (USD)"], reverse=True) [:5]

#Wyświetlanie
print("Oto 5 obiektów o najwyższej wartości na jednostkę:")
for obiekt in top_5:
    print(obiekt['Typ'], "(", obiekt['Czystość'], ")", " - ", obiekt['Wartość za uncję (USD)'], "USD")

