import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *
import time


def change_color():
    color = colorchooser.askcolor(title='Choose color')
    text_area.tag_add('textColor', 'sel.first', 'sel.last')
    text_area.tag_config('textColor', foreground=color[1])
    
def change_highlight_color():
    color = colorchooser.askcolor(title='Choose color')
    text_area.tag_add('highlight', 'sel.first', 'sel.last')
    text_area.tag_config('highlight', background=color[1])

def change_bg_color():
    color = colorchooser.askcolor(title='Choose color')
    text_area.config(bg=color[1])

def change_font(*args):
    fontName = font_name.get()
    fontSize = font_size.get()
    try:
        text_area.tag_add('font', 'sel.first', 'sel.last')
        text_area.tag_config('font', font=(fontName, fontSize))
    except Exception:
        text_area.config(font=(fontName, fontSize))

def underline():
    text_area.tag_add('underline', 'sel.first', 'sel.last')
    text_area.tag_config('underline', underline=True)

def bold():
    text_area.tag_add('bold', 'sel.first', 'sel.last')
    text_area.tag_config('bold', font=('bold', 12))


def printBullet(event):
    text_area.insert(INSERT, "\n•\t")


def new_file(event):
    window.title('Untitled')
    text_area.delete(1.0, END)


def open_file(event):
    file = askopenfilename(defaultextension='.txt', file=[('All Files', '*.*'), ('Text Documents', '*.txt')])

    try:
        window.title(os.path.basename(file))
        text_area.delete(1.0, END)

        file = open(file, 'r')

        text_area.insert(1.0, file.read())

    except Exception:
        showerror("Error", "Couldn't read file")

    finally:
        file.close()

def save_file(event):
    file = filedialog.asksaveasfilename(initialfile='untitled.txt',
                                        defaultextension='.txt',
                                        filetypes=[('All Files', '*.*'),
                                                   ('Text Documents', '*.txt')])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, 'w')

            file.write(text_area.get(1.0, END))

        except Exception:
            showerror("Uh Oh!", "Couldn't save file!\nTry again later")

        finally:
            file.close()

def cut(*args):
    text_area.event_generate('<<Cut>>')


def copy(*args):
    text_area.event_generate('<<Copy>>')


def paste(*args):
    text_area.event_generate('<<Paste>>')


def about():
    showinfo('About this editor', 'I made this in like 30 minutes')


def quit():
    window.destroy()


window = Tk()
window.title("Text Editor Program")
file = None
window_width= 1000
window_height = 700
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2.2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

font_name = StringVar(window)
font_name.set('Arial')

font_size = StringVar(window)
font_size.set('12')

text_area = Text(window, font=(font_name.get(), font_size.get()))
text_area.bind("<Control-8>", printBullet)

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)

frame = Frame(window)
frame.grid()

color_button = Button(frame, text='Color', command=change_color)
color_button.grid(row=0, column=0)

highlight_button = Button(frame, text='Highlight', command=change_highlight_color)
highlight_button.grid(row=0, column=1)

underline_button = Button(frame, text='Underline', command=underline)
underline_button.grid(row=0, column=2)

bold_button = Button(frame, text='Bold', command=bold)
bold_button.grid(row=0, column=3)

bg_color_button = Button(frame, text='Background Color', command=change_bg_color)
bg_color_button.grid(row=0, column=4)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=5)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=6)

scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)

file_menu.add_command(label='New', command=new_file)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Cut', command=cut)
edit_menu.add_command(label='Copy', command=copy)
edit_menu.add_command(label='Paste', command=paste)

# Copy/Paste/Cut shortcuts
window.bind("<Control-c>", copy)
window.bind("<Control-x>", cut)
window.bind("<Control-v>", paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About', command=about)

# Ctrl-S saving files
window.bind("<Control-s>", save_file)
window.bind("<Control-o>", open_file)
window.bind("<Control-n>", new_file)


window.mainloop()
