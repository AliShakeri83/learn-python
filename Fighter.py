from random import randint
import time
class Fighter:
    def __init__(self, Health, Defense, power):
        self.Health = Health
        self.Defense = Defense
        self.Power = power

    def ToKnock(self, fighter):
        fighter.Health -= abs(self.Power - fighter.Defense)

f1 = Fighter(randint(70, 100), randint(30,50), randint(40,50))
f2 = Fighter(randint(70, 100), randint(30,50), randint(40,50))
while True:
    print("Fighter 1 is fight to Fighter 2 ...")
    f1.ToKnock(f2)
    print(f1.Health)
    if f2.Health <= 0:
        print("Fighter 1 win the game!")
        break
    time.sleep(1)
    print("Fighter 2 is fight to Fighter 1 ...")
    f2.ToKnock(f1)
    print(f1.Health)
    if f1.Health <= 0:
        print("Fighter 2 win the game!")
        break
    time.sleep(1)
    print('--------------------------')
