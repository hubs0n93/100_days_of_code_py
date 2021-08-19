import tkinter


#Button def
def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())

#Window
window = tkinter.Tk()
window.title("My First GUI")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label["text"] = "New Text"
my_label.config(padx=50, pady=50)

#Button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)
new_button = tkinter.Button(text="New Button", command=button_clicked)
new_button.grid(column=2, row=0)
# Entry
input = tkinter.Entry(width=10)
input.grid(column=3, row=3)



window.mainloop()