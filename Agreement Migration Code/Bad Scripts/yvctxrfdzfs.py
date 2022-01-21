import os


x=0


root_dir = "/Users/everetmm/Desktop/Agreement_Migration"
for dir_, _,files in os.walk(root_dir):
    for file_name in files:
        if "(Original)" in file_name:
            x=x+1


print(x)
    
