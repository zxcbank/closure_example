def fib():
    x0 = 0
    x1 = 1

    def subfib():
        nonlocal x0, x1

        x2 = x0 + x1
        x0, x1 = x1, x2
        return x2
    return subfib

fibFubction = fib()
for i in range(3, 119):
    print("{}-ый элемент последовательности фибоначчи равен {}".format(i, fibFubction()))
