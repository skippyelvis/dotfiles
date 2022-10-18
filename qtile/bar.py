from libqtile import bar, widget
from libqtile.widget import base
import os
import subprocess

class Battery(base.ThreadPoolText):

    def __init__(self, **config):
        super().__init__("", **config)
        self.update_interval = 1

    def format_output(self, text):
        status_map = {
            "Charging": "",
            "Discharging": "",
            "Full": "⚡"
        }
        colors = [
            [10, "#c4456b"],  # pinkish red
            [20, "#c46945"],  # orange red
            [30, "#c4af45"],  # yellow
            [75, "#4587c4"],  # soft blue
            [90, "#5ac445"],  # green
            [100, "#b545c4"], # pink
        ]
        level = int(text[1][:-1])
        color = ""
        for l, c in colors:
            if l > level:
                color = c
                break
        span = '<span foreground="{}">{}</span>'
        label = f"{status_map[text[0]]}{text[1]}"
        return span.format(color,label)

    def poll(self):
        script = os.path.expanduser("~/cli/battery.sh")
        run = subprocess.run([script, "info"], capture_output=True)
        text = run.stdout.decode().strip().split(" ")
        return self.format_output(text)

class Volume(base.ThreadPoolText):

    def __init__(self, **config):
        super().__init__("", **config)
        self.update_interval = 1

    def format_output(self, text):
        status_map = {
            0: "婢",
            25: "",
            50: "",
            75: "",
            100: ""
        }
        level = text[0]
        level_key = int(level[:-1])
        level_key = level_key - (level_key%25)
        return status_map[level_key]

    def poll(self):
        script = os.path.expanduser("~/cli/volume.sh")
        run = subprocess.run([script], capture_output=True)
        text = run.stdout.decode().strip().split(" ")
        return self.format_output(text)

class S76GraphicsMode(base.ThreadPoolText):

    def __init__(self, **config):
        super().__init__("", **config)
        self.update_interval = 1

    def format_output(self, text):
        status_map = {
            "compute": "ﴰ",
            "hybrid": "",
            "integrated": "ﳝ",
            "nvidia": "ﬨ"
        }
        return status_map[text[0]]

    def poll(self):
        script = ["system76-power", "graphics"]
        run = subprocess.run(script, capture_output=True)
        text = run.stdout.decode().strip().split(" ")
        return self.format_output(text)

custombar = bar.Bar([
    widget.CurrentLayout(),
    widget.GroupBox(),
    widget.Prompt(),
    widget.Chord(),
    widget.Spacer(),
    widget.Clock(),
    widget.Spacer(),
    S76GraphicsMode(
        font="HeavyData Nerd Font", 
        markup=True,
        fontsize=20,
    ),
    Volume(
        font="DroidSansMono Nerd Font",
        markup=True,
        fontsize=20,
    ),
    Battery(
        markup=True,
        fontsize=20,
    ),
    widget.QuickExit()
], 36)
