##################################################
#classification of IRIS flower using Machine Learning
#loading IRIS data to program
from sklearn.datasets import load_iris
iris=load_iris()
##separating input and output
x=iris.data
y=iris.target
##spliting the database for training and testing
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
##################################################

##creating a KNN model##
#k nearest neighbors algorithm
from sklearn.neighbors import KNeighborsClassifier
k=KNeighborsClassifier(n_neighbors=5)
#training the model by training dataset
k.fit(x_train, y_train)
#testing the model by testing data
y_pred=k.predict(x_test)
###3finding accuracy
from sklearn.metrics import accuracy_score
acc_knn=accuracy_score(y_test,y_pred)
acc_knn=round(acc_knn*100,2)


##################################################
######## designing the GUI using TKINTER #########

from tkinter import *
import tkinter.messagebox as m
w=Tk()
w.title("Machine Learning")
w.configure(bg='coral2')
w.geometry('650x400')


s1=IntVar()
s2=IntVar()
s3=IntVar()
s4=IntVar()
v=StringVar()
###dinamic part of the project(fucion)
def submit():
    a=s1.get()
    b=s2.get()
    c=s3.get()
    d=s4.get()
    
def Reset():
    pass
def knn():
    pass




####### designing the component of the GUI #######
l2=Label(w, text="                     ", bg="coral2")
l2.grid(row=0, column=1)
l=Label(w, text="'''        Enter Following File        '''", fg="firebrick4" ,font=("Times New Roman",15,"underline"), bg="coral2")
l.grid(row=1, column=3, columnspan=2)
l1=Label(w, text="            ", bg="coral2")
l1.grid(row=2, column=0)



####left side UI
knn=Button(w, text="KNN", font=("arial", 15, "bold"), height=1,width=6, bg="firebrick4")
knn.grid(row=2, column=1)
l3=Label(w, text="       ", bg="coral2")
l3.grid(row=3, column=1)


lg=Button(w, text="LG", font=("arial", 15, "bold"), height=1,width=6, bg="firebrick4")
lg.grid(row=4, column=1)
l4=Label(w, text="       ", bg="coral2")
l4.grid(row=5, column=1)

dt=Button(w, text="DT", font=("arial", 15, "bold"), height=1,width=6, bg="firebrick4")
dt.grid(row=6, column=1)
l5=Label(w, text="       ", bg="coral2")
l5.grid(row=7, column=1)

nb=Button(w, text="NB", font=("arial", 15, "bold"), height=1,width=6, bg="firebrick4")
nb.grid(row=8, column=1)
l6=Label(w, text="       ", bg="coral2")
l6.grid(row=9, column=1)

compare=Button(w, text="Compare", font=("arial", 15, "bold"), height=1,width=6, bg="firebrick4")
compare.grid(row=10,column=1)
l7=Label(w, text="       ", bg="coral2")
l7.grid(row=11, column=1)


l8=Label(w, text="                                 ", bg="coral2")
l8.grid(row=2, column=2)
result=Label(w, text="result will be shown here", font=("arial", 20, "bold"), textvariable=v ,relief="solid", bg="coral4", width=35)
result.grid(row=12, column=1, columnspan=6)
####right side UI
sl=Label(w, text="SL  ", bg="coral2", font=("arial", 15, "bold"), height=1,width=6, justify="left")
sl.grid(row=2, column=3)
slEntry=Entry(w, font=("arial", 15, "bold"), relief="solid", textvariable=s1)
slEntry.grid(row=2, column=4)

sw=Label(w, text="SW  ", bg="coral2", font=("arial", 15, "bold"), height=1,width=6)
sw.grid(row=4, column=3)
swEntry=Entry(w, font=("arial", 15, "bold"), relief="solid", textvariable=s2)
swEntry.grid(row=4, column=4)

pl=Label(w, text="PL  ", bg="coral2", font=("arial", 15, "bold"), height=1,width=6)
pl.grid(row=6, column=3)
plEntry=Entry(w, font=("arial", 15, "bold"), relief="solid", textvariable=s3)
plEntry.grid(row=6, column=4)

pw=Label(w, text="PW  ", bg="coral2", font=("arial", 15, "bold"), height=1,width=6)
pw.grid(row=8, column=3)
pwEntry=Entry(w, font=("arial", 15, "bold"), relief="solid", textvariable=s4)
pwEntry.grid(row=8, column=4)

submit=Button(w, text="Submit", font=("arial", 15, "bold"), height=1, width=6, bg="firebrick4", command=submit)
submit.grid(row=10, column=3, columnspan=1)
reset=Button(w, text="Reset", font=("arial", 15, "bold"), height=1, width=6, bg="firebrick4", command=Reset)
reset.grid(row=10, column=4, columnspan=1)

w.mainloop()
######################################################
