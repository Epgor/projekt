def greed(max, input):
    tab = []
    i=0
    input.sort(key = lambda input: input[3])
    for x,_ in reversed(list(enumerate(input))): #poruszając się po malejącej tablicy
        if(max >= int(input[x][1])):#jeśli suma wag nie przekracza
            max -= int(input[x][1])#odejmij y od max
            tab.append([input[x][0]])#do tablicy najwyższa opcja
    return max, tab


def ladny_print(macierz):#druk linia po linii
    for x in range(len(macierz)):
        print(macierz[x])


def main(
    
    ###opcje###
    max = 19, #max
    lista_opcji = [10, 5, 2, 1] #dostępne opcje wyboru
    ):#wywołanie, by mozna wywołąć funkcje z zewnątrz z parametrami
    ######################################
    '''
    answer = greed(max, lista_opcji)#wywołanie metody

    print("Wybrane opcje: \n opcja, ile razy")
    ladny_print(answer[1])
    print(f"Zużyto całą pulę ")\
        if answer[0] == 0 \
            else  print(f"Pozostało {answer[0]} punktów")
    '''

if __name__ == "__main__":
    main()