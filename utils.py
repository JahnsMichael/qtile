import subprocess

def xrandr():
    monitors = get_monitors(True)
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
