n = int(input('Количество учеников: '))
k = int(input('Количество яблок: '))

ost = k % n
otv = k // n

print('Остаток', ost, 'яблок')
print('Каждый ученик получил', otv, 'яблок')