a = ['sport', 'lol','bts']
print(a)
for i in range(3):    
    b = input('one more hobby: ')
    a.append(b)
print(a)

for e,f in enumerate(a):
    print(e+1, f.upper())