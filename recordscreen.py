import pyautogui
import cv2
import numpy as np
from datetime import datetime
from pynput import keyboard

screen_width, screen_height = pyautogui.size()
codec = cv2.VideoWriter_fourcc(*"mp4v")
out = None

recording = False

def on_key_release(key):
    global recording, out
    if key == keyboard.Key.esc:
        recording = not recording
        if recording:
            print("Recording...")
            current_time_name = datetime.now().strftime("%Y-%m-%d %H-%M-%S").replace(" ", "_").replace(":", "_")
            file_path = f"{current_time_name}.mp4"
            out = cv2.VideoWriter(file_path, codec, 24.0, (screen_width, screen_height))

def capture_screenshot():
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    if out is not None:
        out.write(frame)

print("Press ESC to record...")
with keyboard.Listener(on_release=on_key_release) as listener:
    while True:
        if recording:
            capture_screenshot()
        elif not recording and out is not None:
            print("Recording stopped. Press ESC to record...")
            out.release()
            out = None
