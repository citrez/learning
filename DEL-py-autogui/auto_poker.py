import pyautogui

# im1 = pyautogui.screenshot()
# im1.save('my_screenshot.png')
# im2 = pyautogui.screenshot('my_screenshot2.png')

screenWidth, screenHeight = pyautogui.size() # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
currentMouseX, currentMouseY = pyautogui.position() # Returns two integers, the x and y of the mouse cursor's current position.
def main():
    pyautogui.moveTo(747, 42) # Move the mouse to the x, y coordinates 100, 150.
    pyautogui.click(button = 'right') 

def check():
    x = 630
    y = 700
    pyautogui.moveTo(x, y)
    pyautogui.click() 
    return None

def fold():
    x = 630
    y = 700
    pyautogui.moveTo(x, y)
    pyautogui.click() 



def call():
    x = 750
    y=700
    pyautogui.moveTo(x, y)
    pyautogui.click() 


    pass

def bet():
    pass

def screenshot():
    im = pyautogui.screenshot(region=(0,0, 300, 400))
    im.save('temp.png')

    pass

if __name__ == '__main__':
    img = pyautogui.screenshot(region=(0,0, 300, 400))
    img.save('temp.png')
    # img = img.convert('RGB')
    # img.save('temp.jpg')