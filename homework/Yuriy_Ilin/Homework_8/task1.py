import random

def get_bonus(salary):
    bonus = (True, False)
    if random.choice(bonus):
        total_salary = salary + salary * (random.uniform(0.1, 0.5))  # Подразумевается, что бонус может составить от 10 до 50%
        return round(total_salary, 2)
    return salary


salary = int(input())
print(f"Твоя зарплата с учетом бонуса составляет: {get_bonus(salary)}")
