a = ['sport', 'lol','bts']
print(a)
for i in range(3):    
    b = input('one more hobby: ')
    a.append(b)
print(a)

for f in a:
    if "e" in f or "E" in f:
        print(f)