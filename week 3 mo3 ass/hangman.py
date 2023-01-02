def print_hangman(wrong):
    if wrong==0:
        print('\n+---+')
        print('    |')
        print('    |')
        print('    |')
        print('   ===')
    elif wrong==1:
        print('\n+---+')
        print('0   |')
        print('    |')
        print('    |')
        print('   ===')
    elif wrong==2:
        print('\n+---+')
        print('0   |')
        print('|   |')
        print('    |')
        print('   ===')
    elif wrong==3:
        print('\n+---+')
        print(' o  |')
        print('/|  |')
        print('    |')
        print('   ===')

    elif wrong==4:
        print('\n+---+')
        print(' o  |')
        print('/|\ |')
        print('    |')
        print('   ===')

    elif wrong==5:
        print('\n+---+')
        print(' o  |')
        print('/|\ |')
        print('/   |')
        print('   ===')
    elif wrong==6:
        print('\n+---+')
        print(' o  |')
        print('/|\ |')
        print('/ \ |')

import random
word_list=['daniel','joseph','tomiwa','mofe','funto','doyin','ayobami','suscribe','obina']
def get_word():
  word=random.choice(word_list)
  return word.upper()
def play(word):
    globals()
    word_completion='_'*len(word)
    guessed=0
    guessed_letters=[]
    guessed_word=[]
    tries=0
    length=len(word)
    print('let play')
    print(print_hangman(tries))
    print(word_completion)
    print('\n')
    while guessed!=length and tries!=6:
        print(word_completion)
        guess=input('guess a word:').upper()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letters:
                print('u ave aiready guessed',guess)
            elif guess not in word:
                print(guess,'is not in word')
                tries+=1
                print_hangman(tries)
            else:
                print('good job',guess,'is in the world')
                guessed_letters.append(guess)
                word_as_list=list(word_completion)
                indices = [i for i,letter in enumerate(word) if letter in guess]

                for index in indices:
                    word_as_list[index]=guess
                    word_completion=''.join(word_as_list)
                    guessed += 1

        elif len(guess)==len(word) and guess.isapha():
            if guess in guessed_word:
                print('you ave alreadly guess ',guess)
            elif guess != word:
                print(guess,'is not in word')
                tries-=1
                guessed_word.append(guess)
            else:
                guessed+=1
                word_completion=word
        else:
            print('not a valid guess')
            print(print_hangman(tries))
            print(word_completion)
            print('\n')
    if guessed==length:
        print('congrat,you guessed the word',word)
    else:
        print('sorry ,you ran out of tries  the word was',word)
def main():
    word=get_word()
    play(word)
main()
while input('play again(Y/N)').upper()=='y':
        word = get_word()
        play(word)
else:
    print('thanks for playing')








