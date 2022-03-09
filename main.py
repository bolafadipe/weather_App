import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.messagebox import showerror

from weather_info import get_weather
#from app_controller import show_weather
import requests
import json
import datetime


#get_weather()
class InputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
       
        # setup the grid layout manager
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        #self.configure(background='#34c6eb')

         # Initialize style
        self.style = ttk.Style()
        # Create style used by default for all Frames
        self.style.configure('TFrame', background='#a86cd9')


        # self.rowconfigure(0, weight=1)
        # self.rowconfigure(1, weight=4)
        

        self.__create_widgets()

    #def __create_widgets(self):
        # Find what
        
        

    

    def __create_widgets(self):
        ttk.Label(self, text='Search City:').grid(column=0, row=0, sticky=tk.W)
        self.text = tk.StringVar()
        self.city_field = ttk.Entry(self, width=30, textvariable=self.text)
        self.city_field.focus()
        self.city_field.grid(column=1, row=0, sticky=tk.W)
        #print(self.city_field.get())

        # Replace with:
        self.search_btn = ttk.Button(self, text='Get Weather', command=self.show_weather).grid(column=1, row=1, sticky=tk.N)

        
        # ttk.Label(self, text='Replace with:').grid(
        #     column=0, row=1, sticky=tk.W)
        # replacement = ttk.Entry(self, width=30)
        # replacement.grid(column=1, row=1, sticky=tk.W)

        

        for widget in self.winfo_children():
            widget.grid(padx=5, pady=5)

#class OutputFrame(ttk.Frame):

    

      
    def show_weather(self):
        self.city_input = self.city_field.get()
        print(self.city_input)
        
        
        if self.city_input == '':
            return showerror('Please enter city name')

        else:
            self.city_weather = get_weather(self.city_field.get())
            
            self.location = ttk.Label(text=self.city_weather[0], background='#42a0ed', font={'Verdana', 'bold', 60}).grid(column=1, row=2,columnspan=2,  ipadx=5, ipady=5, pady=15)
            #self.country = ttk.Label(self, text=self.city_weather[1], background='#6da9c7', font={'bold', 48}).grid(column=1, row=3)
            self.temp_info = ttk.Label(text=self.city_weather[1], background='#42a0ed', font={'Verdana', 'bold', 36}).grid(column=1, row=3, columnspan=2, pady=10)
            self.fills_like_info = ttk.Label(text=f'Feels Like: {self.city_weather[2]}', background='#42a0ed' , font={'Verdana', 'bold', 36}).grid(column=1, row=4, columnspan=2, pady=10)
            self.weather_icon = ttk.Label(text=self.city_weather[3], background='#42a0ed' , font={'Verdana', 'bold', 36}).grid(column=1, row=5, columnspan=2, pady=10)
            self.weather_description = ttk.Label(text=self.city_weather[4], background='#42a0ed' , font={'Verdana', 'bold', 36}).grid(column=1, row=6, columnspan=2, pady=10)
            #self.pressure = ttk.Label(text=f'Pressure: {self.city_weather[5]}', background='#42a0ed' , font={'Verdana', 'bold', 36}).grid(column=1, row=7, columnspan=2, pady=10)
            self.humidity = ttk.Label(text=f'Humidity: {self.city_weather[6]}', background='#42a0ed' , font={'Verdana', 'bold', 36}).grid(column=1, row=8, columnspan=2, pady=10)
            self.wind_speed = ttk.Label(text=f'wind speed: {self.city_weather[7]}', background='#42a0ed' , font={'Verdana', 'bold', 36}).grid(column=1, row=9, columnspan=2, pady=10)
            
        # for widget in self.winfo_children():
        #     widget.grid(padx=5, pady=5)
               
   

        self.city_field.delete(0, END) 



class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Weather App')
        self.option_add('*Font', '30')
        self.geometry('700x500')
        self.resizable(False, False)
        self.iconbitmap('C:/Users/admin/Desktop/weather/sunny_sun_cloud_weather_cloudy_icon_194237.ico')

        # layout on the root window
        # self.rowconfigure(0, weight=1)
        # self.rowconfigure(1, weight=5)

        self.configure(background='#42a0ed')

        # self.rowconfigure(0, weight=1)
        # self.rowconfigure(1, weight=4)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        # create the input frame
        input_frame = InputFrame(self)
        input_frame.grid(column=1, row=0, columnspan=2, pady=5, sticky=tk.EW)

        # # create the button frame
        # button_frame = OutputFrame(self)
        # button_frame.grid(column=1, row=1, columnspan=2)


if __name__ == '__main__':
    window = App()
   
    # InputFrame(window)
    # OutputFrame(window)
    window.mainloop()