import random
import time
import Levenshtein
from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk
import threading

sentence = random.choice(["The quick brown fox jumps over the lazy dog.", "Sphinx of black quartz, judge my vow.", "Fifty six big red jet planes zoomed quickly by the tower.",
                          "Big fjords vex quick waltz nymph.", "Bright vixens jump; dozy fowl quack.", "How quickly daft jumping zebras vex.", "Fix problems quickly with galvanized jets."])


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        im = Image.new('RGB', (500, 180), 'white')
        ImageDraw.Draw(im).multiline_text((10, 25), sentence, fill=(
            0, 0, 0), spacing=5, align='left')
        render = ImageTk.PhotoImage(im)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)


class Worker(threading.Thread):
    def run(self):
        root = Tk()
        Window(root)
        root.wm_title("Typing Test")
        root.geometry("500x180")
        root.mainloop()


def typing_test(sentence):
    print('Alright, you will have to type the sentence that shows up as fast as possible:')
    w = Worker()
    w.daemon = True
    w.start()
    start = time.time()
    attempt = input()
    diff = round(time.time() - start, 2)
    if diff > 15:
        penalty = diff-15
    else:
        penalty = 0
    score = Levenshtein.distance(attempt, sentence) + penalty
    print(
        f'Yay, you did it! You lose 1 point for each mistake you make, so your score was {100-score} out of 100! It took you {diff} seconds.')


typing_test(sentence)
