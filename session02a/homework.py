import os
from PIL import Image

# Create a new folder called "processed" where all images from "raw" are stored in .png.
# They are all cropped to ratio 4:3 (or 3:4) and resized to be all the same size.
# Notice:
# 1. There are different extensions
# 2. They are all different sizes
# 3. We have portrait and landscape orientated images
# Steps
# 0. Create a new folder
# 1. Define portrait and landscape images
# 2. Figure out on which side you have to crop the image
# 3. Crop the image
# 4. Resize the image
# 5. Save it to your new folder with the new extension. That's it!

#########################################################

old_folder = "C:\\Users\\gumo8029\\PycharmProjects\\session2a-image\\raw"
new_folder = "C:\\Users\\gumo8029\\PycharmProjects\\2020_imprs_python-course\\session02a\\processed"
# os.mkdir(new_folder)


# wrapper function
def edit_save(img_name):
    print("\n", img_name)  # informative output to console
    img_path = os.path.join(old_folder, img_name)  # path to current image
    img = Image.open(img_path)  # open current image
    filename, extension = os.path.splitext(img_name)
    img_name_new = filename + '.png'  # name of target image (after processing)
    orient = "landscape" if img.width > img.height else "portrait"  # image orientation
    print(orient)
    print("old size: ", img.size)
    new_img = crop_to_size(img, orient)  # calls function defined below (which does all the work)
    print("new size: ", new_img.size)
    target_path = os.path.join(new_folder, img_name_new)
    new_img.save(target_path, "PNG")  # save processed image to target folder


# function that does the processing
def crop_to_size(img, orient):

    w, h = img.size
    short = min([w, h])
    long = max([w, h])
    print("dev. ratio orig: ", long/short - 4/3)   # deviation from expected ratio (in pixels)
    mybox = (0, 0, img.size[0], img.size[1])       # original box (see PIL coord system)
    midpoint = (w / 2, h / 2)

    if orient == "landscape":
        target_size = (800, 600)
        if long/short > 4/3:
            print("crop width")
            new_half_w = short * 2 / 3
            mybox = (midpoint[0] - new_half_w, mybox[1], midpoint[0] + new_half_w, mybox[3])
        else:
            print("crop height")
            new_half_h = long * 3 / 8
            mybox = (mybox[0], midpoint[1] - new_half_h, mybox[2], midpoint[1] + new_half_h)

    else:  # portrait
        target_size = (600, 800)
        if long/short > 4/3:
            print("crop height")
            new_half_h = short * 2 / 3
            mybox = (mybox[0], midpoint[1] - new_half_h, mybox[2], midpoint[1] + new_half_h)
        else:
            print("crop width")
            new_half_w = long * 3 / 8
            mybox = (midpoint[0] - new_half_w, mybox[1], midpoint[0] + new_half_w, mybox[3])

    return img.resize(target_size, box=mybox)


img_list = os.listdir(old_folder)
for im in img_list:
    edit_save(im)
