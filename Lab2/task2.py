money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
budg = money_capital
m = 0
while budg + salary >= spend:
    budg += salary
    m += 1
    budg -= spend
    spend *= (1 + increase)

print("Количество месяцев, которое можно протянуть без долгов:", m)
