money=5000;
data=float(input("Сколько дней прошло с депозита "));
if data>364:
    money=money+money*0.2
    print("Вот ваши деньги: ",money,"grn")
else:
    print("Вот ваши деньги: ",money,"grn")
