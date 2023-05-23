from pygame import mixer
from tkinter import *

current_song = 0  
songs = ["song1.mp3", "song2.mp3", "song3.mp3"] 
def play():
    global current_song
    mixer.music.load(songs[current_song])
    mixer.music.play()

def pause():
    mixer.music.pause()

def resume():
    mixer.music.unpause()

def next_song():
    global current_song
    current_song = (current_song + 1) % len(songs)  
    play()

root = Tk()
root.geometry("600x300")

mixer.init()

Label(root, text="Welcome to music player", font="lucidia 30 bold").pack()
Button(text="Play", command=play).place(x=200, y=100)
Button(text="Pause", command=pause).place(x=270, y=100)
Button(text="Resume", command=resume).place(x=350, y=100)
Button(text="Next Song", command=next_song).place(x=440, y=100)
Button(text="Quit", command=root.quit).place(x=520, y=100)

root.mainloop()
