from tkinter import *

#Create new window
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do sth")

#calls action
button = Button(text="Click Me", command=action)
button.pack()

#Entrie
entry = Entry(width=30)
#Add some text to begin with
entry.insert(index=END, string="Some text to begin with.")
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor inside of textbox
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
text.insert(END, " Add next part of text.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#My additional part how to pin the button to spinbox and see result in text box
def spinbox_button():
    #gets the current value in spinbox.
    digit = spinbox.get()
    text.insert(END, digit)
button2 = Button(text="Spinbox_button", command=spinbox_button)
button2.pack()
text.insert(END, "")

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=1, to=100, command=scale_used)
scale.pack()

Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
print(checked_state.get())
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton3 = Radiobutton(text="Option3", value=3, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()

#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()
window.mainloop()