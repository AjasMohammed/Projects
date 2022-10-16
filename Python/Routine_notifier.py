from pygame import mixer
import time


def music_loop():  # function to play music
    mixer.init()
    mixer.music.load("song.mp3")  # add name of music.
    mixer.music.play(-1)
    while True:
        print("Enter yes if you are done.")
        user_inp = input("Are you done : ").lower()
        if user_inp == "yes":
            mixer.music.stop()  # stops music and exit from the function
            break


if __name__ == "__main__":

    exercise = time.time()  # set to the current time.
    eat = time.time()
    drink = time.time()

    exercise_time = 30*60  # interval of time in Hours.
    eat_time = 25*60
    drink_time = 10*60

    while True:
        if time.time() - exercise > exercise_time:  # checks if the interval is passed.
            print("Time to Exercise.")
            music_loop()
            sleep = time.time()  # reset the time.

        if time.time() - eat > eat_time:
            print("Time to Eat.")
            music_loop()
            eat = time.time()

        if time.time() - drink > drink_time:
            print("Time to Drink Water.")
            music_loop()
            drink = time.time()
