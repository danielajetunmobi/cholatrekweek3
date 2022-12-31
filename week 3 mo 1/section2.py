                        #1 removing a character in a string

str='python'
n=3
if n>0 :
    str=str[:3]+str[4:]
    print(str)

                    #2 python program to accept a comma seperated seqeunce of words as input and print the unique word in sorted form

lis=[]
len=int(input('enter len of str'))
i=0
while i<len:
    i+=1
    n=input('enter a char:')
    lis.append(n)
    lis.sort()
print(lis)

                                  #3 python program to print a float num to 2 decimal place

n=float(input('enter a decimal no of more than two:'))
print(round(n,2))

                               #4 python programm to count a substring in a string

samplestring='the quick black fox came to the black house '
print('no of black is',samplestring.count('black'))

                 #5python written to reverse a string

def reverse(x):
    result=''
    for i in x:
        result=i+result
    return result
me='data science'
p=reverse(me)
print(p)
#6 python program to swap dot and comma in a string
s='32.054,23'
maketrans=s.maketrans
s= s.translate(maketrans(',.','.,',' '))
print(s)