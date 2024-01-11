class Game:
    def __init__(self): 
        self.player = None
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
        print('-' * 20)
        print("WELCOME TO THE GAME\nCreate your profile:")

        try:
            name = input("Insert your name: ")
            age = input("Insert your age: ")
            self.player = Player(name, age)
        except ValueError:
            print("You entered invalid data")

        if self.player:
            print("Player created")
            print(f'{self.player.nome}: {self.player.idade}')
            self.menu()
        else:
            print("Try again")
            self.create_player()

    @staticmethod
    def menu():
        print("-" * 30)
        print("GIRATRON AND GENIUS")
        while True:
            option = int(input("[1] Giratron\n[2] Genius\n[3] How to play?\n[4] Exit: "))

            if option == 1:
                play = Giratron()
                play.starting()
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
