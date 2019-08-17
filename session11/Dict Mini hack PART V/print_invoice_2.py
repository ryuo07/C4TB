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

a = input("enter a computer name: ").upper()
b = int(input("enter number of computer you want to buy: "))
print("price of", b, a ,"comuter:", computer_price[a]*b)