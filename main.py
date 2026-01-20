import os

for i in range(1000):
    path = os.path.join("data",f"text_{i:04d}.txt")
    with open(path, "w") as f:
        f.write("Halo")
    f.close()