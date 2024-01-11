import time


class Game:
    def __init__(self):
        self.players = []
        self.sequence_user = []
        self.raffle = []
        self.color_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "blue",
                              "pink", "purple", "yellow", "red", "black", "orange", "gray", "brown", "green", "white",
                              "violet"]
        self.color_options = ["blue", "pink", "purple", "yellow", "red", "black", "orange", "gray", "brown", "green",
                              "white", "violet"]

        self.win = False
        self.level = 4

    def create_player(self):
        print('-' * 30)
        print("WELCOME TO THE GAME\nCreate your player")

        try:
            name = input("Insert your name: ")
            age = input("Insert your age: ")
            self.player = Player(name, age)
            self.players.append(self.player)
        except ValueError:
            print("You entered invalid data")


        print("Player created")
        print("Checking players..")
        time.sleep(1)
        for self.player in self.players:
            print(f'{self.player.nome}: {self.player.idade}')
        self.option()

    def option(self):
        print('-' * 30)
        option = int(input("Do you want to create another player?\n[1] Yes\n[2] No: "))

        if option == 1:
            self.create_player()

        elif option == 2:
            self.menu()

        else:
            print("Invalid data. Insert again")
            self.option()

    @staticmethod
    def menu():
        print("-" * 30)
        print("GIRATRON AND GENIUS")
        while True:
            option = int(input("[1] Giratron\n[2] Genius\n[3] How to play?\n[4] Exit: "))

            if option == 1:
                play = Giratron()
                play.choose_player()
                break

            elif option == 2:
                play = Genius()
                play.starting()
                break

            elif option == 3:
                print("lalala")

            elif option == 4:
                print("Finishing game")
                exit()




if __name__ == "__main__":
    from giratron import Giratron
    from genius import Genius
    from player import Player

    jogo = Game()
    jogo.create_player()
