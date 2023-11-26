def diagonal_carpet(n):
    top= "-" * (n + 1)
    print(f"+{top}+")
    val = n
    for i in range(n + 1):
        left = "#" * val
        right = "#" * (n - val)
        print(f"|{left} {right}|")
        val -= 1
    print(f"+{top}+")
diagonal_carpet(10)