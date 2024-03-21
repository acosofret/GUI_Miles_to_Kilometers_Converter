from tkinter import *

window = Tk()
window.minsize(width=400, height=200)
window.title("Miles to Kilometers Converter")

# Labels

# #Miles label
# # # When creating an element, first, we hav to create a label:
miles_text = Label(text="Miles")
# # # then, define how this label should show up:
miles_text.grid(column=2, row=0)

# # Km label
km_text = Label(text="Km")
km_text.grid(column=2, row=1)

# # Result label
result_text = Label(text="0")
result_text.grid(column=1, row=1)

# # Equal text label
is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

# input Field
entry = Entry(width=10)
entry.insert(END, string="")
entry.grid(column = 1, row = 0)


# result calculation variable
def calculate():
	result = float(entry.get()) * 1.609344
	result_text.config(text=result)



# Calculate Button
button = Button(text="Calculate", command = calculate)
button.grid(column=1, row=2)


# # window.mainloop() is what keeps the window open. Needs to be at very end
window.mainloop()