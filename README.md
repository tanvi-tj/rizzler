# rizzler 💌

A tiny Python script to automatically send flirty messages on WhatsApp - [Reel Link](https://www.instagram.com/reel/DJ_Ydd6IjW-/)
---

## What is this?

This script opens WhatsApp Web, types out a pickup line from a CSV file, and sends it to your crush — completely on its own.

It uses:
- `pywhatkit` → to open WhatsApp Web and type the message
- `pyautogui` → to hit enter and actually send it

---

## Files in this repo

- `rizzler.py` → sends a single message (great for testing)
- `pickup_lines.csv` → a bunch of flirty lines you can customize or add to

---

## How to use

### 1. Install dependencies
```
pip install pywhatkit pyautogui pandas
```

### 2. Replace number

Then, open `rizzler.py` and replace the placeholder number with the actual phone number (including country code) of the person you want to message:

```CRUSH_NUMBER = "+91XXXXXXXXXX"```

### 3. Run the script

Once that’s done, make sure you're already logged into WhatsApp Web in your browser and run the script:

```python rizzler.py```

Make sure:

- You’re logged into WhatsApp Web in your browser
- Chrome is your default browser (works best with pywhatkit)
- Your screen is on and not locked

---

## Want to schedule it every hour from 10 AM to 10 PM?

Modify your loop like this in a scheduler script:

```
for hour in range(10, 23):  # 10 AM to 10 PM
    # send message
    # ...
    time.sleep(3600)  # wait for an hour before next one
```

---

## Automate it Daily

If you want this script to start every day at 10 AM automatically:

### On Mac/Linux:
Use cron. Run crontab -e and add:

```
0 10 * * * /usr/bin/python3 /full/path/to/rizzler.py
```
`/usr/bin/python3` May depend on your machine


### On Windows:

Use Task Scheduler.
- Trigger: Daily at 10:00 AM
- Action: Start a program → choose your Python path
- Add arguments: "C:\full\path\to\rizzler.py"

---

## A few things to keep in mind

- You need to stay logged in on WhatsApp Web.
- Your system needs to stay awake during the time messages are sent.
- This won’t work on cloud platforms (like PythonAnywhere) because pyautogui needs a real GUI.
