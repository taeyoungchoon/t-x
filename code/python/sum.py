#!/usr/bin/python

max = 100

# sum of number and slow
sum = 0
for num in range(1, max + 1):
    sum = sum + num

print(type(sum))
print(sum)

# cons half and fast

sum = 0
half = max / 2
sum = str(int(half)) + str(int(half))
print(type(sum))
print(sum)
