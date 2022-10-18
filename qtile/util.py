import os
import random

def randwallpaper():
    d = "~/Pictures/wallpapers/"
    d = os.path.expanduser(d)
    f = os.listdir(d)
    c = random.randint(0, len(f)-1)
    return os.path.join(d, f[c])
