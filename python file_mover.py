import os 
import shutil

#Source folder input 
source = input("Enter the Source Folder Location: " ).strip()

#Destination folder input
destination = input("Enter the Destination Folder Location: ")

#Create if destinatio folder doesn't exist
if not os.path.exists(destination):
    os.makedirs(destination)

for file in os.listdir(source):
    if file.endswith(".jpg"):
        source_path = os.path.join(source, file)
        destination_path = os.path.join(destination, file)

        shutil.move(source_path, destination_path)
        print(f"Moved: {file}")

print("All .jpg files moved Sucessfultyy...")