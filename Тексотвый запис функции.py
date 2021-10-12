x=float(input('x= '))
b=float(input('b= '))
if x<=2:
    if b<0:
        print('y= ',-9*x**2-12*b)
    elif b>=0:
        print('y= ',3*x**2-8*b)
    else:print('y= ',32+x)
