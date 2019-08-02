a = ['sport', 'lol','bts']
print(a)
new_item = input('new favorite thing: ')
a.append(new_item)
print(a)
print(*a, sep='|')