from tkinter import *
import pygame
from tkinter import filedialog
root=Tk()
root.geometry('500x400')
pygame.mixer.init()


song_box=Listbox(root,width=100, bg='black',fg='white')
song_box.pack(padx=40,pady=30)

row=Frame(root)
row.pack()


def play():
    song=song_box.get(ACTIVE)
    song=f'C:/Users/Ashutosh Bansal/Desktop/Projects/mp3 player/songs/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

def add_song():
    song=filedialog.askopenfilename(initialdir='songs/',title='choose a song',filetypes=(("Mp3 Files", "*.mp3"),))
    song=song.replace("C:/Users/Ashutosh Bansal/Desktop/Projects/mp3 player/songs/","")
    song=song.replace(".mp3","")
    song_box.insert(END,song)
def add_songs():
    songs=filedialog.askopenfilenames(initialdir='songs/',title='choose a song',filetypes=(("Mp3 Files", "*.mp3"),))

    for song in songs:
        song=song.replace("C:/Users/Ashutosh Bansal/Desktop/Projects/mp3 player/songs/","")
        song=song.replace(".mp3","")
        song_box.insert(END,song)


global paused
paused=False

def pause(is_paused):
    global paused
    is_paused=paused

    if not paused:

        pygame.mixer.music.pause()
        paused=True
    else:
        pygame.mixer.music.unpause()
        paused=False

def next_song():
    next_song=song_box.curselection()
    next_song=next_song[0]+1

    song=song_box.get(next_song)
    try:
        song = f'C:/Users/Ashutosh Bansal/Desktop/Projects/mp3 player/songs/{song}.mp3'
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
    except:
        pass

    song_box.select_clear(0,END)
    song_box.activate(next_song)
    song_box.selection_set(next_song,last=None)

def prev_song():
    next_song=song_box.curselection()
    next_song=next_song[0]-1

    song=song_box.get(next_song)
    try:
        song = f'C:/Users/Ashutosh Bansal/Desktop/Projects/mp3 player/songs/{song}.mp3'
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
    except:
        pass
    song_box.select_clear(0,END)
    song_box.activate(next_song)
    song_box.selection_set(next_song,last=None)


button_prev=Button(row,text='prev',width=7,command=prev_song)
button_next=Button(row,text='next',width=7,command=next_song)
button_play=Button(row,text='play',width=7,command=play)
button_pause=Button(row,text='pause',width=7,command=lambda :pause(paused))
button_stop=Button(row,text='stop',width=7,command=stop)

button_prev.grid(row=0,column=0,padx=10)
button_next.grid(row=0,column=1,padx=10)
button_play.grid(row=0,column=2,padx=10)
button_pause.grid(row=0,column=3,padx=10)
button_stop.grid(row=0,column=4,padx=10)


menu=Menu(root)
root.config(menu=menu)

addsong_menu=Menu(menu)
menu.add_cascade(label='Add songs',menu=addsong_menu)
addsong_menu.add_command(label='Add one song to playlist',command=add_song)
addsong_menu.add_command(label='Add multiple song to playlist',command=add_songs)

root.mainloop()
