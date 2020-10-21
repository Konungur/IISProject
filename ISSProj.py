from tkinter import *
from tkinter import messagebox
from dbSource import Database

db = Database('flights.db')


def populate_list():
    flights_list.delete(0, END)
    for row in db.fetch():
        flights_list.insert(END, row)


def add_item():
    if flight_company_input.get() == '' or flight_number_input.get() == '' or flight_from_input.get() == '' or flight_depDate_input.get() == '' or flight_to_input.get() == '' or flight_arrDate_input.get() == '':
        messagebox.showerror("Required Field Empty", "Fill out all fields")
        return
    db.insert(flight_company_input.get(), flight_number_input.get(), flight_from_input.get(),
              flight_depDate_input.get(), flight_to_input.get(), flight_arrDate_input.get())
    flights_list.delete(0, END)
    flights_list.insert(END, (flight_company_input.get(), flight_number_input.get(), flight_from_input.get(),
                              flight_depDate_input.get(), flight_to_input.get(), flight_arrDate_input.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = flights_list.curselection()[0]
        selected_item = flights_list.get(index)
        flight_company_entry.delete(0, END)
        flight_company_entry.insert(END, selected_item[1])
        flight_number_entry.delete(0, END)
        flight_number_entry.insert(END, selected_item[2])
        flight_from_entry.delete(0, END)
        flight_from_entry.insert(END, selected_item[3])
        flight_depDate_entry.delete(0, END)
        flight_depDate_entry.insert(END, selected_item[4])
        flight_to_entry.delete(0, END)
        flight_to_entry.insert(END, selected_item[5])
        flight_arrDate_entry.delete(0, END)
        flight_arrDate_entry.insert(END, selected_item[6])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], flight_company_input.get(), flight_number_input.get(), flight_from_input.get(), flight_depDate_input.get(), flight_to_input.get(), flight_arrDate_input.get())
    populate_list()


def clear_text():
    flight_company_entry.delete(0, END)
    flight_number_entry.delete(0, END)
    flight_from_entry.delete(0, END)
    flight_depDate_entry.delete(0, END)
    flight_to_entry.delete(0, END)
    flight_arrDate_entry.delete(0, END)


# Window
app = Tk()

#
flight_company_input = StringVar()
flight_company_label = Label(app, text='Company', font=("bold", 14), pady=20)
flight_company_label.grid(row=0, column=0, sticky=W)
flight_company_entry = Entry(app, textvariable=flight_company_input)
flight_company_entry.grid(row=0, column=1)

flight_number_input = StringVar()
flight_number_label = Label(app, text='Flight Number', font=("bold", 14))
flight_number_label.grid(row=1, column=0, sticky=W)
flight_number_entry = Entry(app, textvariable=flight_number_input)
flight_number_entry.grid(row=1, column=1)

flight_from_input = StringVar()
flight_from_label = Label(app, text='Flight From', font=("bold", 14))
flight_from_label.grid(row=2, column=0, sticky=W)
flight_from_entry = Entry(app, textvariable=flight_from_input)
flight_from_entry.grid(row=2, column=1)

flight_depDate_input = StringVar()
flight_depDate_label = Label(app, text='Departure Date', font=("bold", 14))
flight_depDate_label.grid(row=0, column=2, sticky=W)
flight_depDate_entry = Entry(app, textvariable=flight_depDate_input)
flight_depDate_entry.grid(row=0, column=3)

flight_to_input = StringVar()
flight_to_label = Label(app, text='Arrival To', font=("bold", 14), pady=20)
flight_to_label.grid(row=1, column=2, sticky=W)
flight_to_entry = Entry(app, textvariable=flight_to_input)
flight_to_entry.grid(row=1, column=3)

flight_arrDate_input = StringVar()
flight_arrDate_label = Label(app, text='Arrival Date', font=("bold", 14), pady=20)
flight_arrDate_label.grid(row=2, column=2, sticky=W)
flight_arrDate_entry = Entry(app, textvariable=flight_arrDate_input)
flight_arrDate_entry.grid(row=2, column=3)

# Flights List
flights_list = Listbox(app, height=8, width=50, border=0)
flights_list.grid(row=4, column=0, columnspan=3, rowspan=6, pady=20, padx=20)

# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=4, column=3)

# Set scroll to listbox
flights_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=flights_list.yview)

# Bind select
flights_list.bind('<<ListboxSelect>>', select_item)

# Buttons


add_btn = Button(app, text="Add Flight", width=12, command=add_item)  # , command = add_item
add_btn.grid(row=3, column=1, pady=20)

del_btn = Button(app, text="Delete Flight", width=12, command=remove_item)  # , command = add_item
del_btn.grid(row=3, column=2)

upd_btn = Button(app, text="Update Flight", width=12, command=update_item)  # , command = add_item
upd_btn.grid(row=3, column=3)

clr_btn = Button(app, text="Clear Text", width=12, command=clear_text)  # , command = add_item
clr_btn.grid(row=3, column=4)

app.title("Flights Management System")
app.geometry("1280x720")

#
populate_list()

#
populate_list()

# ProgramStart
app.mainloop()
