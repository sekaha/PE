from gentool import *
from random import choice


def lemonadeChange(bills) -> bool:
    inventory = {5: 0, 10: 0, 20: 0}

    def make_change(change):
        for b in (10, 5):
            while change > 0 and change - b >= 0 and inventory[b] > 0:
                # print(f"{b} used")
                change -= b
                inventory[b] -= 1

        # print(change)
        return change == 0

    for b in bills:
        change = b - 5

        if not make_change(change):
            return False

        inventory[b] += 1

    return True


while True:
    l = [choice([20, 5, 5, 5, 10, 20, 5, 5, 10]) for _ in range(10**5)]

    if lemonadeChange(l):
        break

lc_copy_debug(l)
