distric = ["ST","BĐ","BTL","CG","ĐĐ","HBT"]
population = [150300, 247100,333300,266800,420900,318000]
km2 = [11743, 9.224, 43.35, 12.04, 9.96, 10.09]
density = []
l = len(km2)
for i in range(l):
    a = population[i] / km2[i]
    density.append(a)
average_population = sum(density)/l
print(average_population)