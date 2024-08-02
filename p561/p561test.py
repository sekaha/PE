for i in range(1, 5):
    a = []

    for j in range(0, 11):
        a.append(f"{int(i**j)}")

    print(f"{i}: " + ", ".join(a))
