import pyautogui

screen_width, screen_height = pyautogui.size()
print(screen_width, screen_height)

currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)

# play 位置： 17 - 18.5, 总 34 * 9   5.5-6.5


play_btn_x = screen_width * 18.0/34.0
play_btn_y = screen_height * 5.5/9.0
print(play_btn_x, play_btn_y)

pyautogui.moveTo(play_btn_x, play_btn_y, 3)
print(currentMouseX, currentMouseY)

pyautogui.click(play_btn_x, play_btn_y)
pyautogui.click(play_btn_x, play_btn_y)