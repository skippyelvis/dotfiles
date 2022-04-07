from libqtile import layout, bar, widget
from libqtile.config import Click, Drag, Group, Match, Screen
from libqtile.config import Key as K, KeyChord as KC
from libqtile.lazy import lazy
from utils import incbrightness, incvolume, rand_wallpaper, spawnesc 

# my comfy qtile config

m = "mod4"
# terminal = "st"
terminal = "kitty"

def launchcmd(cmd):
    if terminal == "st":
        return f"st -e sh -c '{cmd}; exec bash'"
    elif terminal == "kitty":
        return f"kitty {cmd}"

def launch_keys():
    name = lambda x: f"Launch {x}"
    lk = [
        K([m], "Return", lazy.spawn(terminal), desc=name("terminal emulator")),
        K([m, "shift"], "Return", lazy.spawn("google-chrome-stable"), desc=name("chrome")),
        K([m], "p", lazy.spawncmd(), desc=name("command")),
        KC([m], "0", [
            K([], "t", *spawnesc(terminal)),
            K([], "c", *spawnesc("google-chrome-stable")),
            K([], "n", *spawnesc(launchcmd("nvim"))),
            K([], "r", *spawnesc(launchcmd("ranger"))),
            K([], "m", *spawnesc("google-chrome-stable outlook.office.com/mail/")),
        ], mode="Launch")
    ]
    return lk

def admin_keys():
    ak = [
        K([m, "control"], "r", lazy.reload_config(), desc="Reload config"),
        K([m, "control"], "q", lazy.shutdown(), desc="Shutdown"),
        K([], "XF86MonBrightnessUp", lazy.spawn(incbrightness("mon", 5)),
            desc="Increase brightness"),
        K([], "XF86MonBrightnessDown", lazy.spawn(incbrightness("mon", -5)),
            desc="Decrease brightness"),
        K([], "XF86KbdBrightnessUp", lazy.spawn(incbrightness("kbd", 5)),
            desc="Increase brightness"),
        K([], "XF86KbdBrightnessDown", lazy.spawn(incbrightness("kbd", -5)),
            desc="Decrease brightness"),
        K([], "XF86AudioRaiseVolume", lazy.spawn(incvolume(2)),
            desc="Increase volume"),
        K([], "XF86AudioLowerVolume", lazy.spawn(incvolume(-2)),
            desc="Decrease volume"),
        K([], "XF86AudioMute", lazy.spawn("amixer -q sset Master 0%"),
            desc="Mute volume"),
        K([], "XF86Sleep", lazy.spawn("lockscreen.sh"), desc="Lock screen"),
        KC([m], "s", [
            K([], "w", *spawnesc("nm-connection-editor"), desc="Network settings")
        ], mode="Settings")
    ]
    return ak

def layout_keys():
    lok = [
        K([m, "shift"], "Tab", lazy.layout.toggle_split(), 
            desc="Toggle b/t split and unsplit stacks"),
        K([m], "Tab", lazy.next_layout(), desc="Switch to next layout")
    ]
    return lok

def move_focus_keys():
    h = lazy.layout.left()
    j = lazy.layout.down()
    k = lazy.layout.up()
    l = lazy.layout.right()
    name = lambda x: f"Move focus to window {x}"
    mk = [
        K([m], "h", h, desc=name("left")),
        K([m], "j", j, desc=name("down")),
        K([m], "k", k, desc=name("up")),
        K([m], "l", l, desc=name("right")),
        K([m], "space", lazy.layout.next(), desc=name("next")),
        K([m], "q",     lazy.window.kill(), desc="Kill window"),
    ]
    return mk

def move_window_keys():
    h = lazy.layout.shuffle_left()
    j = lazy.layout.shuffle_down()
    k = lazy.layout.shuffle_up()
    l = lazy.layout.shuffle_right()
    name = lambda x: f"Move window {x}"
    mwk = [
        K([m, "shift"], "h", h, desc=name("left")),
        K([m, "shift"], "j", j, desc=name("down")),
        K([m, "shift"], "k", k, desc=name("up")),
        K([m, "shift"], "l", l, desc=name("right")),
    ]
    return mwk

def grow_window_keys():
    h = lazy.layout.grow_left()
    j = lazy.layout.grow_down()
    k = lazy.layout.grow_up()
    l = lazy.layout.grow_right()
    name = lambda x: f"Grow window {x}"
    gk = [
        K([m, "control"], "h", h, desc=name("left")),
        K([m, "control"], "j", j, desc=name("down")),
        K([m, "control"], "k", k, desc=name("up")),
        K([m, "control"], "l", l, desc=name("right")),
        K([m, "control"], "n", lazy.layout.normalize(), desc="Reset window size(s)")
    ]
    return gk

def group_control_keys(groups):
    gck = []
    for i, group in enumerate(groups):
        gname = group.name
        gkey = str(i+1)
        gck.extend([
            K([m],            gkey, lazy.group[gname].toscreen(),
                desc=f"Switch to group {gname}"),
            K([m, "shift"],   gkey, lazy.window.togroup(gname, switch_group=True),
                desc=f"Switch to group {gname} & bring focused window"),
            K([m, "control"], gkey, lazy.window.togroup(gname),
                desc=f"Send focused window to group {gname}")
        ])
    return gck

groups = [Group(x) for x in 'ABCDE']

keys = [
    *launch_keys(),
    *admin_keys(),
    *layout_keys(),
    *move_focus_keys(),
    *move_window_keys(),
    *grow_window_keys(),
    *group_control_keys(groups),
]

layouts = [
    layout.MonadTall(margin=2),
    layout.MonadWide(margin=2),
]


custombar1 = bar.Bar([
    widget.Clock(),
    widget.GroupBox(),
    widget.Prompt(),
    widget.Spacer(),
    widget.Chord(),
    widget.Wlan(format="<b>{essid}!</b>", mouse_callbacks={
        "Button1": lazy.spawn("nm-connection-editor")
        }),
], 30)

screens = [
    Screen(top=custombar1, wallpaper=rand_wallpaper(), wallpaper_mode="fill")
]

mouse = [
    Drag([m], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position(), 
        desc="Drag & set floating window position"),
    Click([m], "Button2", lazy.window.bring_to_front(), 
        desc="Click to bring floating window to front"),
]
