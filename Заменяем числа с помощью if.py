a=float(input('a= '))
b=float(input('b= '))
if a<b:
    a=0
    b=1
elif b<a:
    a=1
    b=0
else:
    print('Все норм не парься')
print('a= ',a,', b= ',b)
