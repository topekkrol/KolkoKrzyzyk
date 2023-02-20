# def display_board(board):
#
#
# #
# # Funkcja, która przyjmuje jeden parametr zawierający bieżący stan tablicy
# # i wyświetla go w oknie konsoli.
# #
#
# def enter_move(board):
#
#
# #
# # Funkcja, która przyjmuje parametr odzwierciedlający biężący stan tablicy,
# # prosi użytkownika o wykonanie ruchu,
# # sprawdza dane wejściowe i aktualizuje tablicę zgodnie z decyzją użytkownika.
# #
#
# def make_list_of_free_fields(board):
#
#
# #
# # Funkcja, która przegląda tablicę i tworzy listę wszystkich wolnych pól;
# # lista składa się z krotek, a każda krotka zawiera parę liczb odzwierciedlających rząd i kolumnę.
# #
#
# def victory_for(board, sign):
#
#
# #
# # Funkcja, która dokonuje analizy stanu tablicy w celu sprawdzenia
# # czy użytkownik/gracz stosujący "O" lub "X" wygrał rozgrywkę.
# #

def draw_move(board):
    board='''
    +-------+-------+-------+
    |       |       |       |
    |   1   |   2   |   3   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   4   |   X   |   6   |
    |       |       |       |
    +-------+-------+-------+
    |       |       |       |
    |   7   |   8   |   9   |
    |       |       |       |
    +-------+-------+-------+
    '''
    return board

print(draw_move("x"))