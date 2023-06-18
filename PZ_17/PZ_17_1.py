# Создайте класс «Банк», который имеет атрибуты суммы денег и процентной ставки. 
# Добавьте методы для вычисления процентных начислений и снятия денег. 


class Bank:
    def __init__(self, money, interest_rate):
        self.money = money
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.money * (self.interest_rate / 100)
        self.money += interest
        return interest
    
    def withdraw(self, amount):
        if amount > self.money:
            return "Недостаточно средств на счете"
        else:
            self.money -= amount
            return amount

bank1 = Bank(10000, 5)
print("Начальная сумма денег на счете:", bank1.money)
print("Процентная ставка:", bank1.interest_rate)

interest = bank1.add_interest()
print("Начисленные проценты:", interest)
print("Сумма денег на счете после начисления процентов:", bank1.money)

withdraw_amount = 8000
withdraw_result = bank1.withdraw(withdraw_amount)
if type(withdraw_result) == str:
    print(withdraw_result)
else:
    print("Снято со счета:", withdraw_result)
    print("Остаток на счете:", bank1.money)
