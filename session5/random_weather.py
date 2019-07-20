from secrets import randbelow
a = randbelow(100)
print(a)

if a < 30:
    print("Rainy")
elif a < 60:
    print("Cloudy")
elif a <= 100:
    print("Sunny")