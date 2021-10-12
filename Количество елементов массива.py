numbers=[2.3,4.5,3.5,10.3,5]
t = numbers[0]
#k=0
#for i in numbers:
#    k+=1
#print(k)
#b=0
#for i in numbers:
#   b+=i 
#print(k)
k=0
for i in numbers:
    if t<i:
        t=i
    else:
        k=t
print(k)
    
