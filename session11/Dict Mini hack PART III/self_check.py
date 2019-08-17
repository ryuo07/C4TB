computers = {
    "HP" : 20,

    "DELL" : 50,

    "MACBOOK" : 12,

    "ASUS" : 30,
}

for i in range(2):
    if i == 0:        
        computers["TOSHIBA"] = 10
        print(computers)
        for k,v in computers.items():
            print(k,":",v)
    if i == 1:
        a = 0
        computers["FUJITSU"] = 15
        computers["ALIENWARE"] = 5
        print(computers)
        for k,v in computers.items():
            a = a + v
        print("total number of computers:", a)