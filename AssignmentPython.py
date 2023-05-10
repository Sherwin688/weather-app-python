''' Weather Application By

    R/BCA-20-225

Features: Gets weather data scraped from timeanddate.com of any state of India.
Displays temperature
Displays Type of Weather
Displays a picture depending on the type of weather
Background colour changes according to type of weather
used tkinter, PIL and Beautiful soup library
'''





from tkinter import *
from PIL import ImageTk,Image
from bs4 import BeautifulSoup
import requests

root=Tk()
root.geometry('400x400')
root.title('Weather App')
root.resizable(width=False, height=False)

def hide_frames():
    for widget in search_frame.winfo_children():
        widget.destroy()
    search_frame.pack_forget()
    label_img.pack()
    e.delete(0,'end')

def search():
    try:
        global search_frame
        label_img.pack_forget() 
        
        search_frame=LabelFrame(root,bg='black',width=400,height=400)
        search_frame.pack(ipadx=200,ipady=200)
        
           
        #scrape
        place=e.get()
        if place=='':
            place_text='India'
        else:
            place_text=place.title()
            
       
        
            
        html_text=requests.get('https://www.timeanddate.com/weather/india/'+place).text
        soup = BeautifulSoup(html_text, 'lxml')
        place=soup.find('h1',class_='headline-banner__title')
        container=soup.find('div',class_='bk-focus__qlook')
        w_type=container.find_all('p')
        temp=container.find('div',class_='h2')
        containter2=soup.find('table',class_='table table--left table--inner-borders-rows')
          
        weather_type_text=w_type[1].text
        print(weather_type_text)
        temp_text=temp.text  
            #scrape-end
            
            #labels
        place_label=Label(search_frame,text=place_text,font=('helvetica',13,'bold'),anchor="center")
        place_label.pack(pady=20)
        global label_mg1
        bakgrnd='white'
        w_type_descision='partlycloudy.png'
        if 'Clear' in weather_type_text:
            w_type_descision='partlysunny.jpg'
            bakgrnd='yellow3'
            print('1')
                
        elif 'Partly cloudy' in weather_type_text or 'Passing clouds'in weather_type_text:
            w_type_descision='partlycloudy.png'
            bakgrnd='blue3'
            print('2')
                
        elif 'Sunny'in weather_type_text:
            w_type_descision='sunny.jpg'
            bakgrnd='yellow'
            print('3')
                
        elif 'Haze' in weather_type_text or 'Fog' in weather_type_text or 'Clouds' in weather_type_text:
            w_type_descision='cloudy.jpg'
            bakgrnd='blue4'
            print('4')
            
        search_frame.config(bg=bakgrnd)
      
            
        label_mg1=ImageTk.PhotoImage(Image.open(w_type_descision))
        label_img1=Label(search_frame,image=label_mg1)
        label_img1.pack(pady=20)
            
            
        weather_type_label=Label(search_frame,anchor="center",text=weather_type_text,font=('helvetica',15),bg='white')
        weather_type_label.pack(ipadx=200)
            
        temp_label=Label(search_frame,text=temp_text,anchor="center",font=('helvetica',15),bg='white',bd=1)
        temp_label.pack(ipadx=50)
            #labels
        button2=Button(search_frame,text='back',command=hide_frames).pack(pady=20)
    except:
        print("Error occured,re-open app")
    
#labels2
label_mg=ImageTk.PhotoImage(Image.open('weather_app.jpg'))
global label_img
label_img=Label(image=label_mg)
label_img.pack()

#Entry and buttons
e = Entry(root,font=('helvetica',14),bd=2)
e.place(x = 72, y = 242)
button=Button(root,text='Get Details',command=search).place(x = 165, y = 300)

root.mainloop()

