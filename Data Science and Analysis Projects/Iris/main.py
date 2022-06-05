import json
import pickle
from tkinter import *

import numpy as np
with open('columns.json','r') as f:
    target=json.load(f)["data_columns"]
with open("iris.pickle",'rb') as f:
    model=pickle.load(f)


window = Tk()
window.geometry("610x400")
window.title("Iris Flower Prediction")
sl = DoubleVar(window)
sw = DoubleVar(window)
pl = DoubleVar(window)
pw = DoubleVar(window)
label_h = Label(window, text="IRIS FLOWER PREDICTION", relief="solid", width=28, font=("arial", 19, "bold"))
label_h.place(x=90, y=60)
label_a = Label(window, text="Sepal Length(cm)", width=30, font=("arial", 10, "bold"))
label_a.place(x=100, y=140)
entry_a = Entry(window, textvar=sl)
entry_a.place(x=305, y=140)
label_a = Label(window, text="Sepal Width(cm)", width=30, font=("arial", 10, "bold"))
label_a.place(x=100, y=170)
entry_a = Entry(window, textvar=sw)
entry_a.place(x=305, y=170)
label_a = Label(window, text="Petal Length(cm)", width=30, font=("arial", 10, "bold"))
label_a.place(x=100, y=200)
entry_a = Entry(window, textvar=pl)
entry_a.place(x=305, y=200)
label_a = Label(window, text="Sepal Width(cm)", width=30, font=("arial", 10, "bold"))
label_a.place(x=100, y=230)
entry_a = Entry(window, textvar=pw)
entry_a.place(x=305, y=230)
def predict(sl, sw, pl, pw):

    x = np.zeros(4)
    x[0] = sl
    x[1] = sw
    x[2] = pl
    x[3]=pw
    price=target[model.predict([x])[0]]
    label4 = Label(window, text=price, relief="solid",
                   width=24, font=("arial", 14, "bold"))
    label4.place(x=140, y=260)
    return price
b_p = Button(window, text="Estimate Price", width=50, bg='brown', fg='white',command=lambda :predict(sl.get(),sw.get(),pl.get(),pw.get()))
b_p.place(x=100, y=300)

window.mainloop()