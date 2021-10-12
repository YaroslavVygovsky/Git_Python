year=365
data=integer(input('Сколько времени прошло с депозита? '))
money=integer(input('Сколько денег вы вложили? '))
if data>=year:
    money:=money*(data//365*0.2)
    print(money)
else:
    money:=money;
print(money)
    
