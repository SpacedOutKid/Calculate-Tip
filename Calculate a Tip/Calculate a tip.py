#Calculates a servers tip
from tkinter import *

#This is a function that relates to the calcBtn to calculate the tip and the total bill
def calculateTip():
    DecimalPercent=(eval(entTip.get()))/100
    ExtendedTip=(eval(entBill.get()))*DecimalPercent
    Tip=(f'${ExtendedTip:,.2f}')
    totalbill=(eval(entBill.get()))+ExtendedTip
    total=(f'${totalbill:,.2f}')
    results.set(Tip)
    totalCost.set(total)
  

#This creates the window and the title for the window and the title on the window
window=Tk()
window.title('Tip Calculator')

#This is the bill entry box and label
lblBill=Label(window, text='Enter the total cost of the bill:')
lblBill.grid(row=0,column=0,padx=20,pady=10,sticky=E)
entBill=Entry(window, fg='black')
entBill.configure(width=21)
entBill.grid(row=0,column=1,pady=10,sticky=W,padx=15)
dolSign=Label(window,text='$')
dolSign.grid(row=0,column=1,padx=5,sticky=W)

#This is the tip percentage entry box and label
lblTip=Label(window, text='Enter the tip percentage:')
lblTip.grid(row=1,column=0,padx=10,pady=10,sticky=E)
entTip=Entry(window, fg='black')
entTip.grid(row=1, column=1,padx=15,pady=10,sticky=W)
entTip.configure(width=21)
percentSign=Label(window,text='%')
percentSign.grid(row=1,column=1,padx=1,sticky=W,pady=10)

#This is the button that calculates everything
calcBtn=Button(window,text='Calculate',font=('Agency FB',16),command=calculateTip)
calcBtn.grid(row=2,column=0,columnspan=2,padx=100,pady=20,sticky=SW)
calcBtn.configure(width=20)

#This is a label and entry that displays the results 
results=StringVar()
resultslbl=Label(window,text='The Tip To Pay Is:',font=('Agency FB',16))
resultslbl.grid(row=3,column=0,columnspan=2,padx=117,pady=20,sticky=NW)
resultsEnt=Entry(window,state='readonly',textvariable=results,fg='green')
resultsEnt.grid(row=3,column=0,columnspan=2,padx=110,pady=55,sticky=SW)
resultsEnt.configure(width=20)

#This is a label and entry box that displays the total bill 
totalCost=StringVar()
totalBill=Label(window,text='The Total Bill Is:',font=('Agency FB',16))
totalBill.grid(row=4,column=0,columnspan=2,padx=117,pady=10,sticky=NW)
totalBillEnt=Entry(window,state='readonly',textvariable=totalCost,fg='black')
totalBillEnt.grid(row=4,column=0,columnspan=2,padx=105,pady=40,sticky=SW)
totalBillEnt.configure(width=20)

window.mainloop()
