import random


def czy_mamy_zwyciesce(lista):
    lista.sort()
    poczatek_poziom=[1,4,7]
    poczatek_pionowo=[1,2,3]
    for liczby in lista:
        if liczby in poczatek_poziom:
            index = lista.index(liczby)
            try:
                if (lista[index]+1) == lista[index+1] and lista[index+1]+1 == lista[index+2]:
                    return True
            except Exception as e:
                print(e)

    for liczby in lista:
        if liczby in poczatek_pionowo:
            index = lista.index(liczby)
            try:
                if (lista[index]+3) == lista[index+1] and lista[index+1]+3 == lista[index+2]:
                    return True
            except Exception as e:
                print(e)
    if 3 in lista and 5 in lista and 7 in lista:
        return True
    if 1 in lista and 5 in lista and 9 in lista:
        return True


def wytwornia_list():
    miejsce={}
    for i in range (1,11):
        miejsce[i] = " "

    return miejsce


def draw_move(lista):

    board=f'''
    +-------+-------+-------+
    |       |       |       |
    |   {pm(1,lista)}   |   {pm(2,lista)}   |   {pm(3,lista)}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {pm(4,lista)}   |   {pm(5,lista)}   |   {pm(6,lista)}   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   {pm(7,lista)}   |   {pm(8,lista)}   |   {pm(9,lista)}   |
    |       |       |       |
    +-------+-------+-------+
    '''
    return board

def pm(i,lista): ## przypisywanie miejsca
    return lista.get(i)

def zmiana_na_planszy(lista,lokalizacja,znak):
    lista[lokalizacja]=znak
    return lista

def ruch(kto,znak,wartosc):
    persona = wartosc
    while persona in pola_gracza or persona in pola_komputera:
        if znak == "x":
            persona = random.randint(1,9)
        else:
            persona = int(input("to miejsce jest zajete, wybierz inne:"))
    kto.append(persona)
    for pozycyja in kto:
        list = zmiana_na_planszy(lista, pozycyja, znak)
    print(draw_move(list))



lista = (wytwornia_list())
lista[5]="x"
pola_komputera=[5]
pola_gracza=[]

print(draw_move(lista))
while True:
    persona = int(input("blablabla"))
    ruch(pola_gracza,'o',persona)
    if czy_mamy_zwyciesce(pola_gracza):
        print("wygrywa gracz")
        break
    ruch(pola_komputera,'x', random.randint(1,9))
    if czy_mamy_zwyciesce(pola_komputera):
        print("wygrywa komputer")
        break


print('koniec')