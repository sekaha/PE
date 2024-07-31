from time import time


def get_prime_sum(n):
    is_prime = [True] * n
    prime_sum = 0

    for i in range(2, n):
        if is_prime[i]:
            prime_sum += i

            for j in range(i * i, n, i):
                is_prime[j] = False

    return prime_sum


s = time()
print(get_prime_sum(2_000_000))

print(f"{time()-s:.2f}s")
