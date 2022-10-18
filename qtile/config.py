from libqtile import layout, hook
from libqtile.config import Click, Drag, Group, Screen
from libqtile.lazy import lazy
from keys import makekeys
from util import randwallpaper
from bar import custombar
import os
import subprocess

mod = "mod4"
terminal = "kitty" 
browser = "google-chrome-stable"

follow_mouse_focus = False   
bring_front_click = True
cursor_warp = False
auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "qtile"

@hook.subscribe.startup_complete
def autostart():
    script = os.path.expanduser("~/dotfiles/autostart.sh")
    subprocess.run([script])

# set up the groups/workspaces
groups = [Group(i) for i in "ABC"]

# initialize keymap
keys = makekeys(mod, terminal, browser, groups)

# which layouts we want to use
layouts = [
    layout.Bsp(
        margin=5,
        border_focus="#4ba8cc",
        border_normal="#8b60b3",
        border_width=2,
    ),
    layout.Zoomy(margin=3),
]

# screen has bottom bar and random wallpaper
screens = [
    Screen(bottom=custombar, wallpaper=randwallpaper(), wallpaper_mode="fill"),
    Screen(wallpaper=randwallpaper(), wallpaper_mode="fill")
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", 
        lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", 
        lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

