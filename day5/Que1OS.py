



import os

folder = "notes"
os.makedirs(folder, exist_ok=True)           # create if not exists

file_path = os.path.join(folder, "hello.txt")

# Write
with open(file_path, "w") as f:
  f.write("Hello from Python!\n")

# Read
with open(file_path, "r") as f:
  content = f.read()

print("File content:", content)
print("Saved at:", file_path)




