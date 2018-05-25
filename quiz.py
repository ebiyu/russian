#coding: UTF-8
import random
random.seed()

#import from file
f=open('data.csv','r')
data=f.readlines()
f.close()
for i in range(len(data)):
    data[i]=[s.strip() for s in data[i].split(',')]
l=len(data)

conti=True

while conti:
    #shuffle
    for i in range(l):
        j=random.randrange(l)
        data[i],data[j]=data[j],data[i]

    #start quiz
    i=0
    c=0
    while i<l:
        ans=input(data[i][2]+'>')
        if ans==data[i][1]:
            print('OK')
            c+=1
            i+=1
        elif ans=='':
            print(data[i][1])
            i+=1
        elif ans=='q':
            break
        else:
            print('No!')
    print('result--')
    print('{0}/{1}'.format(c,i+1))
    if input('again?(y/N)')!='y':
        conti=False
