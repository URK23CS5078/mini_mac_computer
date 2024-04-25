from tkinter import*  from tkinter import ttk  from tkinter import ttk, messagebox import tkinter as tk  from tkinter import filedialog import platform  import psutil #brightness 
import screen_brightness_control as pct 
#audio 
from ctypes import cast, POINTER  from comtypes import CLSCTX_ALL 
from pycaw.pycaw import AudioUtilities , IAudioEndpointVolume 
#weather 
from geopy.geocoders import Nominatim  from timezonefinder import TimezoneFinder  from datetime import datetime import requests  import pytz #clock 
from time import strftime 
#calendar from tkcalendar import * #open google  import pyautogui import subprocess  import webbrowser as wb  import random root=Tk() root.title('mac-soft Tool') root.geometry("850x500+300+170") root.resizable(False,False) root.configure (bg='#292e2e') 
#icon 
image_icon=PhotoImage (file="C:/Users/dhana/OneDrive/Desktop/Image/Image/icon.png") root.iconphoto (False, image_icon) 
Body=Frame (root,width=900, height=600,bg="#d6d6d6") 
Body.pack(pady=20, padx=20) 
 
#--------- 
LHS=Frame 
(Body,width=310,height=435,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickne ss=1) 
LHS.place (x=10,y=10) 
#logo 
photo=PhotoImage (file="C:/Users/dhana/OneDrive/Desktop/Image/Image/laptop.png")  myimage=Label(LHS,image=photo,background="#f4f5f5") myimage.place(x=2,y=20) my_system= platform.uname() 
l1=Label (LHS, text=my_system.node,bg="#f4f5f5", font=("Acumin Variable Concept", 13, 
'bold'),justify="center") l1.place (x=20,y=200) 
l2=Label (LHS, text=f"Version:{my_system.version}",bg="#f4f5f5", font=("Acumin 
Variable Concept" ,8), justify="center") l2.place (x=20,y=230) 
l3=Label (LHS, text=f"System:{my_system.system}",bg="#f4f5f5", font=("Acumin Variable 
Concept", 10), justify="center") l3.place (x=20,y=253) 
l4=Label (LHS, text=f"Machine: {my_system.machine}",bg="#f4f5f5", font=("Acumin 
Variable Concept", 12), justify="center") l4.place (x=20,y=280) 
l5=Label (LHS, text=f"Total RAM installed: {round(psutil.virtual_memory (). total/1000000000, 2)} GB",bg="#f4f5f5", font=("Acumin Variable Concept", 10), justify="center") l5.place (x=20,y=310) 
l6=Label (LHS, text=f"Processor: {my_system.processor}",bg="#f4f5f5", font=("times new roman", 5,"bold"), justify="center") l6.place (x=20,y=340) 
 
#--------- 
RHS=Frame 
(Body,width=470,height=230,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickne ss=1) 
RHS.place (x=330,y=10) 
system=Label (RHS, text='System', font=("Acumin Variable Concept", 15), bg="#f4f5f5")  system.place (x=10,y=10) 
 
###############battery############## 
 
def convertTime(seconds): 
    minutes,seconds=divmod(seconds,60)     hours,minutes=divmod(minutes,60) 
    return "%d:%02d:%02d"%(hours,minutes,seconds) 
 
def none(): 
    global battery_pg     global battery 
     
    battery=psutil.sensors_battery()     percent=battery.percent     time=convertTime(battery.secsleft) 
 
    lb1.config(text=f"{percent}%") 
    lb1_plug.config(text=f'Plug in:{str(battery.power_plugged)}') 
    Ib1_time.config(text=f'{time}remaining') 
 
    battery_label=Label(RHS,background='#f4f5f5')     battery_label.place (x=15,y=50)     lb1.after (1000, none) 
     
    if battery.power_plugged==True: 
        battery_pg=PhotoImage 
(file="C:/Users/dhana/OneDrive/Desktop/Image/Image/charging.png")         battery_label.config(image=battery_pg) 
     else: 
        
battery_pg=PhotoImage(file="C:/Users/dhana/OneDrive/Desktop/Image/Image/battery.png")         battery_label.config(image=battery_pg) 
 
lb1=Label (RHS, font=("Acumin Variable Concept", 20, 'bold'),bg= '#f4f5f5') lb1.place(x=200,y=40) 
 
lb1_plug=Label (RHS, font=("Acumin Variable Concept", 10),bg='#f4f5f5') lb1_plug.place(x=20,y=100) 
 
Ib1_time=Label (RHS, font=("Acumin Variable Concept", 15),bg='#f4f5f5') Ib1_time.place(x=200,y=100) none() 
######################################################## 
################speaker################ 
lb1_speaker=Label(RHS,text="Speaker:",font=('arial',10,'bold'),bg="#f4f5f5") lb1_speaker.place(x=10,y=150)  volume_value=tk.DoubleVar() 
def get_current_volume_value(): 
    return '{: .2f}'.format(volume_value.get ()) 
 
def volume_changed(event): 
    device =AudioUtilities.GetSpeakers() 
    interface = device.Activate(IAudioEndpointVolume._iid_,CLSCTX_ALL,None)     volume = cast(interface,POINTER(IAudioEndpointVolume))     volume. SetMasterVolumeLevel(-float (get_current_volume_value ()), None) volume=ttk.Scale (RHS, from_=60,to=0,orient='horizontal',                   command=volume_changed, variable=volume_value) volume.place(x=90,y=150) volume.set(20) 
 
######################################################## 
###############Brightness######################### 
 
lb1_brightness=Label(RHS,text='Brightness',font=('arial', 10, 'bold'),bg="#f4f5f5") lb1_brightness.place (x=10,y=190) 
 
current_value=tk.DoubleVar () def get_current_value(): 
    return '{: .2f}'.format (current_value.get ()) def brightness_changed(event): 
    pct.set_brightness (get_current_value()) 
 
brightness= ttk.Scale(RHS, from_=0, to=100, orient='horizontal', 
 
                                     command=brightness_changed, variable=current_value) brightness.place (x=90,y=190) 
######################################################## 
def weather(): 
    app1=Toplevel() 
    app1.geometry('850x500+300+170')     app1.title('Weather')     app1.configure(bg='#f4f5f5')     app1.resizable(False,False) 
 #icon 
    
image_icon=PhotoImage(file='C:/Users/dhana/OneDrive/Desktop/Image/Image/App1.png')     app1.iconphoto(False,image_icon) 
 
    def getWeather():         try: 
            city=textfield.get() 
 
            geolocator=Nominatim(user_agent="geoapiExercises")             location=geolocator.geocose(city)             obj=TimezoneFinder() 
            result=obj.ttimezone_at(lng=location.longitude,lat=location.latitude) 
 
            home=pytz.timezone(result)             local_time=datetime.now(home) 
            current_time=location_time.strftime("%I:%M %p")             clock.config(text=current_time)             name.config(text='CURRENT WEATHER')         except Exception as e: 
            messagebox.showerror("Weather App","Invalid Enry!") 
 
    #search box Search_image=PhotoImage(file="C:/Users/dhana/OneDrive/Desktop/Image/Image/search.pn g") 
    myimage=Label(app1,image=Search_image,bg='#f4f5f5')     myimage.place(x=20,y=20) 
 
    
textfield=tk.Entry(app1,justify='center',width=17,font=('poppins',25,'bold'),bg='#404040',bord er=0,fg='white')     textfield.place(x=50,y=40)     textfield.focus() 
 
    
Search_icon=PhotoImage(file="C:/Users/dhana/OneDrive/Desktop/Image/Image/search_icon .png") 
    
myimage_icon=Button(app1,image=Search_icon,borderwidth=0,cursor='hand2',bg='#404040'
,command=getWeather)     myimage_icon.place(x=400,y=34) 
 
    #logo 
    
Logo_image=PhotoImage(file="C:/Users/dhana/OneDrive/Desktop/Image/Image/logo.png")     logo=Label(app1,image=Logo_image,bg='#f4f5f5')     logo.place(x=150,y=100) 
 
    #botton box 
    
Frame_image=PhotoImage(file="C:/Users/dhana/OneDrive/Desktop/Image/Image/box.png")     frame_myimage=Label(app1,image=Frame_image,bg='#f4f5f5')     frame_myimage.pack(padx=5,pady=5,side=BOTTOM) 
 
    #time 
    name=Label(app1,font=('arial',15,'bold'),bg='#f4f5f5') 
name.place(x=30,y=100) 
    clock=Label(app1,font=('Helvetica',20),bg='#f4f5f5')     clock.place(x=30,y=130) 
 
    #label 
    label1=Label(app1, text="WIND", font=("Helvatica", 12, 'bold'), fg="white",bg="#1ab5ef")     label1.place(x=120,y=400) 
     
    label2=Label(app1, text="HUMIDITY", font=("Helvatica", 12, 'bold'),fg="white", bg="#1ab5ef")     label2.place(x=250,y=400) 
     
    label3=Label(app1, text="DESCRIPTION", font=("Helvatica", 12, 
'bold'),fg="white",bg="#1ab5ef")     label3.place(x=430,y=400) 
     
    label4=Label(app1, text="PRESSURE", font=("Helvatica", 12, 
'bold'),fg="white",bg="#1ab5ef")     label4.place(x=650,y=400) 
 
    t=Label(app1,font=('arial',70,'bold'),fg="#ee666d",bg= '#f4f5f5')     t.place(x=400,y=148) 
    c=Label(app1, font=('arial',70, 'bold'),bg= '#f4f5f5')     c.place(x=400,y=250) 
 
    w=Label(app1,text="...",font=('arial',20, 'bold'),bg="#1ab5ef")     w.place(x=120,y=430) 
 
    h=Label(app1,text=" ...",font=('arial', 20, 'bold'),bg="#1ab5ef")     h.place(x=280,y=430) 
 
d=Label(app1, text=" ...",font=('arial' ,20, 'bold'),bg="#1ab5ef") 
    d.place(x=450,y=430) 
 
    p=Label(app1, text="...", font=('arial',20, 'bold'),bg="#1ab5ef")     p.place(x=670,y=430) 
     
 
    app1.mainloop() 
     
def clock(): 
    app2=Toplevel() 
    app2.geometry("850x110+300+10")     app2.title('Clock')     app2.configure(bg='#292e2e')     app2.resizable(False,False) 
 
    #icon 
    
image_icon=PhotoImage(file="C:/Users/dhana/OneDrive/Desktop/Image/Image/App2.png")     app2.iconphoto(False,image_icon) 
 
    def clock(): 
        text=strftime("%H:%M:%S %p")         lb1.config(text=text)         lb1.after(1000,clock) 
 
 
    lb1=Label(app2,font=('digital-7',50,'bold'),width=20,bg='#f4f5f5',fg="#292e2e")     lb1.pack(anchor='center',pady=20)     clock() 
 
app2.mainloop() 
 
def calendar(): 
    app3=Toplevel() 
    app3.geometry("300x300+-10+10")     app3.title("Calendar")     app3.configure(bg="#292e2e")     app3.resizable(False,False) 
 
    #icon 
    
image_icon=PhotoImage(file="C:/Users/dhana/OneDrive/Desktop/Image/Image/App3.png")     app3.iconphoto(False,image_icon) 
 
    mycal=Calendar(app3,setmode='day',date_pattern='d/m/yy')     mycal.pack(padx=15,pady=35) 
     
 
    app3.mainloop() 
 
##############MODE####################### button_mode=True 
 
def mode(): 
    global button_mode     if button_mode: 
        LHS.config(bg="#292e2e")         myimage.config(bg="#292e2e")         l1.config(bg="#292e2e",fg="#d6d6d6")         l2.config(bg="#292e2e",fg="#d6d6d6")         l3.config(bg="#292e2e",fg="#d6d6d6")         l4.config(bg="#292e2e",fg="#d6d6d6")         l5.config(bg="#292e2e",fg="#d6d6d6")         l6.config(bg="#292e2e",fg="#d6d6d6") 
 
        RHB.config(bg='#292e2e')         app1.config(bg='#292e2e')         app2.config(bg='#292e2e')         app3.config(bg='#292e2e')         app4.config(bg='#292e2e')         app5.config(bg='#292e2e')         app6.config(bg='#292e2e')         app7.config(bg='#292e2e')         app8.config(bg='#292e2e')         app9.config(bg='#292e2e')         app10.config(bg='#292e2e')         apps.config(bg='#292e2e',fg="#d6d6d6") 
          
        button_mode=False 
     else: 
        LHS.config(bg="#f4f5f5")         myimage.config(bg='#f4f5f5')         l1.config(bg="#f4f5f5",fg="#292e2e")         l2.config(bg="#f4f5f5",fg="#292e2e")         l3.config(bg="#f4f5f5",fg="#292e2e")         l4.config(bg="#f4f5f5",fg="#292e2e")         l5.config(bg="#f4f5f5",fg="#292e2e") 
 
        RHB.config(bg='#f4f5f5')         app1.config(bg="#f4f5f5")         app2.config(bg="#f4f5f5")         app3.config(bg="#f4f5f5")         app4.config(bg="#f4f5f5")         app5.config(bg="#f4f5f5")         app6.config(bg="#f4f5f5")         app7.config(bg="#f4f5f5")         app8.config(bg="#f4f5f5")         app9.config(bg="#f4f5f5")         app10.config(bg="#f4f5f5")         apps.config(bg="#f4f5f5",fg="#292e2e") 
         
         button_mode=True 
 
def game(): 
    app5=Toplevel() 
    app5.geometry("300x500+1170+170")     app5.title("Ludo")     app5.configure(bg="#dee2e5")     app5.resizable(False,False) 
 
    #icon 
    
image_icon=PhotoImage(file="C:/Users/dhana/OneDrive/Desktop/Image/Image/App5.png")     app5.iconphoto(False,image_icon) 
 
    ludo_image=PhotoImage(file="C:/Users/dhana/OneDrive/Desktop/Image/Image/ludo back.png") 
    Label(app5,image=ludo_image).pack() 
 
    label=Label(app5,text='',font=("time",100)) 
 
    def roll(): 
        dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685'] 
        label.configure(text=f'{random.choice(dice)}{random.choice(dice)}',fg="#29232e")         label.pack() 
 
    btn_image=PhotoImage(file="C:/Users/dhana/OneDrive/Desktop/Image/Image/ludo button.png") 
    btn=Button(app5,image=btn_image,bg="#dee2e5",command=roll)     btn.pack(padx=10,pady=10) 
 
    app5.mainloop() 
 
###############SCREENSHOT############# def screenshot():     root.iconify() 
 
    myScreenshot=pyautogui.screenshot() 
    file_path=filedialog.asksaveasfilename(defaultextension='.png')     myScreenshot.save(file_path) 
 
def file(): 
    subprocess.Popen(r'explorer /select, "C:\path\of\folder\file"') 
 
def crome(): 
    wb.register("chrome",None)     wb.open('https://www.google.com/') 
 
def close_apps(): 
    wb.register("chrome",None)     wb.open('https://www.google.com/') def close_window(): 
    root.destroy() #--------- 
RHB=Frame 
(Body,width=470,height=190,bg="#f4f5f5",highlightbackground="#adacb1",highlightthickne ss=1) 
RHB.place (x=330,y=225) 
 
apps=Label(RHB,text='Apps',font=('Acumin Variable Concept',15),bg='#f4f5f5') apps.place(x=10,y=10) 
 
app1_image=PhotoImage(file="C:/Users/dhana/OneDrive/Desktop/Image/Image/App1.png") app1=Button(RHB,image=app1_image,bd=0,command=weather) app1.place(x=15,y=50) 
 
app2_image=PhotoImage(file="C:/Users/dhana/OneDrive/Desktop/Image/Image/App2.png") app2=Button(RHB,image=app2_image,bd=0,command=clock) app2.place(x=100,y=50) 
 
app3_image=PhotoImage(file="C:/Users/dhana/OneDrive/Desktop/Image/Image/App3.png") app3=Button(RHB,image=app3_image,bd=0,command=calendar) app3.place(x=185,y=50) 
 
app4_image=PhotoImage(file="C:/Users/dhana/OneDrive/Desktop/Image/Image/App4.png") app4=Button(RHB,image=app4_image,bd=0,command=mode) app4.place(x=270,y=50) 
 
app5_image=PhotoImage(file="C:/Users/dhana/OneDrive/Desktop/Image/Image/App5.png") app5=Button(RHB,image=app5_image,bd=0,command=game) app5.place(x=355,y=50) app6_image=PhotoImage(file="C:/Users/dhana/OneDrive/Desktop/Image/Image/App6.png") app6=Button(RHB,image=app6_image,bd=0,command=screenshot) app6.place(x=15,y=120) 
 
app7_image=PhotoImage(file="C:/Users/dhana/OneDrive/Desktop/Image/Image/App7.png") app7=Button(RHB,image=app7_image,bd=0,command=file) app7.place(x=100,y=120) 
 
app8_image=PhotoImage(file="C:/Users/dhana/OneDrive/Desktop/Image/Image/App8.png") app8=Button(RHB,image=app8_image,bd=0,command=crome) app8.place(x=185,y=120) 
 
app9_image=PhotoImage(file="C:/Users/dhana/OneDrive/Desktop/Image/Image/App9.png") app9=Button(RHB,image=app9_image,bd=0,command=close_apps) app9.place(x=270,y=120) 
 
app10_image=PhotoImage(file="C:/Users/dhana/OneDrive/Desktop/Image/Image/App10.pn g") 
app10=Button(RHB,image=app10_image,bd=0,command=close_window) app10.place(x=355,y=120) 
 
root.mainloop() 
