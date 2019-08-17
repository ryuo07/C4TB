computers = {
    "HP" : 20,
    "DELL" : 50,
    "MACBOOK" : 12,
    "ASUS" : 30,
}
print(computers)
for i in range(3):
    if i == 0:
        print("run time number 1:")
        computers["TOSHIBA"] = 10
        print(computers)
            
    if i == 1:
        print("run time number 2:")
        computers["DELL"] = computers["DELL"] + 10
        computers["MACBOOK"] = computers["MACBOOK"] - 2
        print(computers)
    if i == 2:
        print("run time number 3:")
        computers["FUJITSU"] = 15
        computers["ALIENWARE"] = 5
        print(computers)