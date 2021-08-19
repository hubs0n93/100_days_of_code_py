import tkinter as tk


def calculate():
    value = round(1.609 * float(entry.get()), 1)
    main_label.config(text=f"is equal to {value} Km")

#Window
window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)

#Label empty
empty = tk.Label(text=" ")
empty.grid(column=0, row=0)
empty.config(padx=40, pady=10)
#Text
entry = tk.Entry(width=5)
entry.grid(column=1, row=0)

#Labels
miles = tk.Label(text="Miles")
miles.grid(column=2, row=0)

#Main label
value = 0
main_label = tk.Label(text=f"is equal to {value} Km")
main_label.grid(column=1, row=1)

#Button
button = tk.Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)



window.mainloop()