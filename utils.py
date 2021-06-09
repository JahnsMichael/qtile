import subprocess


def xrandr():
    monitors = get_monitors()
    if (len(monitors) > 1):
        cmd = "xrandr "
        for i in range(1, len(monitors)):
            cmd += f"--output {monitors[i]} --auto --right-of {monitors[i-1]} "
        subprocess.call(cmd, shell=True)


def get_monitors(all=False):
    if (all):
        cmd = "xrandr | grep 'connected ' | awk '{ print$1 }'"
    else:
        cmd = "xrandr | grep ' connected ' | awk '{ print$1 }'"
    monitors = subprocess.check_output(
        cmd, shell=True).decode("utf8").splitlines()
    return monitors


def show_keys(keys):
    key_help = ""
    for k in keys:
        mods = ""

        for m in k.modifiers:
            if m == "mod4":
                mods += "Super + "
            else:
                mods += m.capitalize() + " + "

        if len(k.key) > 1:
            mods += k.key.capitalize()
        else:
            mods += k.key

        try:
            key_help += "{:<30} {}".format(mods, k.desc + "\n")
        except AttributeError as e:
            pass

    return key_help
