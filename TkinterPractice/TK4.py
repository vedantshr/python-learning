from tkinter import *
# from tkinter.tkk import *
import tkinter.font as tkFont
import webbrowser


def clicked():
    webbrowser.open(url1)
def clicked1():
    webbrowser.open(url2)   
def clicked2():
    webbrowser.open(url3)

root = Tk()
root.title("Test_Window")
root.geometry('2500x1500')
fontstyle = tkFont.Font(family="Lucida Grande", size=30)
a = Label(root, text = "Google", font=fontstyle)
b = Label(root, text = "Whatsapp", font=fontstyle)
c = Label(root, text= "Sociotalks", font=fontstyle)
a.grid(column=0, row=0)
b.grid(column=0, row=1)
c.grid(column=0, row=2)
btn1 = Button(root, text = "Click me", fg = "blue", command = clicked, font=fontstyle)
btn2 = Button(root, text = "Click me", fg = "blue", command = clicked1, font=fontstyle)
btn3 = Button(root, text = "Click me", fg = "blue", command = clicked2, font=fontstyle)
btn1.grid(column=1, row=0)
btn2.grid(column=1, row=1)
btn3.grid(column=1, row=2)
url1 = 'https://www.google.com/'

url2 = 'https://web.whatsapp.com/'

url3 = 'https://sociotalks.blog/'

root.mainloop()