import random


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

def ruch(kto):
    wybor_gracza = int(input("blablabla"))
    while wybor_gracza in pola_gracza or wybor_gracza in pola_komputera:
        wybor_gracza = int(input("to miejsce jest zajete, wybierz inne:"))
    pola_gracza.append(wybor_gracza)
    for pozycyja in pola_gracza:
        list = zmiana_na_planszy(lista, pozycyja, "o")
    print(draw_move(list))

lista = (wytwornia_list())
lista[5]="x"
pola_komputera=[5]
pola_gracza=[]

print(draw_move(lista))
while True:

    wybor_gracza = int(input("blablabla"))
    while wybor_gracza in pola_gracza or wybor_gracza in pola_komputera:
        wybor_gracza = int(input("to miejsce jest zajete, wybierz inne:"))
    pola_gracza.append(wybor_gracza)
    for pozycyja in pola_gracza:
        list = zmiana_na_planszy(lista, pozycyja, "o")
    print(draw_move(list))

    wybor_komputera = random.randint(1,9)
    while wybor_komputera in pola_gracza or wybor_komputera in pola_komputera:
        wybor_komputera = random.randint(1,9)
    pola_komputera.append(wybor_komputera)
    for pozycja in pola_komputera:
        lista = zmiana_na_planszy(lista,pozycja,"x")
    print(draw_move(lista))