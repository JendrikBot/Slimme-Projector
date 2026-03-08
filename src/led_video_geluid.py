from gpiozero import DigitalInputDevice, LED
from signal import pause
import subprocess
import os
import threading
import time
import signal

GPIO_SOUND = 17
GPIO_LED = 27

VIDEO = "/home/wokkel/kalmeer_video_2.mp4"
LOCK_TIME = 60  # 1 minuut projectie + lockout

# LM393 is meestal active-low → pull_up=True
sensor = DigitalInputDevice(GPIO_SOUND, pull_up=True)
led = LED(GPIO_LED)

locked = False
player = None
timer = None


def stop_show():
    """Stop video + LED en maak systeem weer klaar voor nieuwe trigger."""
    global locked, player, timer

    # Stop mpv als het nog draait
    if player and player.poll() is None:
        try:
            # We starten mpv in z'n eigen process group -> killpg stopt mpv netjes/hard
            os.killpg(player.pid, signal.SIGTERM)
        except Exception:
            pass

    player = None
    timer = None
    led.off()
    locked = False
    print(" 1 minuut voorbij -> video uit, LED uit, weer klaar")


def triggered():
    global locked, player, timer

    if locked:
        print("Trigger genegeerd (nog in lock)")
        return

    locked = True
    led.on()
    print(" Trigger -> video START (max 60s)")

    env = os.environ.copy()
    env["DISPLAY"] = ":0"

    # Start mpv fullscreen
    # start_new_session=True => eigen process group (handig om later te stoppen)
    player = subprocess.Popen(
        ["mpv", "--fs", "--no-border", "--really-quiet", "--no-terminal", VIDEO],
        env=env,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )

    # Start 60s timer (nieuwe triggers verlengen dit niet)
    timer = threading.Timer(LOCK_TIME, stop_show)
    timer.start()


sensor.when_activated = triggered

print("Klaar. Wacht op geluid (GPIO17). LED op GPIO27.")
pause()
