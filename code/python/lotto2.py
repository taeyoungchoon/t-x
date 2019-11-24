#!/usr/bin/env python3
#
# lotto 6/45
#

import random

# init
numbers = []
lotto = []
limit = 45
loop = 6
numbers = [i for i in range(1, limit + 1)]

# loop 6 times
for i in range(loop):
    pick = random.choice(numbers)
    lotto.append(pick)
    numbers.remove(pick)

# finally
lotto.sort()
print(lotto)
