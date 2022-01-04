import numpy as np
import re
import random
from read_file import FileOperator
import turtle

screen = turtle.getscreen()
turtley = turtle.Turtle()
DIRECTION = 0
LIVE = 40 #warunek stopu - ile iteracji wykona program

def return_dir():
    global DIRECTION
    if DIRECTION == 1:
        return "up"
    if DIRECTION == 2:
        return "down"

def set_direction(old, new):
    if new > old:
        return 1 #jak wieksze to do góyry
    else:
        return 2

def move_turtle():
    global DIRECTION
    if DIRECTION == 1:
        turtley.down()
        turtley.fd(10)
        turtley.up()
    else:
        turtley.down()
        turtley.bk(10)
        turtley.up()

def reset_live():#reset stopu
    global LIVE
    LIVE = 40

def return_min_waga(dane):
    min = 99
    for x in enumerate(dane):
        if x < min:
            min = x
    return min


def random_init(waga_max, dane, ile): #inicjalizacja losowych danych, podejście: sprawdzam x losowych przedmiotów i ładuje te które się mieszczą, nie zwracam uwagi na wagę
    tab = []
    waga_plecaka = 0
    i = 0
    random.shuffle(dane) #tasuję
    for _ in range(ile): #sprawdzam [ile] pierwszych przedmiotów mieści się
        if waga_plecaka + int(dane[i][1]) <= waga_max: #w plecaku
            tab.append(dane[i]) #wkładam przedmiot do plecaka
            waga_plecaka += int(dane[i][1]) #odnotowuje wzrost wagi plecaka
            i+=1

    while len(tab) < 1 or len(tab) < ile-2: #żeby nie pusty
        losowy = random.choice(dane)
        if waga_plecaka + int(losowy[1]) <= waga_max: #w plecaku
            tab.append(losowy)

    return tab, waga_plecaka #zwracam zawartość plecaka i jego wagę

def warunek_stop(): #warunek stopu
    global LIVE
    LIVE -= 1
    if LIVE == 0:
        return True
    return False

def zaznacz_pozycje(tabu, dane, sol): #ta funkcja zwraca numer indeksu danego przedmiotu sol - przedmiot, dane - baza przedmiotów
    for x, y in enumerate(dane):
        if y == sol:
                #tabu.append(x)
            return x
    return tabu

def sasiedzi(kandydat, pozycja, dane): #zwracam sąsiednie indeksy
    L = []
    if pozycja == 0:# jak 0 to nie zwróce -1, bo wyjdzie za tablice
        L.append(pozycja+1)
        return L
    if pozycja == len(dane)-1:
        L.append(pozycja-1) #analogicznie dla max
        return L
    L.append(pozycja+1)
    L.append(pozycja-1)
    return L

#w poniższej funkcji można dobudować potem dodatkowe przeliczniki
def fitness(obecny, kandydat, waga_max, waga):#kryterium dołączenia do tablicy, fitness prosty
    if int(kandydat[2]) >= int(obecny[2]):#jeśli kadydat jest droższy/ równy obecnemu, równy by uciec z optimum lokalnego
    #if kandydat[1] <= obecny[1]:#oraz jeśli waży tyle samo/mniej niż obecny
            return True #zwróc prawda - pasuje
    if (waga + int(kandydat[1])) <= waga_max: #lub jeżeli wagowo zmieści się w pozostałe w plecaku miejsce
        return True # to dorzucimy do plecaka
    return False

def NowyNajlepszySimple(najlepszy, kandydat):#najlepszy obiekt, opcja prosta
    if int(kandydat[2]) >= int(najlepszy[2]): #jeśli kadydat jest droższy/ równy obecnemu, równy by uciec z optimum lokalnego
        if (int(kandydat[1]) <= int(najlepszy[1]))\
            or ((int(kandydat[2]))/(int(kandydat[1])) >= (int(najlepszy[2]))/(int(najlepszy[1]))):##oraz jeśli waży tyle samo/mniej niż obecny lub ma lepszy przelicznik
            return True
    return False

def WarunekWyrzucenia(tabu, waga, waga_max):#warunki są na zewnątrz głównej funkcji, by móc je ulepszać w przyszłości
    if waga > waga_max:
        return True
    return False


def Tabu(init_sol, dane, waga_max):
    global DIRECTION
    przejscia_pasywne = 0 #łapiemy pierwszy obiekt z listy wstępnej jako punkt startowy
    check = 0
    najlepszy_obiekt = init_sol[0]
    najlepszy_kandydat = init_sol[0]
    pozycja = 0
    neighbours = []
    #tabu_list = [0 for _ in range(len(dane))]
    tabu_list = []
    tabu_list.append(init_sol[0]) #wrzucamy go do listy tabu
    waga = int(tabu_list[0][1])
    pozycja = zaznacz_pozycje(tabu_list, dane, sol = najlepszy_kandydat) #zaznaczam pozycje
    #print(tabu_list)
    while(not warunek_stop()): # dopoki nie warunek stopu
    #for _,y in enumerate(tabu_list):
        neighbours = sasiedzi(najlepszy_kandydat, pozycja, dane) #znajduje sąsiadów
        najlepszy_kandydat = dane[neighbours[0]] #łapię pierwszego lepszego jako kandydata
        DIRECTION = 2 #startujemy w dół
        for kandydat in neighbours: #i szukam najlepszego kandydata
            if (not dane[kandydat] in tabu_list) and (fitness(najlepszy_kandydat, dane[kandydat], waga_max, waga)):
                najlepszy_kandydat = dane[kandydat] #najlepszy kandydat do włożenia do plecaka
                new_pozycja = zaznacz_pozycje(tabu_list, dane, sol = najlepszy_kandydat) #zaznaczam pozycje
                DIRECTION = set_direction(pozycja, new_pozycja)
                pozycja = new_pozycja
                move_turtle()
        if  NowyNajlepszySimple(najlepszy_obiekt, najlepszy_kandydat): #sprawdzam, czy nowy kandydat nie jest może najlepszy
            najlepszy_obiekt = najlepszy_kandydat
        
        if (not najlepszy_kandydat in tabu_list):#sprawdzam czy kandydat jest w liście
            tabu_list.append(najlepszy_kandydat)#dodajemy najlepszego kandydata do plecaka
            waga += int(najlepszy_kandydat[1])#waga
            przejscia_pasywne = 0
            print(return_dir())
        else: #mechanizm przesuwający wskaznik kolejnego kandydata na kolejny z listy init
            if przejscia_pasywne > 3: #jeśli wiecej niż 3 razy wykona się algorytm i nic do plecaka nie doda
                check += 1
                if check >= len(init_sol):
                    check = 0
                najlepszy_kandydat = init_sol[check] #biorę następnego z listy wstępnej
                new_pozycja = zaznacz_pozycje(tabu_list, dane, sol = najlepszy_kandydat)
                DIRECTION = set_direction(pozycja, new_pozycja)
                pozycja = new_pozycja
                print(return_dir())
                move_turtle()
            przejscia_pasywne += 1 #liczę przejscia bez dodawania do plecaka

        if WarunekWyrzucenia(tabu_list, waga, waga_max):
            waga -= int(tabu_list[0][1])
            tabu_list.pop(0)#pierwszy element, niezależnie, czy najlepszy


    print("Stop")
    print("Plecak: \n", tabu_list)
    print()
    print("Najlepszy obiekt: \n",najlepszy_obiekt)
    print("-------------------")
    reset_live()
    return najlepszy_obiekt


def main():
    dane = FileOperator("TabuKnapsack") #ładuje obiekt
    dane.default() #ładuje domyślne dane
    
    waga_max = 23 #max waga plecaka, pamietać, żeby nie za mały min waga 2*ile_init-2 | >2
    waga = 0 #startowa waga

    ile_init = 3 #ile przedmiotów sprawdzić


    lista = []
    for _ in range(1): #10 razy algorytm
        init_solution, waga = random_init(waga_max, dane.get().tolist(), ile_init)#rozwiązanie wejściowe
        print("Rozwiązanie wstępne \n",init_solution)
        temp = Tabu(init_solution, dane.get().tolist(), waga_max)
        lista.append(temp)
    print("Najlepsze obiekty")
    print(lista)
    input("Press any key...")

if __name__ == "__main__":
    main()
