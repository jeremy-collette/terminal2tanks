def lcd(a, b):
    for i in range(2, min(a,b)+1):
        if (a % i == 0 and b % i == 0):
            return i
    return -1

print(lcd(5, 10))