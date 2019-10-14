from tkinter import *

root=Tk()
root.geometry('255x350')
root.resizable(False,False)
root.title("English-Bulgarian Dictionary")

root.configure(background="light goldenrod yellow")

world=StringVar()

def translate():
    entered = ent.get()
    output.delete(0.0, END)
    try:
        world = wordslist[entered]
    except:
        world = 'SORRY NO INFO \n AVAILABLE!!!!!!!!\n'
    output.insert(0.0, world)

def clear():
    world.set("")
    output.delete(0.0,END)

wordslist={'book': 'книга', 'telephone': 'телефон', 'music': 'музика', 'advice': 'Съвет', 'girlfriend': 'приятелка(гадже)',
           'dictionary': 'речник', 'car': 'кола', 'title':'заглавие'}

lblworld=Label(root, text='Enter A World :', font=('arial 20 bold'),bg='light goldenrod yellow')
lblworld.grid(row=0, column=1, sticky=W)

ent = Entry(root, width=20, font=('arial 18 bold'), textvariable=world, bg='white')
ent.grid(row=1, column=1)

but = Button(root, padx=2, pady=2, text='Translate', command=translate, bg='light goldenrod yellow', font=('none 18 bold'))
but.grid(row=2, column=1)

but2 = Button(root, padx=2, pady=2, text='Clear', command=clear, bg='light goldenrod yellow', font=('none 18 bold'))
but2.grid(row=3, column=1)

output = Text(root, width=18, height=8, font=('Time 20 bold'), fg="black")

output.grid(row=4, column=1)

root.mainloop()