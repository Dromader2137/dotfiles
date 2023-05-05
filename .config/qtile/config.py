from libqtile import bar, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import PowerLineDecoration

###------------------------------------------###

mod = "mod4"
terminal = "kitty"

###------------------------------------------###

keys = [
    Key([mod], "j", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "k", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "i", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.flip(), desc="Flip"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "z", lazy.spawn("pcmanfm"), desc="Launch pcmanfm"),
    Key([mod, "shift"], "w", lazy.spawn("firefox"), desc="Launch web browser (Firefox)"),
    Key([mod, "shift"], "s", lazy.spawn("flameshot gui"), desc="Launch Flameshot"),
    Key([mod, "shift"], "d", lazy.spawn("discord"), desc="Launch Discord"),
    Key([mod, "shift"], "g", lazy.spawn("lutris"), desc="Launch Lutris"),
    Key([mod, "shift"], "b", lazy.spawn("blender"), desc="Launch Blender"),
    Key([mod, "shift"], "i", lazy.spawn("gimp"), desc="Launch Gimp"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),

    Key([mod, "control", "shift"], "q", lazy.spawn("shutdown now"), desc="Shutdown PC"),
    Key([mod, "control", "shift"], "r", lazy.spawn("reboot"), desc="Reboot PC"),
]

###------------------------------------------###

groups = [Group(i) for i in "12345678"]

for i in groups:
    keys.extend(
        [
            Key([mod],i.name,lazy.group[i.name].toscreen(),desc="Switch to group {}".format(i.name)),
            Key([mod, "shift"],i.name,lazy.window.togroup(i.name, switch_group=True),desc="Switch to & move focused window to group {}".format(i.name)),
            Key([mod, "control"],i.name,lazy.window.togroup(i.name, switch_group=False),desc="Move focused window to group {}".format(i.name))
        ]
    )

###------------------------------------------###

layouts = [
    layout.MonadTall(border_width=2, border_focus="#686868", border_normal="#282a36", margin=10, ratio=0.55),
]

###------------------------------------------###

widget_defaults = dict(
    font="mononoki bold",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

###------------------------------------------###

pl = {
    "decorations": [
        PowerLineDecoration(path="rounded_left")
    ]
}
pr = {
    "decorations": [
        PowerLineDecoration(path="rounded_right")
    ]
}

###------------------------------------------###

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Clock(format="%d/%m", fmt="  {}" ,font = "mononoki bold", background = "#F3F99D", foreground = "#282a36", margin = 4, **pl),
                widget.Clock(format="%H:%M", fmt=" {} " ,font = "mononoki bold", background = "#57c7ff", foreground = "#282a36", **pr),
                widget.Spacer(),
                widget.GroupBox(active="#F1F1F0", inactive="#DFE0DB", highlight_method="block", margin = 3, 
                                font = "mononoki bold", this_current_screen_border = "#686868", padding = 3,
                                this_screen_border = "#686868", fmt="{}"),
                widget.Spacer(**pr),
                widget.PulseVolume(font = "mononoki bold", background = "#F3F99D", foreground = "#282a36", device="PulseAudio", **pl),
                widget.Battery(format = "{percent:2.0%}", fmt=" {}", background = "#5AF78E", foreground = "#282a36", font = "mononoki bold", update_interval = 15),
                widget.TextBox(fmt = "", background = "#5AF78E", foreground = "#282a36", **pr, padding = 3),
                widget.DF(visible_on_warn=False, format="{uf}GB", fmt = " {}  ", font = "mononoki bold", background = "#FF5C57", foreground = "#282a36", partition="/home"),
            ],
            24,
            margin = [10, 10, 0, 10],
            background = "#282a36",
            opacity = 0.9,
        ),
        wallpaper='~/.config/qtile/Wallpaper.png',
        wallpaper_mode='fill',
    ),
    Screen(
        top=bar.Bar(
            [
                widget.Clock(format="%d/%m", fmt="  {}" ,font = "mononoki bold", background = "#F3F99D", foreground = "#282a36", margin = 4, **pl),
                widget.Clock(format="%H:%M", fmt=" {} " ,font = "mononoki bold", background = "#57c7ff", foreground = "#282a36", **pr),
                widget.Spacer(),
                widget.GroupBox(active="#F1F1F0", inactive="#DFE0DB", highlight_method="block", margin = 3, 
                                font = "mononoki bold", this_current_screen_border = "#686868", padding = 3,
                                this_screen_border = "#686868", fmt="{}"),
                widget.Spacer(**pr),
                widget.PulseVolume(font = "mononoki bold", background = "#F3F99D", foreground = "#282a36", device="PulseAudio", **pl),
                widget.Battery(format = "{percent:2.0%}", fmt=" {}", background = "#5AF78E", foreground = "#282a36", font = "mononoki bold", update_interval = 15),
                widget.TextBox(fmt = "", background = "#5AF78E", foreground = "#282a36", **pr, padding = 3),
                widget.DF(visible_on_warn=False, format="{uf}GB", fmt = " {}  ", font = "mononoki bold", background = "#FF5C57", foreground = "#282a36", partition="/home"),
            ],
            24,
            margin = [10, 10, 0, 10],
            background = "#282a36",
            opacity = 0.9,
        ),
        wallpaper='~/.config/qtile/Wallpaper.png',
        wallpaper_mode='fill',
    ),
]

###------------------------------------------###

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

###------------------------------------------###

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None
wmname = "Qtile"
