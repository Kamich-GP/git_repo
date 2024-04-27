class Player:
    def __init__(self, speed, accuracy, stamina, power):
        self.speed = speed
        self.accuracy = accuracy
        self.stamina = stamina
        self.power = power


class GoalKeeper(Player):
    def __init__(self, speed, accuracy, stamina, power):
        super().__init__(speed, accuracy, stamina, power)


    def save(self):
        print('Поймал мяч в руки')
