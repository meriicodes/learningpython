import tkinter as tk
from tkinter import *
import random 
from tkinter import messagebox


root = tk.Tk()
root.title("<3")
root.geometry("500x500")
root.configure(background= '#ffc8dd')


def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 40:
       x = random.randint(0, root.winfo_width() - button_1.winfo_width())
       y = random.randint(0, root.winfo_height() - button_1.winfo_height())
       button_1.place(x=x, y=y)


def accepted():
    messagebox.showinfo(
        '<3', 'AEEEEEH, te amo !!')
    

def denied():
    messagebox.showinfo(
        '', 'Você recusou...')
    messagebox.showinfo(
        ' ', 'Eu não acredito!!')
    messagebox.showinfo(
        ' ', 'Por que recusou??')
    messagebox.showinfo(
        ' ', 'Você me odeia??')
    messagebox.showinfo(
        ' ', 'Nunca imaginei isso')
    messagebox.showinfo(
        ' ', 'Vou te dar mais uma chance!')
    button_1.destroy()


margin = Canvas(root, width=500, bg= '#ffc8dd', height=100,
                bd= 0, highlightthickness=0, relief='ridge')
margin.pack()
text_id = Label(root, bg='#ffc8dd', text= 'Quer namorar comigo?',
                fg= '#590d22', font=('Montserrat', 24, 'bold'))
text_id.pack()
button_1 = tk.Button(root, text='Não', bg='#ffb3c1', command=denied,
                     relief=RIDGE, bd=3, font=('Gothic', 15, 'bold'))
button_1.pack()
root.bind('<Motion>', move_button_1)
button_2 = tk.Button(root, text='Sim', bg='#ffb3c1', relief=RIDGE,
                     bd=3, command=accepted, font= ('Gothic', 15, 'bold'))
button_2.pack()


root.mainloop()