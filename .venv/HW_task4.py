'''
4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
 Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)
'''


from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000

attempts = 10
num = randint(LOWER_LIMIT,UPPER_LIMIT)

print('Угадайте число от 0 до 1000 за 10 попыток.')

for i in range(1, attempts + 1):
    guess = int(input(f'Попытка {i}:\nВведите число: '))
    if guess < LOWER_LIMIT or guess > UPPER_LIMIT:
        print(f'Число должно быть в диапазоне от {LOWER_LIMIT} до {UPPER_LIMIT}')
        continue
    if guess < num:
        print('Загаданное число больше')
    elif guess > num:
        print('Загаданное число меньше')
    else:
        print(f'Вы угадали число {num}')
        break
else:
    print(f'Число попыток закончилось. Загаданное число было {num}')
