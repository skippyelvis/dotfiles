import os
import subprocess
import random

def scall(cmd):
    return subprocess.call(cmd.split(" "))

def magdlt(inc):
    mag = abs(inc)
    dlt = "+" if inc > 0 else "-"
    return mag, dlt

device_map = {
        "mon": "intel_backlight",
        "kbd": "system76_acpi::kbd_backlight",
}

def incbrightness(d, inc):
    cmd = "brightnessctl -d {} set {}%{}"
    mag, dlt = magdlt(inc)
    dev = device_map[d]
    return cmd.format(dev, mag, dlt)

def incvolume(inc):
    cmd = "amixer -q sset Master {}%{}"
    return cmd.format(*magdlt(inc))

def rand_wallpaper():
    d = "/home/homieja/Pictures/wallpapers/"
    f = os.listdir(d)
    r = random.randint(0, len(f)-1)
    return os.path.join(d, f[r])

def set_rand_wallpaper():
    p = rand_wallpaper()
    cmd = f"feh --bg-scale {p}"
    return cmd
