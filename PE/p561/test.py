from random import choice

chars = "   /\\"
W = 5  # 30

print(["".join([choice(chars) for _ in range(W)]) for _ in range(W)])
