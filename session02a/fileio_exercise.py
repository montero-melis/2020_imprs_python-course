import os
from PIL import Image

# where are the images?
old_folder = "C:\\Users\\gumo8029\\PycharmProjects\\session2a-image\\raw"

# make a new folder
new_folder = "C:\\Users\\gumo8029\\PycharmProjects\\session2a-image\\temp"
# os.mkdir(new_folder)

# list all files
img_list = os.listdir(old_folder)
print(img_list)

for img in img_list:
    img_path = os.path.join(old_folder, img)
    img_open = Image.open(img_path)
    img_open.save(os.path.join(new_folder, img))

