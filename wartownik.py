import random

def generuj_tablice(rozmiar, zakres_od, zakres_do):
    """
    Generuje tablicę liczb pseudolosowych.

    Argumenty:
    rozmiar - liczba elementów w tablicy
    zakres_od - dolny zakres wartości w tablicy
    zakres_do - górny zakres wartości w tablicy

    Zwraca:
    listę liczb pseudolosowych
    """
    return [random.randint(zakres_od, zakres_do) for _ in range(rozmiar)]

def przeszukaj_tablice_z_wartownikiem(tablica, wartosc):
    """
    Przeszukuje tablicę metodą z wartownikiem.

    Argumenty:
    tablica - tablica liczb całkowitych
    wartosc - szukana wartość

    Zwraca:
    indeks pierwszego wystąpienia wartości w tablicy
    lub -1, jeśli wartość nie występuje
    """
    n = len(tablica)
    tablica.append(wartosc)  # Dodanie wartownika na końcu tablicy
    i = 0

    while tablica[i] != wartosc:
        i += 1

    # Jeśli znaleziono wartownika, oznacza to brak wartości w tablicy
    return i if i < n else -1

def wyswietl_wynik(indeks, wartosc):
    """
    Wyświetla wynik przeszukiwania tablicy.

    Argumenty:
    indeks - indeks znalezionej wartości (lub -1)
    wartosc - szukana wartość
    """
    if indeks == -1:
        print(f"Element {wartosc} nie został odnaleziony w tablicy.")
    else:
        print(f"Element {wartosc} odnaleziony na indeksie: {indeks}.")

def main():
    """
    Główna funkcja programu.
    """
    # Parametry tablicy
    rozmiar_tablicy = 50
    zakres_od = 1
    zakres_do = 100

    # Generowanie tablicy
    tablica = generuj_tablice(rozmiar_tablicy, zakres_od, zakres_do)
    print("Wygenerowana tablica:")
    print(", ".join(map(str, tablica)))

    # Wczytanie wartości do wyszukania
    wartosc = int(input("\nPodaj wartość do wyszukania (1-100): "))

    # Przeszukiwanie tablicy
    indeks = przeszukaj_tablice_z_wartownikiem(tablica, wartosc)

    # Wyświetlenie wyniku
    wyswietl_wynik(indeks, wartosc)

if __name__ == "__main__":
    main()
