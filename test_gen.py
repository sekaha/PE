from random import choice, randint

s1 = [choice("abcdefghijklmnopqrstuvwxyz") for _ in range(500)]
s2 = ""
runs = 0
while len(s2) != 500:
    runs += 1
    s2 = ""

    for c in s1:
        if randint(0,2):
            match randint(0,2):
                # insertion
                case 0:
                    s2 += choice("abcdefghijklmnopqrstuvwxyz")+c
                # deletion
                case 1:
                    s2 += ""
                # replacement
                case 2:
                    s2 += choice("abcdefghijklmnopqrstuvwxyz")
        else:
            s2 += c

print(runs)
print(len(s2))
print("".join(s1))
print()
print(s2)