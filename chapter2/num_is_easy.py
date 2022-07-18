from decimal import Decimal

score = 100
temp = 37.2
com = 1 + 2j

print(int(score))
print(float(score))
print(complex(score))
print(int(temp))
print(float(temp))
print(complex(temp))

print(0.1 + 0.2)


print(Decimal('0.1') + Decimal('0.2'))

print(Decimal(0.1) + Decimal(0.2))

print(int(True), int(False))

print(1 + True, 1 + False)

numbers = [1, 2, 4, 5, 7]

count = 0
for i in numbers:
    if i % 2 == 0:
        count += 1

print(count)

print(sum(i % 2 == 0 for i in numbers))

print(float('inf'))
