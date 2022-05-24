# txt
```
# write
with open("kernel_gradients.txt", "w") as txt:
    for i in range(angles.shape[0]):
        for j in range(angles.shape[1]):
            txt.write(f"{angles[i, j]},")
        txt.write(f"\n")
# read
with open("kernel_gradients.txt", "r") as txt:
    for line in txt:
        line_vec = line.split(", ")
        print(line_vec)
```