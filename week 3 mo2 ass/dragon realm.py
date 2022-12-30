import random
import time


def start():
    print('''you are in a land full of dragons. in front of you you see two caves .'
          'in one cave the dragon is friendly and will share it treasure  with u'
          'the other is deadly and will eat u on sight'
          'which cave will you enter (1 or 2)''')



def game(num):
    print('you approach the cave ....')
    time.sleep(2)
    print('it is dark and spooky...')
    time.sleep(2)
    print('a large dragon jumps out in front of you!')
    time.sleep(2)
    print('he opens his jaw and...')
    time.sleep(2)
    friend=random.randint(1,2)
    if num==friend:
        print('give you his treasures')
    else:
        print('gobbles you down in one bite')
start()
cave=int(input('which cave do u wanna go'))
game(cave)
while input('do wanna play again y/n')=='y':
    start()
    cave = int(input('which cave do u wanna go'))
    game(cave)
