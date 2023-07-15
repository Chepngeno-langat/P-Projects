from tkinter import *

window = Tk()
window.title('My First GUI program')
window.minsize(width=500, height=300)

#label
my_label = Label(text='I am a Label', font=('Arial', 22, 'bold'))
my_label.pack()


#Button
def button_clicked():
    print('I got clicked!')
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text='Click Me', command=button_clicked)
button.pack()

# Entry
input = Entry(width=15)
input.pack()




window.mainloop()