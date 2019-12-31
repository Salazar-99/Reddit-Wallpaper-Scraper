from scraper import *
from system import *

wallpaper_directory = #Path to the directory where you would like images stored
clean_directory(wallpaper_directory)
image_path = get_wallpaper(wallpaper_directory)
resize_image(image_path)
set_wallpaper(image_path)