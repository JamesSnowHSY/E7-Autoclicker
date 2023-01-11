from random import choice
from PIL import Image
import pyautogui
import threading
import os

def check_screen(image_file):
    image_location = pyautogui.locateOnScreen(image_file)
    if image_location:
        return True
    else:
        return False

class E7CurrencyFinder(threading.Thread):

    def __init__(self):
        self.Friendship_Bookmarks = os.path.abspath('./Images/fb.png')
        self.Mystic_Medals = os.path.abspath('./Images/mm.png')
        self.Covenant_Bookmarks = os.path.abspath('./Images/cm.png')

text = "Select the E7 Currencies you wish to find"
title = "E7 Currency Finder"
buttons = ["Friendship Bookmarks", "Covenant Bookmarks", "Mystic Medals"]
e7c_finder1 = pyautogui.confirm(text=text, title=title, buttons=buttons)
e7c_finder2 = pyautogui.confirm(text=text, title=title, buttons=buttons)

prompt_text = "Do you want to find the following E7 Currency?\n\n- {}\n- {}".format(e7c_finder1, e7c_finder2)
buttons = ["Yes", "No"]

choices = pyautogui.confirm(text=prompt_text, title=title, buttons=buttons)

if choices == "Yes":
    print("Searching...")
    e7 = E7CurrencyFinder()
    if e7c_finder1 == "Friendship Bookmarks":
        if check_screen(e7.Friendship_Bookmarks) == True:
            print('Friendship Bookmarks found!')
    elif e7c_finder1 == "Covenant Bookmarks":
        if check_screen(e7.Covenant_Bookmarks) == True:
            print('Covenant Bookmarks found!')
    elif e7c_finder1 == "Mystic Medals":
        if check_screen(e7.Mystic_Medals) == True:
            print('Mystical Medals found!')
    if e7c_finder2 == "Friendship Bookmarks":
        if check_screen(e7.Friendship_Bookmarks) == True:
            print('Friendship Bookmarks found!')
    elif e7c_finder2 == "Covenant Bookmarks":
        if check_screen(e7.Covenant_Bookmarks) == True:
            print('Covenant Bookmarks found!')
    elif e7c_finder2 == "Mystic Medals":
        if check_screen(e7.Mystic_Medals) == True:
            print('Mystical Medals found!')
    else:
        print('No E7 Currencies found')
elif choices == "No":
    print('User has cancelled search')
else:
    print("Error :<")
