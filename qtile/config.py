from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Match, Screen
from libqtile.config import Key as K
from libqtile.lazy import lazy
import subprocess

m = "mod4"

def launch_keys():
    name = lambda x: f"Launch {x}"
    lk = [
        K([m], "Return", lazy.spawn("kitty"), desc=name("kitty terminal")),
        K([m], "u", lazy.spawn("google-chrome-stable"), desc=name("chrome")),
        K([m], "i", lazy.spawn("kitty nvim"), desc=name("nvim")),
        K([m], "o", lazy.spawn("kitty ranger"), desc=name("ranger file explorer")),
        K([m], "p", lazy.spawncmd(), desc=name("command")),
    ]
    return lk

def admin_keys():
    ak = [
        K([m, "control"], "r", lazy.reload_config(), desc="Reload config"),
        K([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set 5%+"),
            desc="Increase brightness"),
        K([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 5%-"),
            desc="Decrease brightness"),
        K([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q sset Master 5%+"),
            desc="Increase volume"),
        K([], "XF86AudioLowerVolume", lazy.spawn("amixer -q sset Master 5%-"),
            desc="Decrease volume"),
    ]
    return ak

def layout_keys():
    lok = [
        K([m, "shift"], "Return", lazy.layout.toggle_split(), 
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
    layout.MonadTall(padding=5),
    layout.MonadWide(padding=5),
    layout.Matrix(padding=5),
]

custombar1 = bar.Bar([
    widget.Clock(),
    widget.Prompt(),
], 30)

screens = [
    Screen(top=custombar1)
]

mouse = [
    Drag([m], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position(), 
        desc="Drag & set floating window position"),
    Click([m], "Button2", lazy.window.bring_to_front(), 
        desc="Click to bring floating window to front"),
]
