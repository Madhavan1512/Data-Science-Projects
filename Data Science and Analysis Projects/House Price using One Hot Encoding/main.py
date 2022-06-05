
import pickle
import numpy as np
from tkinter import *
import json
#monroe township=1,0
#robinsville=0,1


def get_estimated_price(town, area):

    x = np.zeros(3)
    if (town=="monroe township"):
        x[0]=1
    elif (town=="robinsville"):
        x[1]=1
    x[2]=area
    price=round(__model.predict([x])[0], 2)
    label4 = Label(window, text=str(price)+"Lakhs", relief="solid",
                   width=24, font=("arial", 14, "bold"))
    label4.place(x=140, y=220)
    return price



window = Tk()
window.geometry("610x400")
window.title("Price Prediction")

town = StringVar(window)
area = DoubleVar(window)

data_columns = {}

with open("columns.json", 'r') as f:
    data_columns = json.load(f)

global __model
with open("price.pickle", 'rb') as f:
    __model = pickle.load(f)

towns=data_columns['towns']

label_h = Label(window, text="HOUSE PRICE PREDICTION USING ONE HOT ENCODING", relief="solid", width=28, font=("arial", 16, "bold"))
label_h.place(x=90, y=40)

label_c = Label(window, text="Town", width=30, font=("arial", 10, "bold"))
label_c.place(x=100, y=130)
droplist = OptionMenu(window, town, *towns)
town.set("Select Location")
droplist.config(width=15)
droplist.place(x=300, y=130)

label_j = Label(window, text="Area", width=30, font=("arial", 10, "bold"))
label_j.place(x=100, y=170)
entry_a = Entry(window, textvar=area)
entry_a.place(x=300, y=170)


b_p = Button(window, text="Estimate Price", width=50, bg='brown', fg='white',command=lambda :get_estimated_price(town.get(),area.get()))
b_p.place(x=100, y=300)
window.mainloop()