from tkinter import *

m = Tk()

frame = Frame(m)
#frame.pack(fill=X)
display = Label(
            master=frame,
            text="Ready?",
            #font=Font(size=28, weight="bold"),
        )
display.pack()

m.mainloop()