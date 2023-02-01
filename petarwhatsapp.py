# vamos a utilizar una libreria llamada pyautogui

import pyautogui
import time

time.sleep(4)
# esperamos 4 segundos para entrar al navegador
count = 0
while count <= 10:
    pyautogui.typewrite("GOL DE RAPHINHAAAAA")
    pyautogui.press("enter")
    count = count + 1
