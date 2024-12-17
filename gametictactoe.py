def game_tic_tac_toe():
    board = [" " for _ in range(9)]

    def print_board():
        print(f"{board[0]} | {board[1]} | {board[2]}")
        print("---------")
        print(f"{board[3]} | {board[4]} | {board[5]}")
        print("---------")
        print(f"{board[6]} | {board[7]} | {board[8]}")

    while True:
        print_board()
        pilihan = input("Masukkan pilihan (1-9): ")
        if board[int(pilihan) - 1] == " ":
            board[int(pilihan) - 1] = "X"
            if " " not in board:
                print("Seri!")
                break
            print_board()
            pilihan = input("Masukkan pilihan lawan (1-9): ")
            if board[int(pilihan) - 1] == " ":
                board[int(pilihan) - 1] = "O"
                if " " not in board:
                    print("Seri!")
                    break
        else:
            print("Pilihan sudah terisi!")

game_tic_tac_toe()


# Program 7: Penghitung Jumlah Kata

def penghitung_jumlah_kata():
    kalimat = input("Masukkan kalimat")
