import pywhatkit as kit
import time
import pandas as pd
import random
from datetime import datetime
import pyautogui

# Your crush's WhatsApp number
CRUSH_NUMBER = "+91XXXXXXXXXX"


# Load pickup lines from CSV
df = pd.read_csv("pickup_lines.csv")
pickup_lines = df["Pickup Line"].dropna().tolist()
random.shuffle(pickup_lines)  # Shuffle to randomize order

if pickup_lines:
    message = pickup_lines.pop(0).strip('"')  # Take the first unique one
    print(f"Generated Rizz: {message}")

    # Send it 1 minute from now (because pywhatkit needs lead time)
    now = datetime.now()
    hour = now.hour
    minute = now.minute + 1

    print(f"Sending message at {hour}:{minute} → {message}")
    kit.sendwhatmsg(CRUSH_NUMBER, message, hour,
                    minute, wait_time=10, tab_close=True)

    # Wait for message to be typed in
    print("Waiting for WhatsApp Web to load and message to be typed...")
    time.sleep(18)

    pyautogui.hotkey("alt", "tab")
    time.sleep(1)

    #  Press Enter to send
    pyautogui.press("enter")
    print("💌 Message sent!")
else:
    print("No pickup lines left to send.")
