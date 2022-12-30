import random
import  sys
import array

up=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
low=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
sym=('!','£','$','%','&','*','@','#','<',',','>','.',';',':')
num=('1','2','3','4','5','6','7','8','9','0')
upper=random.choice(up)
lower=random.choice(low)
syms=random.choice(sym)
nums=random.choice(num)
temp=upper+lower+syms+nums
combine=up+low+sym+num
length=int(input('please enter the length of ur password, should not be less than six:'))

if length>=6:
    try:

        for i in range(length-4) :
            temp=random.choice(combine)+temp
            lists=array.array('u',temp)
            random.shuffle(lists)
        password=''
        for i in lists:
            password = password + i
        print(password)

    except(TypeError):
        print(sys.exc_info()[0],'occured')


else:
    print('password should not be less than six')


