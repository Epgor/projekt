
def greed(max, input):
    tab = []
    i=0
    input.sort(reverse=True) #sortujemy malejąco
    for _, y in enumerate(input): #poruszając się po malejącej tablicy
        while(max >= y):#dopóki najmniejszy element>max
            max -= y#odejmij y od max
            i = i+1#zwiększ licznik o 1
        tab.append([y, i])#do tablicy para najwyższa opcja, ilosć użyć
        i = 0#zerujemy licznik
        if max < min(input):#jeśli max mniejszy niż najniższa opcja
            return max, tab #zwróć, reszta, użyte opcje


def ladny_print(macierz):#druk linia po linii
    for x in range(len(macierz)):
        print(macierz[x])


def main(
    ###opcje###
    max = 19, #max
    lista_opcji = [10, 5, 2, 1] #dostępne opcje wyboru
    ):#wywołanie, by mozna wywołąć funkcje z zewnątrz z parametrami
    ######################################
    answer = greed(max, lista_opcji)#wywołanie metody

    print("Wybrane opcje: \n opcja, ile razy")
    ladny_print(answer[1])
    print(f"Zużyto całą pulę ")\
        if answer[0] == 0 \
            else  print(f"Pozostało {answer[0]} punktów")


if __name__ == "__main__":
    main()