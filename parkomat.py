from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Frame, Label
import datetime
from datetime import timedelta
import random
from threading import Timer
from time import sleep
from collections import OrderedDict

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d %H:%M')
    except ValueError:
        raise ValueError("Incorrect data format, should be Y-m-d H:M")

def closeWindow(window):
    window.destroy()

def windowPayCash(parent, duration):

    def cashNextClick():
        window=windowPayCard(newWindow)
        sleep(0.05)
        if (window==None):
            closeWindow(newWindow)

    def countMoney():
        paidMoney=0
        for key, value in money.money.items():
            paidMoney+=value*key*100
        label3.config(text='Zapłacono: '+str(round(paidMoney/100.0,2))+' zł')
        if (paidMoney/100>=toPay):
            if (toPay==10 and paidMoney/100>10):
                closeWindow(newWindow)
                messagebox.showerror("Brak reszty!", \
                    "Brak monet do wydania w automacie!\nProszę zabrać wpłacone "+str(paidMoney/100)+"zł") 
                return
            if (paidMoney/100==toPay):
                closeWindow(newWindow)
                messagebox.showinfo("Sukces!", "Wyliczona suma, proszę odebrać blankiecik ;)")
                return
            newWindow.withdraw()
            window=windowGetChange(newWindow, paidMoney-toPay*100)
            sleep(0.05)
            if (window==None):
                closeWindow(newWindow)

    
    money=Money()
    paidMoney=0
    toPay=0

    ## Obliczanko ile płacimy
    days = duration.days
    hours = duration.seconds//3600
    minutes = (duration.seconds//60)%60

    #print(str(toPay)+' '+str(days))
    toPay+=(days//28)*7500
    days%=28
    #print(str((days//28)*7500)+' '+str(toPay)+' '+str(days))
    toPay+=(days//7)*1800
    days%=7
    #print(str((days//7)*1800)+' '+str(toPay)+' '+str(days))
    toPay+=250*(days//2)
    days%=2
    #print(str(250*(days//2))+' '+str(toPay)+' '+str(days))
    toPay+=100*days
    if (hours==0):
        toPay+=2
    else:
        toPay+=2+(hours*4)
    label2text='Do zapłaty: '+str(toPay)+' zł'   
    ## Koniec obliczanka  
    
    newWindow = Toplevel(parent)
    newWindow.wm_title("Wrzuć monety lub zapłać kartą")
    newWindow.grab_set()
        
    ## CASH LAYOUT

    frame1 = Frame(newWindow)
    frame1.pack(fill=BOTH)    

    #td.days, td.seconds//3600, (td.seconds//60)%60 
    label1text='Czas postoju: '+str(duration.days)+ ' dni, ' \
        +str(duration.seconds//3600)+ ' godz, ' \
        +str((duration.seconds//60)%60)+' min'
    
    label1 = Label(frame1, text=label1text, width=50)
    label1.pack(side=LEFT, padx=5)
    #label1.config(text='change the value')
        
    frame2 = Frame(newWindow)
    frame2.pack(fill=BOTH)

    label2 = Label(frame2, text=label2text, width=50)
    label2.pack(side=LEFT, padx=5)
        
    frame3 = Frame(newWindow)
    frame3.pack(fill=X)

    label3text='Zapłacono: 0zł'
    label3 = Label(frame3, text=label3text, width=50)
    label3.pack(side=LEFT, padx=5)

    frame4 = Frame(newWindow)
    frame4.pack(fill=BOTH, expand=True)        

    button41 = Button(frame4, text="1g", width=12, bg='goldenrod',\
                      command= lambda: [money.addMoney(0.01), countMoney()])
    button41.pack(side=LEFT, padx=5, pady=5)
    button42 = Button(frame4, text="2g", width=12, bg='goldenrod',\
                      command= lambda: [money.addMoney(0.02), countMoney()])
    button42.pack(side=LEFT, padx=5, pady=5)
    button43 = Button(frame4, text="5g", width=12, bg='goldenrod',\
                      command= lambda: [money.addMoney(0.05), countMoney()])
    button43.pack(side=LEFT, padx=5, pady=5)
        
    frame5 = Frame(newWindow)
    frame5.pack(fill=BOTH, expand=True)

    button51 = Button(frame5, text="10g", width=12, bg='gray85',\
                      command= lambda: [money.addMoney(0.10), countMoney()])
    button51.pack(side=LEFT, padx=5, pady=5)
    button52 = Button(frame5, text="20g", width=12, bg='gray85',\
                      command= lambda: [money.addMoney(0.20), countMoney()])
    button52.pack(side=LEFT, padx=5, pady=5)
    button53 = Button(frame5, text="50g", width=12, bg='gray85',\
                      command= lambda: [money.addMoney(0.50), countMoney()])
    button53.pack(side=LEFT, padx=5, pady=5)

    frame6 = Frame(newWindow)
    frame6.pack(fill=BOTH, expand=True)

    button61 = Button(frame6, text="1zł", width=12, bg='gray95',\
                      command= lambda: [money.addMoney(1), countMoney()])
    button61.pack(side=LEFT, padx=5, pady=5)
    button62 = Button(frame6, text="2zł", width=12, bg='gray95',\
                      command= lambda: [money.addMoney(2), countMoney()])
    button62.pack(side=LEFT, padx=5, pady=5)
    button63 = Button(frame6, text="5zł", width=12, bg='gray95',\
                      command= lambda: [money.addMoney(5), countMoney()])
    button63.pack(side=LEFT, padx=5, pady=5)

    frame7 = Frame(newWindow)
    frame7.pack(fill=BOTH, expand=True)

    button71 = Button(frame7, text="10zł", width=12, bg='light sky blue',\
                      command= lambda: [money.addMoney(10), countMoney()])
    button71.pack(side=LEFT, padx=5, pady=5)
    button72 = Button(frame7, text="20zł", width=12, bg='light sky blue',\
                      command= lambda: [money.addMoney(20), countMoney()])
    button72.pack(side=LEFT, padx=5, pady=5)
    button73 = Button(frame7, text="50zł", width=12, bg='light sky blue',\
                      command= lambda: [money.addMoney(50), countMoney()])
    button73.pack(side=LEFT, padx=5, pady=5)

    frame8 = Frame(newWindow)
    frame8.pack(fill=BOTH, expand=True)

    button81 = Button(frame8, text="100zł", width=12, bg='light sky blue',\
                      command= lambda: [money.addMoney(100), countMoney()])
    button81.pack(side=LEFT, padx=5, pady=5)
    button82 = Button(frame8, text="200zł", width=12, bg='light sky blue',\
                      command= lambda: [money.addMoney(200), countMoney()])
    button82.pack(side=LEFT, padx=5, pady=5)
    button83 = Button(frame8, text="500zł", width=12, bg='light sky blue',\
                      command= lambda: [money.addMoney(500), countMoney()])
    button83.pack(side=LEFT, padx=5, pady=5)

    frame9 = Frame(newWindow)
    frame9.pack(fill=BOTH)    
        
    label9 = Label(frame9, text="Aby przejść dalej, wrzuć monety lub zapłać kartą... ", width=50)
    label9.pack(side=LEFT, padx=5, pady=15)

    frame10 = Frame(newWindow)
    frame10.pack(fill=BOTH)

    button10 = Button(frame10, text="Zapłać kartą", bg='lightyellow', command=cashNextClick)
    button10.pack(fill=BOTH, pady=10, padx=5, expand=True)

def windowPayCard(parent):

    newWindow = Toplevel(parent)
    newWindow.wm_title("Pay by card")
    newWindow.grab_set()
        
    ## CARD LAYOUT

    frame1 = Frame(newWindow)
    frame1.pack(fill=BOTH)
    
    if (random.randint(0, 99)>3):
        label1 = Label(frame1, text="Drukowanie paragonu i blankietu, proszę czekać...", width=50)
    else:
        label1 = Label(frame1, text="Transakcja odrzucona! Powrót do menu...", width=50)
    label1.pack(side=LEFT, padx=20, pady=20)

    timer = Timer(3, closeWindow, [newWindow])
    timer.start()

    return newWindow.wait_window()

def windowGetChange(parent, changeValue):

    newWindow = Toplevel(parent)
    newWindow.wm_title("Zabierz resztę")   
        
    ## GET YOUR CHANGE LAYOUT

    frame1 = Frame(newWindow)
    frame1.pack(fill=BOTH)    
    if (changeValue%100==0):
        label1text='Zabierz swoje '+str(int(changeValue/100))+'zł reszty...'
    else:
        label1text='Zabierz swoje '+str(changeValue/100)+'zł reszty...'
    label1 = Label(frame1, text=label1text, width=50)
    label1.pack(side=LEFT, padx=25, pady=15)

    frame2 = Frame(newWindow)
    frame2.pack(fill=BOTH)    
    
    text2=Text(frame2, width=50, height=16, wrap=WORD)
    text2.pack(side=LEFT, padx=10)

    frame3 = Frame(newWindow)
    frame3.pack(fill=BOTH) 

    button3 = Button(frame3, text="Dziękuję!", bg='lightgreen',\
                     command= lambda: closeWindow(newWindow))
    button3.pack(fill=BOTH, pady=15, padx=5, expand=True)

    ## Obliczanko ile reszty
    change=Money()
    for key, value in change.money.items():
        change.money[key]=changeValue//(key*100)
        changeValue=changeValue%(key*100)
    for key, value in change.money.items():
        #print(str(key))
        if (change.money[key]>0):
            if (float(key)<1):
                text2.insert(0.0,"Nominał "+str(int(key*100))+"gr, ilość: "\
                         +str(int(change.money[key]))+"\n")
            else:
                text2.insert(0.0,"Nominał "+str(int(key))+"zł, ilość: "\
                         +str(int(change.money[key]))+"\n")
    text2.config(state=DISABLED)  
    ## Koniec obliczanka

    return newWindow.wait_window()
       
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        self.initUI()
          
    def initUI(self):

        def button2click():
            text2.delete(0, END)
            text2.insert(0, datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

        def button3click():
            text3.delete(0, END)
            text3.insert(0, datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
            
        def mainNextClick():
            registrationNo=text1.get()
            if (len(registrationNo)==0):
                messagebox.showerror("Błąd!", "Brak numeru rejestracyjnego!")
                return
            elif (len(registrationNo)>9):
                messagebox.showerror("Błąd!", "Numer rejestracyjny dłuższy niż 9 znaków!")
                return

            text1.delete(0, END)
            text1.insert(0,registrationNo.upper())

            startDateString=text2.get()
            endDateString=text3.get()
            try:
                validate(startDateString)
            except ValueError:
                messagebox.showerror("Błąd!", "Zły format daty rozpoczęcia!")
                return
            try:
                validate(endDateString)
            except ValueError:
                messagebox.showerror("Błąd!", "Zły format daty zakończenia!")
                return
            

            
            startDate = datetime.datetime.strptime(startDateString, '%Y-%m-%d %H:%M')
            endDate = datetime.datetime.strptime(endDateString, '%Y-%m-%d %H:%M')

            if((endDate-datetime.datetime.now())/datetime.timedelta(minutes=1)<-5
               or (startDate-datetime.datetime.now())/datetime.timedelta(minutes=1)<-5):
                messagebox.showerror("Błąd!",
                    "Data z przeszłości!")
                return
            
            if ((endDate - startDate) / datetime.timedelta(minutes=1) < 1):
                messagebox.showerror("Błąd!",
                    "Data zakończenia jest wcześniej lub taka sama jak rozpoczęcia!")
                return
            #self.parent.withdraw()
            windowPayCash(self, endDate - startDate)

        ## MAIN LAYOUT

        self.parent.title("Parkomat")
        self.pack(fill=X, expand=True)

        frame1 = Frame(self)
        frame1.pack(fill=BOTH, pady=5)
        
        label1 = Label(frame1, text="Numer rej.", width=15)
        label1.pack(side=LEFT, padx=5)           
       
        text1 = Entry(frame1, width=20)
        text1.pack(side=LEFT, padx=10)
        #text1.insert(END, 'KLI')
        
        frame2 = Frame(self)
        frame2.pack(fill=BOTH)
        
        label2 = Label(frame2, text="Data parkowania", width=15)
        label2.pack(side=LEFT, padx=5, pady=5)           
       
        text2 = Entry(frame2, width=20)
        text2.pack(side=LEFT, padx=10)
        text2.insert(0, datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

        button2 = Button(frame2, text="Akt. data", width=10, command=button2click)
        button2.pack(side=LEFT, padx=5, pady=5) 
        
        frame3 = Frame(self)
        frame3.pack(fill=X)
        
        label3 = Label(frame3, text="Data odjazdu", width=15)
        label3.pack(side=LEFT, padx=5, pady=5)        

        text3 = Entry(frame3, width=20)
        text3.pack(side=LEFT, padx=10)
        date=datetime.datetime.now()+timedelta(hours=1)
        text3.insert(0,date.strftime("%Y-%m-%d %H:%M"))

        button3 = Button(frame3, text="Akt. data", width=10, command=button3click)
        button3.pack(side=LEFT, padx=5, pady=5)

        frame4 = Frame(self)
        frame4.pack(fill=BOTH, expand=True)        

        label4 = Label(frame4, text="Format daty: YYYY-MM-DD HH:MM")
        label4.pack(fill=BOTH, pady=5, padx=70)
        
        frame5 = Frame(self)
        frame5.pack(fill=BOTH, expand=True)        

        button5 = Button(frame5, text="Przejdź do zapłaty", command=mainNextClick, bg='lightyellow')
        button5.pack(fill=BOTH, pady=5, padx=5, expand=True)

class Money():
    def __init__(self):
        self.money=[(500,0),(200,0),(100,0),(50,0),(20,0),\
                    (10,0),(5,0),(2,0),(1,0),(0.50,0),(0.20,0),\
                    (0.10,0),(0.05,0),(0.02,0),(0.01,0)]
        self.money=OrderedDict(self.money) 

    def addMoney(self, coin):
        self.money[coin]+=1      

def main():
  
    root = Tk()
    root.geometry("340x180+300+300")
    root.resizable(width=False, height=False)
    app = Example(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()   
