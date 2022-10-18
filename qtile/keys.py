from libqtile.config import KeyChord, Key as K
from libqtile.lazy import lazy

def spawnesc(cmd):
    out = [
        lazy.spawn(cmd),
        lazy.spawn("xdotool key Escape")
    ]
    return out

def makekeys(m, term, browser, groups):
    # basic 
    quick = [
        K([m], "Return", lazy.spawn(term), desc=f"Launch {term}"),
        K([m, "shift"], "Return", lazy.spawn(browser), desc=f"Launch {browser}"),
        K([m], "s", lazy.spawn(f"slack"), desc="Launch slack-desktop"),
        K([m], "q", lazy.window.kill(), desc="Quit focused window"),
        K([m, "control"], "r", lazy.reload_config(), desc="Reload qtile config"),
        K([m, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
        K([m], "0", lazy.spawncmd(), desc="Spawn command"),
        K([m], "minus", lazy.spawn("i3lock"), desc="Lock screen"),
        K([m], "Tab", lazy.next_layout(), desc="Next layout"),
        K([m], "[", lazy.spawn("brightness.sh inc 5"), desc="Raise brightness"),
        K([m], "]", lazy.spawn("brightness.sh dec 5"), desc="Raise brightness"),
    ]

    # launch mode
    launch = KeyChord([m], "space", [
        K([], "Return", lazy.spawn(term), desc=f"Launch {term}"),
        K(["shift"], "Return", lazy.spawn(browser), desc=f"Launch {browser}"),
        K([], "r", lazy.spawn(f"{term} ranger"), desc="Launch ranger"),
        K([], "s", lazy.spawn(f"slack"), desc="Launch slack-desktop"),
        K([], "n", lazy.spawn(f"{term} nvim"), desc="Launch nvim"),
        K([], "f", lazy.spawn(f"nautilus"), desc="Launch nautilus"),
        K(["shift"], "r", spawnesc(f"{term} ranger"), desc="Launch ranger"),
        K(["shift"], "n", spawnesc(f"{term} nvim"), desc="Launch nvim"),
        K(["shift"], "f", spawnesc(f"nautilus"), desc="Launch nautilus"),
    ], mode="launch mode")

    # moving focus
    focus = [
        K([m], "h", lazy.layout.left(), desc="Move focus left"),
        K([m], "j", lazy.layout.down(), desc="Move focus down"),
        K([m], "k", lazy.layout.up(), desc="Move focus up"),
        K([m], "l", lazy.layout.right(), desc="Move focus right"),
    ]

    # adjustment mode
    adjust = KeyChord([m], "a", [
        K([], "Tab", lazy.next_layout(), desc="Next layout"),
        K([], "q", lazy.layout.left(), desc="Move focus left"),
        K([], "w", lazy.layout.down(), desc="Move focus down"),
        K([], "e", lazy.layout.up(), desc="Move focus up"),
        K([], "r", lazy.layout.right(), desc="Move focus right"),
        K([], "h", lazy.layout.grow_left(), desc="Grow left"),
        K([], "j", lazy.layout.grow_down(), desc="Grow down"),
        K([], "k", lazy.layout.grow_up(), desc="Grow up"),
        K([], "l", lazy.layout.grow_right(), desc="Grow right"),
        K([], "n", lazy.layout.normalize(), desc="Normalize windows"),
        K([], "u", lazy.layout.grow(), desc="Grow window"),
        K([], "p", lazy.layout.shrink(), desc="Shrink window"),
        K(["control"], "h", lazy.layout.shuffle_left(), desc="Shuffle left"),
        K(["control"], "j", lazy.layout.shuffle_down(), desc="Shuffle down"),
        K(["control"], "k", lazy.layout.shuffle_up(), desc="Shuffle up"),
        K(["control"], "l", lazy.layout.shuffle_right(), desc="Shuffle right"),
        K(["shift"], "h", lazy.layout.flip_left(), desc="Flip left"),
        K(["shift"], "j", lazy.layout.flip_down(), desc="Flip down"),
        K(["shift"], "k", lazy.layout.flip_up(), desc="Flip up"),
        K(["shift"], "l", lazy.layout.flip_right(), desc="Flip right"),
    ], mode="adjust mode")

    # group management
    groupk = []
    for idx, i in enumerate(groups):
        groupk.extend(
            [
                K(
                    [m],
                    str(idx+1),
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                ),
                K(
                    [m, "shift"],
                    str(idx+1),
                    lazy.window.togroup(i.name, switch_group=True),
                    desc="Switch to & moved window to group {}".format(i.name),
                ),
                K([m, "shift"], str(idx+1), lazy.window.togroup(i.name),
                    desc="Move window to group {}".format(i.name)),
            ]
        )

    keys = [*quick, *focus, launch, adjust, *groupk]
    return keys
