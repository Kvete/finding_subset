from random import randint


def multiply(a, b):
    res = []
    for i in range(len(a)):
        res.append(a[i] * b[i])
    return res


def recurtion(mas, alphabet, result, length=0, ):
    if len(result) == length:
        s = 0
        for i in range(len(result)):
            s += mas[i] * result[i]
        if s == find:

            c = multiply(mas, result)
            for i in range(len(c)):
                if 0 in c:
                    c.remove(0)
            print('res list: ', c)

        return

    for el in alphabet:
        result[length] = el
        recurtion(mas, alphabet, result, length + 1)


mas = [randint(-20, 20) for j in range(10)]
print('given mas: ', mas)
result = [0 for j in range(len(mas))]
find = 10

recurtion(mas, [0, 1], result)
