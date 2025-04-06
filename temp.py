import random
temp = random.randint(-10, 40)

is_sunny = True

if temp >= 25 and is_sunny:
    print("it is HOT outside")
    print("it is sunny")

elif temp <= 0 and is_sunny:
    print("it is cold outside")
    print("it is sunny outside")
else:
    print("it is neither cold nor hot outside")
    print("it is relatively sunny outside")
