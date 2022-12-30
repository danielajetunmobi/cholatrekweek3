import random
def game():
     choose=('rock','scissors','paper')
     computer_choice=random.choice(choose)
     print('choose one of the following')
     user_choice=input('rock paper scissors:')

     print(computer_choice)
     while user_choice in choose:
          if computer_choice=='rock'and user_choice=='scissors':
               print('computer win')
               break
          elif computer_choice=='scissors' and user_choice=='rock':
               print('u win')
               break
          elif computer_choice=='rock' and user_choice=='paper':
               print('u win')
               break
          elif computer_choice=='paper' and user_choice=='rock':
               print('u win')
               break
          elif computer_choice=='scissors' and user_choice=='paper':
               print('computer win')
               break
          elif computer_choice=='paper' and user_choice=='scissors':
               print('u win')
               break
          else:
               print('a tie')
               break
     else:
          print('wrong input')

game()
while input('u wanna play again:y/n:')=='y':
     game()
else:
     print('thanks for playing')

