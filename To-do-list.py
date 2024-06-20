from tkinter import *
from tkinter import font
from PIL import Image, ImageTk


if __name__ == "__main__":
    root = Tk()
    root.title("To Do List")
    root.config(bg="mediumseagreen")
    root.geometry("666x444")
    i = 0
    j = 0

    def del_task(btn, del_btn):
        btn.destroy()
        del_btn.destroy()
    def get_data():
        global i, j
        data = entry_var.get()
        check_btn = IntVar()
        btn = Checkbutton(frame2, text=data, bg="bisque", activebackground="bisque", activeforeground="brown", fg="brown", font=("Arial", 15), variable=check_btn, onvalue=1, offvalue=0, height=2, width=10)
        btn.grid(row=i, column=j, padx=10)
        del_btn = Button(frame2, text="X", bg="brown",activebackground="grey", activeforeground="white", fg="white", padx=5, pady=1, command=lambda : del_task(btn,del_btn))
        del_btn.grid(row=i, column=j+1)
        i = i+1
        if(i>5):
            i=0
            j=j+2
        entry_var.set("")

    def keep_focus():
        entry.focus_set()
        root.after(500, keep_focus)

    frame1 = Frame(root, bg="bisque")
    frame1.pack(padx=20, pady=30)

    features = font.Font(family="Helvetica", size=15)

    label_top = Label(frame1, text="To Do List", fg="brown", bg="bisque", font=("Helvetica", 30, "bold"))
    label_top.grid(row=0, column=0, pady=20, padx=20)

    img = Image.open("to-do-list.jpg")
    photo = ImageTk.PhotoImage(img)
    to_do_img = Label(frame1, image=photo)
    to_do_img.grid(row=0, column=1, padx=40, pady=10)

    entry_var = StringVar()
    entry = Entry(frame1, bg="bisque", textvariable=entry_var, borderwidth=0, highlightthickness=0, font=features)
    entry.grid(row=1, column=0, padx=50, pady=0)

    canvas = Canvas(frame1, bg="bisque", width=entry.winfo_reqwidth(), height=entry.winfo_reqheight(),
                    highlightthickness=0)
    canvas.grid(row=2, column=0, padx=30, pady=0)
    underline_y = entry.winfo_reqheight() - 25
    canvas.create_line(0, underline_y, entry.winfo_reqwidth(), underline_y, fill="black")

    add_btn = Button(frame1, text="Add", bg="brown", fg="bisque", activebackground="brown", activeforeground="bisque", font=features, padx=15, pady=5, command=get_data)
    add_btn.grid(row=1, column=1, padx=20, pady=20)

    frame2 = Frame(frame1, bg="bisque", borderwidth=0, highlightthickness=0)
    frame2.grid(row=3, column=0, pady=20)

    keep_focus()
    root.mainloop()

