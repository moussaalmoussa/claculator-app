#we want to create a calculator application
#import tkinter

from tkinter import *
#create the program
root=Tk()
root.title('calculator')
count=0
num=''
pluscount=0
minuscount=0
timescount=0
devidescount=0
totalnumber=0
secondnumber=0
myLabel=Label(root,text='')
myLabel.grid(row=0,column=0)

#create a plus function
def plus_button():
    global pluscount
    global count
    global num
    global totalnumber
    global secondnumber
    global myLabel
    if pluscount>0:
        print('the first number is: '+str(totalnumber))
        print('the num is: '+str(num))
        for item in num[::-1]:
            print(item)
            if item=='+':
                index=num.find('+')
                print('the index is: '+str(index))
                print('the length is: '+str(len(num)-1))
                for i in range(index+1,len(num)):
                    print('the item is: '+num[i])
                    secondnumber=str(secondnumber)+str(num[i])
                    if num[i]=='=':
                        secondnumber=secondnumber[:-1]
                    print('the second number is: '+secondnumber)
                break
        totalnumber=totalnumber+float(secondnumber)
        totalnumber=round(totalnumber,2)
        print('the total number is: '+str(totalnumber))
        if '=' in num:
            num=num+str(totalnumber)
            print('found')
            myLabel=Label(root,text=num)
            myLabel.grid(row=0,column=0)
            return
    if pluscount==0:   
        totalnumber=float(num)
        print('the first number is: '+str(totalnumber))
    num=num+'+'
    myLabel=Label(root,text=num)
    myLabel.grid(row=0,column=0)
    pluscount=pluscount+1
    
#create a minus function
def minus_button():
    global minuscount
    global count
    global num
    global totalnumber
    global secondnumber
    global myLabel
    if minuscount>0:
        print('the first number is: '+str(totalnumber))
        print('the num is: '+str(num))
        for item in num[::-1]:
            print(item)
            if item=='-':
                index=num.find('-')
                print('the index is: '+str(index))
                print('the length is: '+str(len(num)-1))
                for i in range(index+1,len(num)):
                    print('the item is: '+num[i])
                    secondnumber=str(secondnumber)+str(num[i])
                    if num[i]=='=':
                        secondnumber=secondnumber[:-1]
                    print('the second number is: '+secondnumber)
                break
        totalnumber=totalnumber-float(secondnumber)
        totalnumber=round(totalnumber,2)
        print('the total number is: '+str(totalnumber))
        if '=' in num:
            num=num+str(totalnumber)
            print('found')
            myLabel=Label(root,text=num)
            myLabel.grid(row=0,column=0)
            return
    if minuscount==0:
        totalnumber=float(num)
        print('the first number is: '+str(totalnumber))
    num=num+'-'
    myLabel=Label(root,text=num)
    myLabel.grid(row=0,column=0)
    minuscount=minuscount+1
    
#create a times function
def times_button():
    global timescount
    global count
    global num
    global totalnumber
    global secondnumber
    global myLabel
    if timescount>0:
        print('the first number is: '+str(totalnumber))
        print('the num is: '+str(num))
        for item in num[::-1]:
            print(item)
            if item=='x':
                index=num.find('x')
                print('the index is: '+str(index))
                print('the length is: '+str(len(num)-1))
                for i in range(index+1,len(num)):
                    print('the item is: '+num[i])
                    secondnumber=str(secondnumber)+str(num[i])
                    if num[i]=='=':
                        secondnumber=secondnumber[:-1]
                    print('the second number is: '+secondnumber)
                break
        totalnumber=totalnumber*float(secondnumber)
        totalnumber=round(totalnumber,2)
        print('the total number is: '+str(totalnumber))
        if '=' in num:
            num=num+str(totalnumber)
            print('found')
            myLabel=Label(root,text=num)
            myLabel.grid(row=0,column=0)
            return
    if timescount==0:
        totalnumber=float(num)
        print('the first number is: '+str(totalnumber))
    num=num+'x'
    myLabel=Label(root,text=num)
    myLabel.grid(row=0,column=0)
    timescount=timescount+1
    
#create a devides function
def devides_button():
    global devidescount
    global count
    global num
    global totalnumber
    global secondnumber
    global myLabel
    if devidescount>0:
        print('the first number is: '+str(totalnumber))
        print('the num is: '+str(num))
        for item in num[::-1]:
            print(item)
            if item=='/':
                index=num.find('/')
                print('the index is: '+str(index))
                print('the length is: '+str(len(num)-1))
                for i in range(index+1,len(num)):
                    print('the item is: '+num[i])
                    secondnumber=str(secondnumber)+str(num[i])
                    if num[i]=='=':
                        secondnumber=secondnumber[:-1]
                    print('the second number is: '+secondnumber)
                break
        totalnumber=totalnumber/float(secondnumber)
        totalnumber=round(totalnumber,2)
        print('the total number is: '+str(totalnumber))
        if '=' in num:
            num=num+str(totalnumber)
            print('found')
            myLabel=Label(root,text=num)
            myLabel.grid(row=0,column=0)
            return
    if devidescount==0:
        totalnumber=float(num)
        print('the first number is: '+str(totalnumber))
    num=num+'/'
    myLabel=Label(root,text=num)
    myLabel.grid(row=0,column=0)
    devidescount=devidescount+1
    
#create an equal function
def equal_button():
    global num
    global myLabel
    num=num+'='
    print('the new number is: '+str(num))
    myLabel=Label(root,text=num)
    myLabel.grid(row=0,column=0)
    for item in num[::-1]:
        print('the item is: '+str(item))
        if item=='+' or item=='-' or item=='x' or item=='/':
            if item=='+':
                plus_button()
            if item=='-':
                minus_button()
            if item=='x':
                times_button()
            if item=='/':
                devides_button()

#create a general fuction
def button_click(number):
    print('the number is: '+str(number))
    global count
    global num
    global myLabel
    
    if count==0:
        num=str(number)
        myLabel=Label(root,text=num)
        myLabel.grid(row=0,column=0)
        print('the count is: '+str(count))
        count=count+1
    else:
        print('the count is: '+str(count))
        count=count+1
        num=num+str(number)
        myLabel=Label(root,text=num)
        print('the new number is: '+num)
        myLabel.grid(row=0,column=0)

#creae a reset function
def clear():
    global myLabel
    global num
    num='                                                       '
    myLabel=Label(root,text=num)
    myLabel.grid(row=0,column=0)
        
    
#create buttons
button1=Button(root,text='1',padx=30,pady=30,fg='blue',command=lambda:button_click(1))
button2=Button(root,text='2',padx=30,pady=30,fg='blue',command=lambda:button_click(2))
button3=Button(root,text='3',padx=30,pady=30,fg='blue',command=lambda:button_click(3))
button4=Button(root,text='4',padx=30,pady=30,fg='blue',command=lambda:button_click(4))
button5=Button(root,text='5',padx=30,pady=30,fg='blue',command=lambda:button_click(5))
button6=Button(root,text='6',padx=30,pady=30,fg='blue',command=lambda:button_click(6))
button7=Button(root,text='7',padx=30,pady=30,fg='blue',command=lambda:button_click(7))
button8=Button(root,text='8',padx=30,pady=30,fg='blue',command=lambda:button_click(8))
button9=Button(root,text='9',padx=30,pady=30,fg='blue',command=lambda:button_click(9))
buttonPlus=Button(root,text='+',padx=30,pady=30,fg='blue',command=lambda:plus_button())
buttonMinus=Button(root,text='-',padx=30,pady=30,fg='blue',command=lambda:minus_button())
buttonDevides=Button(root,text='÷',padx=30,pady=30,fg='blue',command=lambda:devides_button())
buttonTimes=Button(root,text='x',padx=30,pady=30,fg='blue',command=lambda:times_button())
buttonEqual=Button(root,text='=',padx=30,pady=30,fg='green',command=lambda:equal_button())
buttonclosebrackets=Button(root,text=')',padx=30,pady=30,fg='blue',command=lambda:button_click(')'))
buttonopenbrackets=Button(root,text='(',padx=30,pady=30,fg='blue',command=lambda:button_click('('))
buttonPourcentage=Button(root,text='%',padx=30,pady=30,fg='blue',command=lambda:button_click('%'))
buttonFloat=Button(root,text='.',padx=30,pady=30,fg='blue',command=lambda:button_click('.'))
button0=Button(root,text='0',padx=30,pady=30,fg='blue',command=lambda:button_click(0))
buttonreset=Button(root,text='C',padx=30,pady=30,fg='red',command=lambda:clear())


#represent the buttons on the screen
button1.grid(row=4,column=0)
button2.grid(row=4,column=1)
button3.grid(row=4,column=2)
button4.grid(row=3,column=0)
button5.grid(row=3,column=1)
button6.grid(row=3,column=2)
button7.grid(row=2,column=0)
button8.grid(row=2,column=1)
button9.grid(row=2,column=2)
buttonPlus.grid(row=4,column=3)
buttonMinus.grid(row=3,column=3)
buttonDevides.grid(row=1,column=3)
buttonTimes.grid(row=2,column=3)
buttonEqual.grid(row=5,column=3)
buttonclosebrackets.grid(row=1,column=1)
buttonopenbrackets.grid(row=1,column=0)
buttonPourcentage.grid(row=1,column=2)
buttonFloat.grid(row=5,column=2)
button0.grid(row=5,column=1)
buttonreset.grid(row=5,column=0)

#loop the main screen
root.mainloop()


