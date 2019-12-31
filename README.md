# Reddit-Wallpaper-Scraper
A script to set the top post from reddit.com/r/EarthPorn as your wallpaper on a Unix system

The flow of the script is as follows:
- Clean ```wallpaper-directory``` (delete oldest of 10 images)
- Make a request to Reddit for the top 5 posts on r/EarthPorn via a ```Reddit``` object
- Find the first post ending in ```.jpg``` to avoid stickied posts
- Save the image
- Resize the image (set by default to 1920x1080, this can be changed in ``` resize_image ```)
- Set the image as the desktop background 

Additionally, the script will check the specified ```wallpaper_directory``` before each run and maintains
only the 10 latest images.

In order for the scraper to make API requests you must first authorize a script under your Reddit account by going to
User Settings > Privacy & Security > Manage Third-Party App Authorization and creating an app. This will provide you
with the ```client_id``` and ```secret_key```. The user_agent is the name you specified for your app.

The ```crontab.txt``` file contains a template for a cronjob to run the script every day at noon.
This can of course be modified to any desired interval.

Future development will include a "smart" resize feature to maintain aspect ratio of downloaded images
while still shrinking them down to fit on the display in their entirety.



