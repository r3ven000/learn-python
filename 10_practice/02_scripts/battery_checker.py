import psutil
import subprocess
import os
import pathlib

flag_1 = pathlib.Path("~/.cache/battery-notify-30")
flag_2 = pathlib.Path("~/.cache/battery-notify-10")

def battery_check():
    if psutil.sensors_battery().power_plugged == True:
        return

    if psutil.sensors_battery().power_plugged == False and psutil.sensors_battery().percent <= 30:
        subprocess.run(["notify-send", "Remaining 30%"])

    pass

if __name__ == "__main__":
    battery_check()
