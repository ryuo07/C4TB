colors = ["blue", "red", "yellow", "green"]
print("Our color list:")
l = len(colors)
for a,b in enumerate(colors):
    c = str(a+1)
    print(c+"."+b)

d = input("Item to delete:")
if d.isalpha():
    colors.remove (d)
    for e in range(3):
        f = str(e+1)
        g = colors[e]
        print(f+"."+g)
elif d.isdigit():
    i = int(d)-1
    colors.pop(i)
    for e in range(3):
        f = str(e+1)
        g = colors[e]
        print(f+"."+g)
colors = ["blue", "red", "yellow", "green"]            
h = input("Item to delete:")
if h.isalpha():
    colors.remove (h)
    for i in range(3):
        j = str(i+1)
        k = colors[i]
        print(j+"."+k)
elif h.isdigit():
    i = int(h)-1
    colors.pop(i)
    for i in range(3):
        j = str(i+1)
        k = colors[i]
        print(j+"."+k)
