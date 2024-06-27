import random

def get_numbers_ticket(min_val, max_val, quantity):
# Умова
    if min_val < 1 or quantity < 1 or quantity > max_val:
        return []

# Генерація унікальних випадкових чисел
    numbers = random.sample(range(min_val, max_val + 1, 1), quantity)

    return sorted(numbers)

# Приклад 

lottery_numbers = get_numbers_ticket(1, 10, 4)
print("Ваші лотерейні числа:", lottery_numbers)
