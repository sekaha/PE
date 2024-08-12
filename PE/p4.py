# Find largest 3 digit palindromic factor


# Kinda gotta work backwards, construct palindrome first
# then see if it has factors
# 100_001~999_999
def get_palindrome(digits):
    upper = 10 ** (digits) - 1
    lower = 10 ** (digits - 1)
    max_possible = upper**2

    for i in range(upper, lower - 1, -1):
        s = str(i)
        n = int(s + s[::-1])

        if n > max_possible:
            continue

        for j in range(upper, lower - 1, -1):
            if n % j == 0 and n // j <= 999:
                print(n, j, n // j, "=", j * (n // j))
                return (j, n // j)


print(get_palindrome(3))
