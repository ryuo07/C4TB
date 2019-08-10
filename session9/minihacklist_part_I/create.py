colors = ["blue", "red", "yellow", "green"]
print("Our color list:")
print(*colors, sep=", ")
new_color = input('Enter a new color: ')
colors.append(new_color)
print("Our new color list:")
print(*colors, sep=", ")