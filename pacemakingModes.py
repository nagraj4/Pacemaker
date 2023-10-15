from tkinter import *
import time
window=Tk()

class modes():
    def __init__(self, ATR_PACE_CTRL_D8, VENT_PACE_CTRL_D9, PACINGREF_PWM_D5, 
                 PACE_CHARGE_CTRL_D2, PACE_GND_CTRL_D10, Z_ATR_CTRL_D4, 
                 Z_VENT_CTRL_D7, ATR_GND_CTRL_D11, VENT__GND_CTRL_D12):
        self.ATR_PACE_CTRL_D8 = ATR_PACE_CTRL_D8
        self.VENT_PACE_CTRL_D9 = VENT_PACE_CTRL_D9
        self.PACINGREF_PWM_D5 = PACINGREF_PWM_D5
        self.PACE_CHARGE_CTRL_D2 = PACE_CHARGE_CTRL_D2
        self.PACE_GND_CTRL_D10 = PACE_GND_CTRL_D10
        self.Z_ATR_CTRL_D4 = Z_ATR_CTRL_D4
        self.Z_VENT_CTRL_D7 = Z_VENT_CTRL_D7
        self.ATR_GND_CTRL_D11 = ATR_GND_CTRL_D11
        self.VENT__GND_CTRL_D12 = VENT__GND_CTRL_D12
    def change(mode):
        def del_change():
            done_change.destroy()
            d8label.destroy()
            d9label.destroy()
            d5label.destroy()
            d2label.destroy()
            d10label.destroy()
            d4label.destroy()
            d7label.destroy()
            d11label.destroy()
            d12label.destroy()
            d5pwm.destroy()
            d5pwnsave.destroy()
        def d8swap():
            if(mode.ATR_PACE_CTRL_D8 == 0):
                mode.ATR_PACE_CTRL_D8 = 1
            else:
                mode.ATR_PACE_CTRL_D8 = 0
            d8label.config(text = "ATR_PACE_CTRL_D8:  " + str(mode.ATR_PACE_CTRL_D8))
        def d9swap():
            if(mode.VENT_PACE_CTRL_D9 == 0):
                mode.VENT_PACE_CTRL_D9 = 1
            else:
                mode.VENT_PACE_CTRL_D9 = 0
            d9label.config(text = "VENT_PACE_CTRL_D9:  " + str(mode.VENT_PACE_CTRL_D9))

        def d5swap():
            newval = d5pwm.get()
            mode.PACINGREF_PWM_D5 = float(newval)
            d5label.config(text = "PACINGREF_PWM_D5:  " + str(mode.PACINGREF_PWM_D5))

        def d2swap():
            if(mode.PACE_CHARGE_CTRL_D2 == 0):
                mode.PACE_CHARGE_CTRL_D2 = 1
            else:
                mode.PACE_CHARGE_CTRL_D2 = 0
            d2label.config(text = "PACE_CHARGE_CTRL_D2:  " + str(mode.PACE_CHARGE_CTRL_D2))
        def d10swap():
            if(mode.PACE_GND_CTRL_D10 == 0):
                mode.PACE_GND_CTRL_D10 = 1
            else:
                mode.PACE_GND_CTRL_D10 = 0
            d10label.config(text = "PACE_GND_CTRL_D10:  " + str(mode.PACE_GND_CTRL_D10))
        def d4swap():
            if(mode.Z_ATR_CTRL_D4 == 0):
                mode.Z_ATR_CTRL_D4 = 1
            else:
                mode.Z_ATR_CTRL_D4 = 0
            d4label.config(text = "Z_ATR_CTRL_D4:  " + str(mode.Z_ATR_CTRL_D4))
        def d7swap():
            if(mode.Z_VENT_CTRL_D7 == 0):
                mode.Z_VENT_CTRL_D7 = 1
            else:
                mode.Z_VENT_CTRL_D7 = 0
            d7label.config(text = "Z_VENT_CTRL_D7:  " + str(mode.Z_VENT_CTRL_D7))
        def d11swap():
            if(mode.ATR_GND_CTRL_D11 == 0):
                mode.ATR_GND_CTRL_D11 = 1
            else:
                mode.ATR_GND_CTRL_D11 = 0
            d11label.config(text = "ATR_GND_CTRL_D11:  " + str(mode.ATR_GND_CTRL_D11))
        def d12swap():
            if(mode.VENT__GND_CTRL_D12 == 0):
                mode.VENT__GND_CTRL_D12 = 1
            else:
                mode.VENT__GND_CTRL_D12 = 0
            d12label.config(text = "VENT__GND_CTRL_D12:  " + str(mode.VENT__GND_CTRL_D12))
        done_change = Button(window, text = "Save and Done", command = del_change)
        done_change.place(x=100, y=280)
        d8label = Button(window, text = "ATR_PACE_CTRL_D8:  " + str(mode.ATR_PACE_CTRL_D8), command = d8swap)
        d8label.place(x=100, y=10)
        d9label = Button(window, text = "VENT_PACE_CTRL_D9:  " + str(mode.VENT_PACE_CTRL_D9), command = d9swap)
        d9label.place(x=100, y=40)

        d5label = Label(window, text = "PACINGREF_PWM_D5:  " + str(mode.PACINGREF_PWM_D5))
        d5label.place(x=100, y=70)
        d5pwm = Entry(window)
        d5pwm.place(x=250, y=70)
        d5pwnsave = Button(window, text = "Save PWM", command = d5swap)
        d5pwnsave.place(x=380, y=70)

        d2label = Button(window, text = "PACE_CHARGE_CTRL_D2:  " + str(mode.PACE_CHARGE_CTRL_D2), command = d2swap)
        d2label.place(x=100, y=100)
        d10label = Button(window, text = "PACE_GND_CTRL_D10:  " + str(mode.PACE_GND_CTRL_D10), command = d10swap)
        d10label.place(x=100, y=130)
        d4label = Button(window, text = "Z_ATR_CTRL_D4:  " + str(mode.Z_ATR_CTRL_D4), command = d4swap)
        d4label.place(x=100, y=160)
        d7label = Button(window, text = "Z_VENT_CTRL_D7:  " + str(mode.Z_VENT_CTRL_D7), command = d7swap)
        d7label.place(x=100, y=190)
        d11label = Button(window, text = "ATR_GND_CTRL_D11:  " + str(mode.ATR_GND_CTRL_D11), command = d11swap)
        d11label.place(x=100, y=220)
        d12label = Button(window, text = "VENT__GND_CTRL_D12:  " + str(mode.VENT__GND_CTRL_D12), command = d12swap)
        d12label.place(x=100, y=250)

def aoocall():
    modes.change(aoo)

def voocall():
    modes.change(voo)
    
def aaicall():
    modes.change(aai)

def vvicall():
    modes.change(vvi)

def date():
    def del_date():
        day.destroy()
        month.destroy()
        year.destroy()
        done_date.destroy()
        display_date.destroy()
    month = OptionMenu(window, clicked_month, *months)
    month.place(x=400, y=40)
    day = OptionMenu(window, clicked_day, *days)
    day.place(x=400, y=70)
    year = OptionMenu(window, clicked_year, *years)
    year.place(x=400, y=10)
    display_date = Label(window, text = "Current: " + str(clicked_day.get()) + "/" + str(clicked_month.get()) + "/" + str(clicked_year.get()))
    display_date.place(x=400, y=100)
    done_date = Button(window, text = "Save and Close", command = del_date)
    done_date.place(x=400, y=130)

def time():
    def del_time():
        hour.destroy()
        min.destroy()
        sec.destroy()
        done_time.destroy()
        display_time.destroy()
    hour = OptionMenu(window, clicked_hour, *hours)
    hour.place(x=500, y=10)
    min = OptionMenu(window, clicked_min, *mins)
    min.place(x=500, y=40)
    sec = OptionMenu(window, clicked_sec, *secs)
    sec.place(x=500, y=70)


    if(clicked_min.get() < 10 and clicked_sec.get() < 10):
        display_time = Label(window, text = "Current: " + str(clicked_hour.get()) + ":" + "0" + str(clicked_min.get()) + ":" + "0" + str(clicked_sec.get()))
        display_time.place(x=500, y=100)
    elif(clicked_min.get() < 10):
        display_time = Label(window, text = "Current: " + str(clicked_hour.get()) + ":" + "0" + str(clicked_min.get()) + ":" + str(clicked_sec.get()))
        display_time.place(x=500, y=100)
    elif(clicked_sec.get() < 10):
        display_time = Label(window, text = "Current: " + str(clicked_hour.get()) + ":" + str(clicked_min.get()) + ":" + "0" + str(clicked_sec.get()))
        display_time.place(x=500, y=100)
    else:
        display_time = Label(window, text = "Current: " + str(clicked_hour.get()) + ":" + str(clicked_min.get()) + ":" + str(clicked_sec.get()))
        display_time.place(x=500, y=100)

    done_time = Button(window, text = "Save and Close", command = del_time)
    done_time.place(x=500, y=130)
    
aoo = modes(0, 0, 0.5, 0, 0, 0, 0, 0, 0)
aai = modes(0, 0, 0.5, 0, 0, 0, 0, 0, 0)
vvi = modes(0, 0, 0.5, 0, 0, 0, 0, 0, 0)
voo = modes(0, 0, 0.5, 0, 0, 0, 0, 0, 0)

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", 
          "Aug", "Sep", "Oct", "Nov", "Dec"]
days = []
years = []
hours = []
mins = []
secs = []

for x in range(31):
    days.append(x+1)

for x in range(30):
    years.append(x+2016)

for x in range(24):
    hours.append(x)

for x in range(60):
    mins.append(x)

for x in range(60):
    secs.append(x)

clicked_month = StringVar()
clicked_day = IntVar()
clicked_year = IntVar()
clicked_hour = IntVar()
clicked_min = IntVar()
clicked_sec = IntVar()

clicked_month.set(months[9])
clicked_day.set(days[14])
clicked_year.set(years[7])
clicked_hour.set(hours[8])
clicked_min.set(mins[30])
clicked_sec.set(secs[30])

clock_init = Button(window, text="Change Date", command = date)
clock_init.place(x=530, y=320)

time_init= Button(window, text="Change Time", command = time)
time_init.place(x=530, y=350)

aoo_init = Button(window, text="AOO mode", command = aoocall)
aoo_init.place(x=10, y=10)

voo_init = Button(window, text="VOO mode", command = voocall)
voo_init.place(x=10, y=40)

aai_init = Button(window, text="AAI mode", command = aaicall)
aai_init.place(x=10, y=70)

vvi_init = Button(window, text="VVI mode", command = vvicall)
vvi_init.place(x=10, y=100)

caution = Label(window, text = "Only change pacemaker values if you are sure of the changes that will occur; if problems occur please contact 911", bg = "#FFFFFF") #red = #DF7775
caution.place(x=10, y=380)

window.title('3K04 GUI')
window.geometry("620x400+10+20")
window.configure(bg="lightblue") #sunset orange = #FA5F55
window.mainloop()