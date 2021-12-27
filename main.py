import os

path = "test"

if not os.path.exists(path):
    os.mkdir(path)
    print(f"{path} directory created successfully")
else:
    print(f"Failed to create directory {path}")

os.chdir(path)

with open("data.txt", "a", encoding="utf-8") as f:
    f.write("Test ")
