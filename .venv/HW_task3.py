'''
 Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
 Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.
'''

LOWER_LIMIT = 0
UPPER_LIMIT = 100_000
ONE = 1
num = LOWER_LIMIT - ONE
counter = 0

while num > UPPER_LIMIT or num < LOWER_LIMIT:
    num = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}:'))

for i in range(2, num // 2 + 1):
    if (num % i == 0):
            counter += 1
if (counter <= 0):
    print("Число простое")
else:
    print("Число не является простым")