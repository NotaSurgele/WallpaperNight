#!/usr/bin/env python3
from datetime import datetime
import sys
import dbus
import argparse
import time

class WallpaperSwap:
    
    background_dark  = '/home/alexis/Desktop/Wallpaper/dark1.jpeg'
    background_light = '/home/alexis/Desktop/Wallpaper/light1.jpg'
    plugin           = 'org.kde.image'
    morning          = 8
    evening          = 18

    JSCRIPT = """
        var allDesktops = desktops();
        print (allDesktops);
        for (i=0;i<allDesktops.length;i++) {
            d = allDesktops[i];
            d.wallpaperPlugin = "%s";
            d.currentConfigGroup = Array("Wallpaper", "%s", "General");
            d.writeConfig("Image", "file://%s")
        }"""

    def set_plugin(self, plugin):
        self.plugin = plugin
    
    def set_wallpaper(self, filepath):
        bus = dbus.SessionBus()
        plasma = dbus.Interface(bus.get_object('org.kde.plasmashell', '/PlasmaShell'),
                                dbus_interface='org.kde.PlasmaShell')
        plasma.evaluateScript(WallpaperSwap.JSCRIPT % (self.plugin, self.plugin, filepath))

    def __parse_args(self):
        args = argparse.ArgumentParser()
        args.add_argument("--dark", default=self.background_dark)
        args.add_argument("--light", default=self.background_light)
        args.add_argument("--morning", default=self.morning)
        args.add_argument("--evening", default=self.evening)
        res = p.parse_args(sys.argv)
        self.background_dark, self.background_light, self.morning, self.evening = res.dark, res.light, res.morning, res.evening
        if self.morning > self.evening:
            print("Morning cannot be after evening!", file=sys.stderr)
            sys.exit(2)

    def run(self):
        MINUTE = 60
        HOUR   = 3600
        DAY    = 86400
        
        EVENING = HOUR * self.evening
        MORNING = HOUR * self.morning

        while True:
            current_time = datetime.now().hour * HOUR + datetime.now().minute * MINUTE + datetime.now().second
            if current_time < EVENING and current_time > MORNING:
                self.set_wallpaper(self.background_light)
                time.sleep(EVENING - current_time)
            else:
                self.set_wallpaper(self.background_dark)
                if current_time > EVENING:
                    time.sleep(DAY - current_time + MORNING)
                else:
                    time.sleep(MORNING - current_time)
        
    def __init__(self):
        self.__parse_args()


if __name__ == '__main__':
    WallpaperSwap().run()
