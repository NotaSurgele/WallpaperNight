#!/usr/bin/env python3
from datetime import datetime
import sys
import dbus
import argparse
import time

dark = '/home/alexis/Desktop/Wallpaper/dark1.jpeg'
light = '/home/alexis/Desktop/Wallpaper/light1.jpg'

def setwallpaper(filepath, plugin = 'org.kde.image'):
    jscript = """
    var allDesktops = desktops();
    print (allDesktops);
    for (i=0;i<allDesktops.length;i++) {
        d = allDesktops[i];
        d.wallpaperPlugin = "%s";
        d.currentConfigGroup = Array("Wallpaper", "%s", "General");
        d.writeConfig("Image", "file://%s")
    }
    """
    bus = dbus.SessionBus()
    plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')
    plasma.evaluateScript(jscript % (plugin, plugin, filepath))


if __name__ == '__main__':
    while True:
        if datetime.now().hour < 18 and datetime.now().hour > 8:
            setwallpaper(light, plugin='org.kde.image')
            time.sleep(230)
        else:
            setwallpaper(dark, plugin='org.kde.image')
            time.sleep(230)