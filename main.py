import pyautogui
import time

message = "tugba"
n = 500

print("Start")

count = 5
while(count != 0):
    time.sleep(1)
    count -= 1

print("\n COMPLATE")
for i in range(0, int(n)):
    pyautogui.typewrite(message + "\n")

