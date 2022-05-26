import tkinter as tk


def file_open():
    label['text'] = 'work'


win = tk.Tk()
label_text = 'You file is:'
button_open = tk.Button(text='Open xml-file', width=15, height=1, command=file_open)
button_open.pack()

label = tk.Label(text=label_text, width=30, height=2)
label.pack()

button_convert = tk.Button(text='Convert', width=15, height=1, command=file_open)
button_convert.pack()

win.mainloop()


# print(dir(tk))