import tkinter

# function for button
def on_click():
    mile = float(entry.get())
    km = round(mile * 1.60934, 2)
    label2.config(text=f"{km}")


window = tkinter.Tk()
window.title("Mile To KM Convertor")
window.config(padx=20, pady=20)

# Label is equal to
label1 = tkinter.Label(text="is equal to")
label1.config(font=("Merryweather", 16))
label1.grid(column=0, row=1)

# user input
entry = tkinter.Entry(width=7)
entry.insert(index=0, string="0")
entry.grid(column=1, row=0)

# answer
label2 = tkinter.Label(text="0")
label2.config(font=("Merryweather", 12))
label2.grid(column=1, row=1)

# Label miles
label3 = tkinter.Label(text="Miles")
label3.config(font=("Merryweather", 12))
label3.grid(column=2, row=0)

# Label km
label4 = tkinter.Label(text="KM")
label4.config(font=("Merryweather", 12))
label4.grid(column=2, row=1)

# Calculate Button
button = tkinter.Button(text="Calculate", command=on_click)
button.grid(column=1, row=2)

window.mainloop()
