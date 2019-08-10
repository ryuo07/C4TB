colors = ["blue", "red", "yellow", "green"]
print("Our color list:")
print(*colors, sep=", ")
position = colors[int(input("Enter position:"))-1]
print(position)