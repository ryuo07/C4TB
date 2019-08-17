computers = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30,
}

computers["TOSHIBA"] = 10

computers["DELL"] = computers["DELL"] + 10
computers["MACBOOK"] = computers["MACBOOK"] - 2

computers["FUJITSU"] = 15
computers["ALIENWARE"] = 5
print(computers)

computer_price = {
    "HP" : 600,
    "DELL" : 650,
    "MACBOOK" : 12000,
    "ASUS" : 400,
    "ACER" : 350,
    "TOSHIBA" : 600,
    "FUJITSU" : 900,
    "ALIENWARE" : 1000,
}
print(computer_price)
l = len(computer_price)
for k,v in computers.items():
    print("price of all",k,"in store:",computers[k]*computer_price[k])
    
        