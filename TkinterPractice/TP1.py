import tkinter as tk

m = tk.Tk()
m.title("TkinterPractice")
m.geometry('500x500')
a = tk.Label(m, text="Press the button to end the program.")
a.pack()
button = tk.Button(m, text='Stop', width=50, command=m.destroy)
button.pack()
m.mainloop()
