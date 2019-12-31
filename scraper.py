import praw
import requests
import re
import os

#Required credentials to make API request, user specific
client_id = #Your client if
secret_key = #Your secret API key
user_agent = #Name of authorized reddit script you created

#Read-only instance of Reddit
reddit = praw.Reddit(client_id=client_id, 
                    client_secret=secret_key, 
                    user_agent=user_agent)

#Retrieves image for wallpaper and returns file path to the image
def get_wallpaper(wallpaper_directory):
    #Directory where images are saved
    save_path = wallpaper_directory
    #Retrieve the top 5 posts in r/EarthPorn sorted by Hot
    posts = reddit.subreddit('EarthPorn').hot(limit=5)
    #Find first post that ends in '.jpg' to avoid stickied posts
    for post in posts:
        if is_jpg(post.url):
            #Create unique file name for the image
            image_name = str(hash(post.id))
            #Specify the path where the image is to be saved
            image_path = os.path.join(save_path, image_name + '.jpg')
            #Save request result which contains the image binary
            result = requests.get(post.url)
            #Save image in a file in designated path
            with open(image_path, 'wb') as file:
                file.write(result.content)
            break
    return image_path

#Function to check if a string ends in '.jpg'
def is_jpg(url):
    if re.search(r".jpg$", url) is not None:
        return True
    else:
        return False
