import tkinter as tk
import psycopg2
import datetime as dt
import time




def get_inputs():

    item_name = input_item.get()

    quantity = input_qty.get()
    unit = input_unit.get()
    model_name = input_model.get()
    encoded_by = input_encodedBy.get()


    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        dbname="MBPI",
        user="postgres",
        password="mbpi-admin")
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO tbl_maintenance(t_itemname, t_quantity, t_unit) VALUES({}, 20, 'ml')
    """.format(item_name))

    # commit the changes
    conn.commit()
    print("Table Created successfully")



# create main window
window = tk.Tk()
window.geometry("600x400")

input_item = tk.Entry(window)
input_item.grid(row=0, column=1)
tl_item = tk.Label(window, text="Item Name")
tl_item.grid(row=0)

input_qty = tk.Entry(window)
input_qty.grid(row=1, column=1)
tl_qty = tk.Label(window, text="Quantity")
tl_qty.grid(row=1)

input_unit = tk.Entry(window)
input_unit.grid(row=2, column=1)
tl_unit = tk.Label(window, text="Unit")
tl_unit.grid(row=2)

input_model = tk.Entry(window)
input_model.grid(row=3, column=1)
tl_model = tk.Label(window, text="Model Name")
tl_model.grid(row=3)

input_encodedBy = tk.Entry(window)
input_encodedBy.grid(row=4, column=1)
tl_encodedBy = tk.Label(window, text="Encoded By")
tl_encodedBy.grid(row=4)

btn1 = tk.Button(window, text='Submit', command=lambda : get_inputs())
btn1.grid(row=5)


window.mainloop()
