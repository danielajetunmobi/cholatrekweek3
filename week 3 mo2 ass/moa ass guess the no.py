import random
import time


def game():
    computer_choice = random.randint(1, 20)

    tries = 6
    guesses = 0
    while tries>0:
        guess = int(input('guess a no between 1 and 20:'))
        if guess==computer_choice:
            time.sleep(1)
            guesses+=1
            print('u guess my no in ',guesses,'guesses')
            break
        elif guess>computer_choice:
            time.sleep(2)
            tries -= 1
            guesses += 1
            print('guess is too high')

        elif guess<computer_choice:
            time.sleep(2)
            tries -= 1
            guesses += 1
            print('ur guess is too low')

        else:
            print('not a valid guess')
    else:
        print('u ran out of tries sorry')
        print('my guess was',computer_choice)
game()
while input('do  wanna play again y/n')=='y':
    game()
else:
    print('thanks for playing')
