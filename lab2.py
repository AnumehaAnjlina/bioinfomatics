d={'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
over1=[]
over2=[]
over3=[]
mainstr='aaccggacgaaa'
substr='ggac'
substr2='cga'
for i in mainstr:
    over1.append(d[i])
for i in substr:
    over2.append(d[i])
for i in substr2:
    over3.append(d[i])
print(over1)
print(over2)
print(over3)
def conn(list1,num):
    for i in list1:
        if(i==num):
            return(list1.index(i))
    return("no")
           

#substring is there or not
def subS(over1,over2):
    for i in range(0,lenfun):
        k=i
        for j in range(0,len(over2)):
            if(over1[k]!=over2[j]):
                break
            k+=1
            j+=1
       
        if(j==len(over2)):
            return(i)
        i+=1
    return(-1)

lenfun=len(over1)+len(over2)
seclenfun=len(over1)+len(over3)
no=over3[0]
com2=conn(over2,no)
subS(over1,over2)
com1=subS(over1,over2)
print(com1,com2)
sec=com1+com2
print(sec)
seclenfun=len(over3)
def mainfun(over1,over3,sec):
    j=0
    count=0
    if(over1[sec]==over3[0]):
        #print("match")
        for i in range(sec,sec+seclenfun):
            if(over1[i]!=over3[j]):
                break
            i+=1
            j+=1
        if(j==len(over3)):
            return(j)
        else:
            return("no")
    else:
        return("not match")
       
       
print(mainfun(over1,over3,sec))
#if more substring means lagrer substing is used for conn

