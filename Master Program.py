#Master program
import matplotlib.pyplot as plt
import numpy as np
choice=input("Hey there!! What would you like to create:-\nBar Graph, Horizontal Bar Graph, Pie Chart or a Line Graph:-\n")
if choice=='Bar Graph':
    xarray=[]
    yarray=[]
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        print("What would like to put in x-axis:- ")
        arrayx = input()
        print("What would like to put in y-axis:- ")
        arrayy = input()
        xarray.append(arrayx)
        yarray.append(arrayy)
    x=np.array(xarray)
    y=np.array(yarray)
    lolipop=input("What type of colour would you like in your bars like\n(#4CAF50(green),#FFB90F(gold) or #00EEEE(cyan)):- ")
    sus=float(input("What would you like the width to be:- "))
    labelx=input("Enter the label for x-axis:- ")
    labely=input("Enter the label for y-axis:- ")
    plt.xlabel(labelx)
    plt.ylabel(labely)
    plt.bar(y, [int(a) for a in x], color=lolipop, width=sus)
    plt.show()
elif choice=='Horizontal Bar Graph':
    xarray=[]
    yarray=[]
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        print("What would like to put in x-axis:- ")
        arrayx = input()
        print("What would like to put in y-axis:- ")
        arrayy = input()
        xarray.append(arrayx)
        yarray.append(arrayy)
    x=np.array(xarray)
    y=np.array(yarray)
    lolipop=input("What type of colour would you like in your bars like\n(#4CAF50(green),#FFB90F(gold) or #00EEEE(cyan)):- ")
    sus=float(input("What would you like the height to be:- "))
    labelx=input("Enter the label for x-axis:- ")
    labely=input("Enter the label for y-axis:- ")
    plt.xlabel(labely)
    plt.ylabel(labelx)
    plt.barh(x,[int(b) for b in y], color=lolipop, height=sus)
    plt.show()
elif choice=='Pie Chart':
    ypie=[]
    lolipop=[]
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
        print("What would like to put in the pie chart:- ")
        arrayy = input()
        print("What labels would you like to add:- ")
        lolipoplist = input()
        ypie.append(arrayy)
        lolipop.append(lolipoplist)
    y=np.array(ypie)
    titlepie=input("What is the title of the pie:- ")
    plt.title(titlepie)
    plt.pie(y, labels=lolipop, shadow=True)
    plt.legend()
    plt.show()
else:
    choiceline=input("Would you like to have a single line or a double line graph:-")
    if choiceline=='Single':
        xarray=[]
        yarray=[]
        n = int(input("Enter number of elements : "))
        for i in range(0, n):
            print("What would like to put in x-axis:- ")
            arrayx = input()
            print("What would like to put in y-axis:- ")
            arrayy = input()
            xarray.append(arrayx)
            yarray.append(arrayy)
        x=np.array(xarray)
        y=np.array(yarray)
        mylinewidth=float(input("Enter the line width:- "))
        mycolor=input("Enter the color:- ")
        mylinestyle=input("Enter the line style:- ")
        labelx=input("Enter the label for x-axis:- ")
        labely=input("Enter the label for y-axis:- ")
        plt.xlabel(labelx)
        plt.ylabel(labely)
        plt.plot([int(c) for c in x], [int(d) for d in y], linewidth=mylinewidth, color=mycolor, linestyle=mylinestyle)
        plt.show()
    else:
        xarray=[]
        yarray=[]
        xarray1=[]
        yarray1=[]
        n = int(input("Enter number of elements : "))
        for i in range(0, n):
            print("What would like to put in x-axis of first line:- ")
            arrayx = input()
            print("What would like to put in y-axis of first line:- ")
            arrayy = input()
            xarray.append(arrayx)
            yarray.append(arrayy)
            print("What would like to put in x-axis of second line:- ")
            arrayx1 = input()
            print("What would like to put in y-axis of second line:- ")
            arrayy1 = input()
            xarray.append(arrayx)
            yarray.append(arrayy)
            xarray1.append(arrayx1)
            yarray1.append(arrayy1)
        x=np.array(xarray)
        y=np.array(yarray)
        x1=np.array(xarray1)
        y1=np.array(yarray1)
        mylinewidth=float(input("Enter the line width of first line:- "))
        mycolor=input("Enter the color of first line:- ")
        mylinestyle=input("Enter the line style of first line:- ")
        mylinewidth1=float(input("Enter the line width of second line:- "))
        mycolor1=input("Enter the color of second line:- ")
        mylinestyle1=input("Enter the line style of second line:- ")
        labelx=input("Enter the label for x-axis:- ")
        labely=input("Enter the label for y-axis:- ")
        plt.xlabel(labelx)
        plt.ylabel(labely)
        plt.plot([int(e) for e in x], [int(f) for f in y], linewidth=mylinewidth, color=mycolor, linestyle=mylinestyle)
        plt.plot([int(g) for g in x1],[int(h) for h in y1], linewidth=mylinewidth1, color=mycolor1, linestyle=mylinestyle1)
        plt.show()
