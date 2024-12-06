import random

tab =[]

def tablica():
    i = 0
    

    while i < 50:
        ran =  random.randint(0,100)
        tab.append(ran)
        i+=1

tablica()

print(tab)


def szukaj():
   dlugosc_tab = len(tab)
   szukana = int(input("szukana liczba"))

   tab.append(szukana)

   for char in range(dlugosc_tab):
       if tab[char] == szukana and  tab[dlugosc_tab] == szukana:
           
          print("Znaleziono liczbę w tablicy!")
       else:
        print("Nie znaleziono liczby w tablicy.")

szukaj()
       

   

      