#1 removing a character in a string
str='python'
n=3
if n>0 :
    str=str[:3]+str[4:]
    print(str)
#2
lis=[]
len=int(input('enter len of str'))
i=0
while i<len:
    i+=1
    n=input('enter a char:')
    lis.append(n)
    lis.sort()
print(lis)
#3
n=float(input('enter a decimal no of more than two:'))
print(round(n,2))
#4
samplestring='the quick black fox came to the black house '
print('no of black is',samplestring.count('black'))
#5
def reverse(x):
    result=''
    for i in x:
        result=i+result
    return result
me='data science'
p=reverse(me)
print(p)
#6
s='32.054,23'
maketrans=s.maketrans
s= s.translate(maketrans(',.','.,',' '))
print(s)