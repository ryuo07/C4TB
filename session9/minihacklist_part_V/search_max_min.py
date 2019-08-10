distric = ["ST","BĐ","BTL","CG","ĐĐ","HBT"]
population = [150300, 247100,333300,266800,420900,318000]
a = max(population)
b = min(population)
l = len(population)
for i in range(l):
    if population[i] == a:
        print("the most populated distric is:",distric[i])
    elif  population[i] == b:
        print("the less populated distric is:",distric[i])
