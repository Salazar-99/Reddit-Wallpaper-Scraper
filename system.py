import os
from PIL import Image    

#To prevent saving too many large images, maintain only the 10 most recent ones
def clean_directory(directory):
    if len(os.listdir(directory)) >= 10:
        oldest_image = get_oldest_image(directory)
        os.remove(directory + '/' + oldest_image)

def get_oldest_image(directory):
    images = os.listidr(directory)
    oldest = 0
    for i in len(range(images)):
        if os.path.getmtime(images[i]) < os.path.getmtime(images[oldest]):
            oldest = i
    return images[oldest]

#Set wallpaper to most recent scraped image
def set_wallpaper(image_path):
    os.system('/usr/bin/gsettings set org.gnome.desktop.background picture-uri ' + image_path)

#Resizes image and saves it
def resize_image(image_path):
    image = Image.open(image_path)
    image = image.resize((1920,1080))
    image = image.save(image_path)