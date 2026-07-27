#!/usr/bin/env python3
import psutil
import subprocess
import os
import pathlib

flag_1 = pathlib.Path("~/.cache/battery-notify-30").expanduser()
flag_2 = pathlib.Path("~/.cache/battery-notify-10").expanduser()

def battery_check():
    if psutil.sensors_battery().power_plugged == True:
        flag_1.unlink(missing_ok=True)
        flag_2.unlink(missing_ok=True)
        return

    if psutil.sensors_battery().power_plugged == False and psutil.sensors_battery().percent <= 10:
        if not flag_2.exists():
            subprocess.run(["notify-send", "Remaining 10%"])
            flag_2.touch()

    elif psutil.sensors_battery().power_plugged == False and psutil.sensors_battery().percent <= 30:
        if not flag_1.exists():
            subprocess.run(["notify-send", "Remaining 30%"])
            flag_1.touch()


if __name__ == "__main__":
    battery_check()
