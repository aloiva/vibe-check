import random as rand
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from PIL import Image
#import msvcrt as m
import time


HAPPIER = "happier.txt"
HAPPY = "happy.txt"
NEUTRAL = "neutral.txt"
SAD = "sad.txt"
SADDER = "sadder.txt"
CATS = 20
HAMSTERS = 16
BUNNIES = 10
YES = ["yes", "yep", "y"]
NO = ["no", "nope", "n"]


def main():
    print_welcome_message()
    while True:
        text = verified_input() 
        if text == "exit":
            break
        score = analyser(text)
        print("Happiness score is", score)
        wait()
        print_emoticon(score)
        animalyser(score)



def analyser(text):
    '''
    "store" is a dictionary with 4 pairs of keys and values, namely positive index, negative index, neutral index and compound value. This function returns compound value.
    '''
    score = SentimentIntensityAnalyzer().polarity_scores(text)
    return score["compound"]


def print_emoticon(score):
    filename = "assets/emoticons/" + get_scale(score)
    print("Emoticon that (hopefully) represents the mood is  ", random_line_from(filename))
    wait()


def random_line_from(filename):
    '''
    this function makes a list of all the lines and returns a random choice from the list
    '''
    with open(filename, encoding="utf8") as f:
        lines = [line.rstrip("\n") for line in f]
    return rand.choice(lines)


def get_scale(score):
    if score >= 0.5:
        return HAPPIER
    elif score < 0.5 and score > 0:
        return HAPPY
    elif score < 0 and score > -0.5:
        return SAD
    elif score <= -0.5:
        return SADDER
    else:
        return NEUTRAL


def animalyser(score):
    if score<0:
        print("Time for a few questions now.")
        print("Do you like cats?")
        ans = yes_or_no()
        if ans in YES:
            imgprnt("cats")
        elif ans in NO:
            print("Or perhaps hamsters..?")
            ans = yes_or_no()
            if ans in YES:
                imgprnt("hamsters")
            elif ans in NO:
                print("Good gracious! At least bunnies? ")
                ans=yes_or_no()
                if ans in YES:
                    imgprnt("bunnies")
                elif ans in NO:
                    print("The first person to ever not like any of the three cutest animal ever, have a nice day ahead.")

    if score>0:
        print("Positive happiness score is a positive sign in life, keep up the good mood!")


def imgprnt(key):
    filename = "assets/img/" + key + "/"
    rand.seed(time.time())
    if key == "cats":
        filename = filename + str(rand.randint(1,CATS)) + ".jpg"
    elif key == "hamsters":
        filename = filename + str(rand.randint(1,HAMSTERS)) + ".jpg"
    elif key == "bunnies":
        filename = filename + str(rand.randint(1,BUNNIES)) + ".jpg"
    img = Image.open(filename)
    print("Here, have a", key, "picture to compensate for the negative happiness score.")
    img.show()


def print_welcome_message():
    print("Welcome to Vibe Check!!!")
    wait()
    print("The program takes input from you (the user!) and analyse the mood of the text.")
    wait()
    print("Emoticons that (hopefully) represent mood of the text will then be printed!!")
    wait()
    print("Enter exit to exit the program.")


def verified_input():
    text=input("txt > ")
    while(text.strip()==""):
        text = input("txt > ")
    return text


def yes_or_no():
    ans = input("> ")
    while ans.lower() not in YES and ans.lower() not in NO:
        ans = input("> ")
    return ans.lower()

def wait():
    time.sleep(2)


if __name__ == "__main__":
    main()