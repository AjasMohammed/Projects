import pyautogui
from PIL import Image, ImageGrab
import time
# from numpy import asarray


# press key automatically
def hit(key):
    pyautogui.press(key)
    return


# chcks if day or night
def check_day(data):
    for i in range(490, 520):
        for j in range(130, 180):
            if data[i, j] > 100:
                return True
    return False


# checks if an obstacle is closing
def is_collide(data):
    for i in range(210, 250):
        for j in range(330, 420):
            if data[i, j] < 100:
                hit('down')  # ducks
                return
    for i in range(300, 350):
        for j in range(450, 500):
            if data[i, j] < 100:
                hit('up')  # jumps
                return

    return


def night_collide(data):
    for i in range(210, 250):
        for j in range(300, 420):
            if data[i, j] > 100:
                hit('down')  # ducks
                return
    for i in range(300, 350):
        for j in range(450, 500):
            if data[i, j] > 100:
                hit('up')  # jumps
                return

    return


if __name__ == "__main__":
    print("Game About to begin.....")

    time.sleep(3)
    hit('up')  # starts the game
    while True:
        image = ImageGrab.grab().convert('L')  # takes screenshot in black and white
        data = image.load()

        if check_day(data):
            is_collide(data)
        else:
            night_collide(data)

        # print(asarray(image))

         # checks cactus

        # checks for night
        # for i in range(490, 520):
        #     for j in range(130, 180):
        #         data[i, j] = 100
        #
        # image.show()
        # break
