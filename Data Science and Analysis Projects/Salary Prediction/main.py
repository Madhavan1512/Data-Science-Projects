import pickle
import numpy as np
from tkinter import *
import json
#google =2 ,abc pharma = 0, facebook= 1
#sales executive=2,computer programmer = 0, business manager = 1
#degree bachelor=0

def get_estimated_price(company, job, degree):

    x = np.zeros(3)
    if (company=="google"):
        x[0]=2
    elif (company=="abc pharma"):
        x[0]=1
    if (job=="sales executive"):
        x[1]=2
    elif (job=="business manager"):
        x[1]=1
    if (degree=="masters"):
        x[2]=1
    price=round(__model.predict([x])[0], 2)
    if(price==1):
        t="More than 100k"
    else:
        t="Less than 100k"
    label4 = Label(window, text=t, relief="solid",
                   width=24, font=("arial", 14, "bold"))
    label4.place(x=140, y=260)
    return price



window = Tk()
window.geometry("610x400")
window.title("Price Prediction")

fn = DoubleVar(window)
com = StringVar(window)
job = StringVar(window)
deg = StringVar(window)
data_columns = {}

with open("./Data/columns.json", 'r') as f:
    data_columns = json.load(f)

global __model
with open("./Data/salary_prediction.pickle", 'rb') as f:
    __model = pickle.load(f)

company=data_columns['company']
degree=data_columns['degree']
jobs=data_columns['job']

label_h = Label(window, text="SALARY PREDICTION", relief="solid", width=28, font=("arial", 19, "bold"))
label_h.place(x=90, y=20)

label_c = Label(window, text="Company", width=30, font=("arial", 10, "bold"))
label_c.place(x=100, y=100)
droplist = OptionMenu(window, com, *company)
com.set("Select Location")
droplist.config(width=15)
droplist.place(x=300, y=100)

label_j = Label(window, text="Job", width=30, font=("arial", 10, "bold"))
label_j.place(x=100, y=140)
droplist = OptionMenu(window, job, *jobs)
job.set("Select Job")
droplist.config(width=15)
droplist.place(x=300, y=140)

label_d = Label(window, text="Degree", width=30, font=("arial", 10, "bold"))
label_d.place(x=100, y=180)
droplist = OptionMenu(window, deg, *degree)
deg.set("Select Degree")
droplist.config(width=15)
droplist.place(x=300, y=180)

b_p = Button(window, text="Estimate Price", width=50, bg='brown', fg='white',command=lambda :get_estimated_price(com.get(),job.get(),deg.get()))
b_p.place(x=100, y=300)
window.mainloop()