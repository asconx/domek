import random

tab = []

def tablica():
    for _ in range(50):
        ran = random.randint(0, 100)
        tab.append(ran)

tablica()


def szukaj():
    dlugosc_tab = len(tab)
    szukana = int(input("Podaj liczbę do wyszukania: "))

    # Dodanie wartownika
    tab.append(szukana)

    # Przeszukiwanie tablicy
    i = 0
    while tab[i] != szukana:
        i += 1

    # Usunięcie wartownika
    tab.pop()

    # Sprawdzenie wyniku
    if i < dlugosc_tab:
        print("Znaleziono liczbę w tablicy! indeks to: ",i)
        print(tab)
    else:
        print("Nie znaleziono liczby w tablicy.")
        print(tab)

szukaj()