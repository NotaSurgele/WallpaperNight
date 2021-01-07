# WallpaperNight
Change the wallpaper automatically, depending on the hour. So you can swap between lighter and darker wallpaper

## How to use it ?
Simply put the path of your picture in a variable, like this for example:
```
wallpaper1 = "/home/user/path/to/image"
wallpaper2 = "/home/user/path/to/image"
...
```
Then, change the if condition on the main
```
while True:
        if (condition):
            setwallpaper(wallpaper1, plugin='org.kde.image')
        else:
            setwallpaper(wallpaper2, plugin='org.kde.image')
    time.sleep(3600)
```
time.sleep(nb) stop the program for nb seconds..

And then just execute the program:
```
./kwallpaperswap.py || python kwallpaperswap.py
```
