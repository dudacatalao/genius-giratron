import random
import pyttsx3
from game import Game
import time


class Giratron(Game):
    def __init__(self):
        super().__init__()

    def starting(self):
        print('-' * 20)
        for i in range(1, 4):
            print(i)
            time.sleep(1)
        print('Lets play GIRATRON')
        self.falar()

    def falar(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', 'english-us')
        self.raffle = []

        for i in range(self.level):
            self.raffle.append(random.choice(self.color_numbers))

        for numero in self.raffle:
            texto = str(numero)
            self.engine.say(texto)
            self.engine.runAndWait()

        count = 0
        self.sequence_user = []
        while count < self.level:
            count += 1
            print(f'Now, tape the {count}º:')
            self.sequence_user.append(str(input(f'{count}. ')))

        self.checking()

    def checking(self):
        print("Checking your sequence...")
        time.sleep(1)

        for i in range(self.level):
            if self.sequence_user[i] == str(self.raffle[i]):
                print(f'Number {i + 1} is correct!')
            else:
                RED = "\033[1;31m"
                RESET = "\033[0;0m"
                print(RED + f'Number {i + 1} is incorrect. Correct number was {self.raffle[i]}' + RESET)

        if self.sequence_user == self.raffle:
            print(f'congrats, you won')
            self.win = True

        else:
            print("sorry, you lost")
            self.play_again()

        if self.win == True:
            print(f'Now you are on the next level')
            if self.level > 3:
                self.level += 1
                self.starting()
            elif self.level < 7:
                print("You've reached the maximum level!")
                self.menu()
        else:
            print("Try again to pass the level")
            self.starting()

    def play_again(self):
        print("-" * 20)
        option = int(input("Do you want to play again?\n[1] Yes\n[2] No\n[3]Menu\n"))

        if option == 1:
            self.starting()

        elif option == 2:
            print("Thank you! ")
            exit()

        elif option == 3:
            self.menu()

