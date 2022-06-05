import pickle
from tkinter import *
import numpy as np

with open("titanic.pickle",'rb') as f:
    model=pickle.load(f)
def predict(pclass,age,fare,gender):
    x=np.zeros(5)
    x[0]=pclass
    x[1]=age
    x[2]=fare
    if(gender=="Female"):
        x[3]=1
    else:
        x[4]=1
    print(x[0:])
    prd=model.predict([x])[0]
    if(prd==0):
        label4 = Label(window, text="Not Survived", relief="solid",
                       width=24, font=("arial", 14, "bold"))
        label4.place(x=140, y=300)
    else:
        label4 = Label(window, text="Survived", relief="solid",
                       width=24, font=("arial", 14, "bold"))
        label4.place(x=140, y=300)
    return prd
window = Tk()
window.geometry("610x400")
window.title("Titanic Survival Prediction")

pclass = IntVar(window)
age = IntVar(window)
fare = DoubleVar(window)
gender = StringVar(window)

label_h = Label(window, text="Titanic Survival PREDICTION", relief="solid", width=28, font=("arial", 19, "bold"))
label_h.place(x=90, y=60)



label_a = Label(window, text="Passenger Class", width=30, font=("arial", 10, "bold"))
label_a.place(x=100, y=140)

list1=['1','2','3']
droplist = OptionMenu(window, pclass, *list1)
pclass.set(1)
droplist.config(width=15)
droplist.place(x=305, y=140)

label_a = Label(window, text="Age", width=30, font=("arial", 10, "bold"))
label_a.place(x=100, y=190)
entry_a = Entry(window, textvar=age)
entry_a.place(x=305, y=190)

label_a = Label(window, text="Fare", width=30, font=("arial", 10, "bold"))
label_a.place(x=100, y=220)
entry_a = Entry(window, textvar=fare)
entry_a.place(x=305, y=220)


label_a = Label(window, text="Passenger Class", width=30, font=("arial", 10, "bold"))
label_a.place(x=100, y=260)
list2=['Male','Female']
droplist = OptionMenu(window, gender, *list2)
gender.set("Select Gender")
droplist.config(width=15)
droplist.place(x=305, y=260)

b_p = Button(window, text="Predict", width=50, bg='brown', fg='white',command=lambda :predict(pclass.get(),age.get(),fare.get(),gender.get()))
b_p.place(x=100, y=340)
window.mainloop()



