items = ['bun','mien','pho']

while True:
    a = input('enter C , R , U , D or exit: ')
    if a == "C":
        b = input('add one more favorite meal:')
        items.append(b)
        print(items)
    elif a == "R":
        for i, item in enumerate(items):
            print(i+1, item)
    elif a == "U":
        b=int(input("place you want to replace in the menu:"))
        items[b-1] = input('replace anothor favorite meal:')
        print(items)
    elif a == "D":
        b = int(input('place you want to delete: '))
        items.pop(b-1)
        print(items)
    elif a == "exit":
        break
    else :
        print("wrong, please enter again:")
        
