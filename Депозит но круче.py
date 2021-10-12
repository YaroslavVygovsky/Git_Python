year=365
data=int(input('Сколько времени прошло с депозита? '))
money=int(input('Сколько денег вы вложили? '))
p=int(input('Какой ваш процент? '))
if (data>=year)and(data>=0)and(money>0):
    print('Вот ваши деньги ',money+money*(p/100)*(data//year))
elif (data<year)and(data>=0)and(money>0):
    print('Вы не сдержали условия контракта поетому вот ваши деньги ',money)
else:
    print('Не может быть')
