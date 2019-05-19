import random

class window:
    def __init__(self):

        self.allcards = ['6', '7', '8', '9', '10', 'J', 'D', 'K', 'T']
        self.diler = []
        self.dilerschet = 0
        self.player = []
        self.playerschet = 0
        self.schetchik = 0
        self.schetchik2 = 0
        self.startgame()
    def startgame(self):
        for i in range(2):
            self.diler.append(random.choice(self.allcards))
            self.player.append(random.choice(self.allcards))
        self.centergame()        
    def centergame(self):
        if self.schetchik2 == 0:
            for i in self.player:
                if i == "6":
                    self.playerschet = self.playerschet + 6
                if i == "7":
                    self.playerschet = self.playerschet + 7
                if i == "8":
                    self.playerschet = self.playerschet + 8
                if i == "9":
                    self.playerschet = self.playerschet + 9
                if i == "10":
                    self.playerschet = self.playerschet + 10
                if i == "J":
                    self.playerschet = self.playerschet + 2
                if i == "D":
                    self.playerschet = self.playerschet + 3
                if i == "K":
                    self.playerschet = self.playerschet + 4
                if i == "T":
                    self.playerschet = self.playerschet + 11
        if self.schetchik == 0:
            for i in self.diler:
                if i == "6":
                    self.dilerschet = self.dilerschet + 6
                if i == "7":
                    self.dilerschet = self.dilerschet + 7
                if i == "8":
                     self.dilerschet = self.dilerschet + 8
                if i == "9":
                    self.dilerschet = self.dilerschet + 9
                if i == "10":
                    self.dilerschet = self.dilerschet + 10
                if i == "J":
                    self.dilerschet = self.dilerschet + 2
                if i == "D":
                    self.dilerschet = self.dilerschet + 3
                if i == "K":
                    self.dilerschet = self.dilerschet + 4
                if i == "T":
                    self.dilerschet = self.dilerschet + 11
        if self.dilerschet == 21:
            print('Победа Дилера')
        elif self.playerschet == 21:
            print('Победа Игрока')
        else:
            self.check()

    def check(self):
        if self.dilerschet <= 15:
            self.schetchik2 = 1
            self.diler = []
            self.diler.append(random.choice(self.allcards))
            self.centergame()
        else:
            if self.playerschet > 21:
                print('Перебор у игрока')            
            elif self.dilerschet > 21:
                print('Перебор у дилера')
            else:
                print(f"Дилер: {self.dilerschet} Вы: {self.playerschet}")
                self.otv = int(input('1.Себе 2.Ещё\nВведите цифру: '))
                if self.otv == 1:
                    if self.dilerschet > self.playerschet:
                        print('Победа Дилера')
                    elif self.dilerschet == self.playerschet:
                        print('Ничья')
                    else:
                        print('Победа Игрока')
                if self.otv == 2:
                    self.player = []
                    self.player.append(random.choice(self.allcards))
                    self.schetchik = 1
                    self.schetchik2 = 0
                    self.centergame()
                                   
wn = window()
