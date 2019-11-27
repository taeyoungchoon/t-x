#!/usr/bin/env python3
#
# lotto 6/45
#

import random

# init
numbers = []
lotto = []
max = 45
loop = 6
for i in range(1, max + 1):
    numbers.append(i)

# loop 6 times
for i in range(loop):
    length = len(numbers)
    idx = random.randint(1, length) - 1
    pick = numbers[idx]
    numbers.remove(pick)
    lotto.append(pick)

# finally
lotto.sort()
print(lotto)
