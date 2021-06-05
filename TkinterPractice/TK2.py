from tkinter import *
import webbrowser
root = Tk()

root.title("Welcome to Vedant's Macbook")
root.geometry('500x500')
a = Label(root, text="Open Google")
a.grid()

def clicked():
    # a.configure(text= "I just got clicked\n" )
    url = 'https://www.google.com/'
    webbrowser.open_new_tab(url)


btn = Button(root, text="Click me" , fg = "red", command=clicked)
btn.grid(column=1, row=0)
root.mainloop()

