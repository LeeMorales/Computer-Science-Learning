#Beautiful is better than ugly.
#Explicit is better than implicit.
#Simple is better than complex.
#Complex is better than complicated.
#Flat is better than nested.
#Sparse is better than dense.
#Readability counts.
#Special cases aren't special enough to break the rules.
#Although practicality beats purity.
#Errors should never pass silently.
#Unless explicitly silenced.
#In the face of ambiguity, refuse the temptation to guess.
#There should be one-- and preferably only one --obvious way to do it.
#Although that way may not be obvious at first unless you're Dutch.
#Now is better than never.
#Although never is often better than *right* now.
#If the implementation is hard to explain, it's a bad idea.
#If the implementation is easy to explain, it may be a good idea.
#Namespaces are one honking great idea -- let's do more of those!
print ('Hello world, I am Python')
print (985*211)
print (45678+0x12fd2)
print ('Learn Python in imooc')
print (100 < 99)
print (0xff == 255)
x1 = 1
d = 3
n = 100
x100 = x1+(n-1)*d
s = (x1+x100)*100/2
print (s)
s = 'Python was started in 1989 by "Guido".Python is free and easy to learn.'
print (s)
name = input('Enter file:')
handle = open(name, 'r')
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
    print(bigcount, bigword)
n = 100

s1 = ['a,b,c']
s2 = [1,2,3]
print (dict(zip(s1,s2)))

a = input("imput a:")
b = input("imput b:")
if a < b:
    print (int(a)/int(b), int(a)+int(b))
else:
    print ("none")
