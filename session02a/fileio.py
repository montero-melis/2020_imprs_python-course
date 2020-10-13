import os
from PIL import Image

print(os.getcwd())

# directory
folder = "C:\\Users\\gumo8029\\PycharmProjects\\session2a-image\\raw"

# load an image
img_path = os.path.join(folder, "bird2.jpg")
print(img_path)
img = Image.open(img_path)

# img.show()

print(img.size)
print(img.size, img.format, img.mode)

# turn it into a png image
filename, extension = os.path.splitext(img_path)
print(filename, extension)

outfile = filename + '.png'
print(outfile)

img.save(outfile, "PNG")
os.remove(outfile)

# make a new folder
new_folder = "C:\\Users\\gumo8029\\PycharmProjects\\session2a-image\\temp"
# os.mkdir(new_folder)

our_file = "copy" + extension
print(our_file)
print(os.path.join(new_folder, our_file))
img.save(os.path.join(new_folder, our_file))

print("ho")
our_file2 = os.path.join(new_folder, filename) + extension
print(our_file2)
print(os.path.join(new_folder, filename) + extension)

img.save(os.path.join(new_folder, filename) + extension)
img.save(our_file2)

print(os.listdir(folder))
