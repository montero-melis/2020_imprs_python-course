import os
from PIL import Image
from PIL import ImageFilter

# load image
img_folder = "C:\\Users\\gumo8029\\PycharmProjects\\session2a-image\\raw"
img_path = os.path.join(img_folder, "bird.jpg")
img = Image.open(img_path)
# img.show()

# crop
print(img.size)
print("ho")
print(img.tile)

# coordinates: left up, right low
reg = (0, 100, 200, 300)
reg2 = (20, 120, 220, 320)
img_crop = img.crop(reg)
# img_crop.show()

# rotate
img_crop = img_crop.transpose(Image.ROTATE_180)
# img_crop.show()

# img.show()
# img.paste(img_crop, reg)
# img.show()

# square crop
width = img.width
height = img.height

# center coords
center = (width / 2, height / 2)
shortest_side = min([width, height])

distance_from_center = shortest_side / 2

left = []
right = []

print(left,right)

for number in center:
    left.append(number - distance_from_center)
    right.append(number + distance_from_center)

print(left,right)
img_square = img.crop((left[0], left[1], right[0], right[1]))
# img_square.show()

img_rsz = img_square.resize((100, 100))
# img_rsz.show()

# convert to b/w
blw = img.convert("L")

# apply filter
img_enh = img.filter(ImageFilter.EDGE_ENHANCE)
# img_enh.show()

# Point transforms
img_contrast = img.point(lambda i: i * 1.3)
# img_contrast.show()
