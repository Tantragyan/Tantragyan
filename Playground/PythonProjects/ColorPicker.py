# -*- coding: utf-8 -*-
"""
Created on Thu May  7 18:23:24 2020

@author: vyomk
"""

"""
Color Picker
"""
import tkinter as tk
window = tk.Tk()


def sliderUpdate(something):
    red = redslider.get()
    green = greenslider.get()
    blue = blueslider.get()
     
    color = "#%02x%02x%02x" %  (red,green,blue)
    canvas.config(bg=color)
    
  
redslider = tk.Scale(window, form_=0, to=255, command=sliderUpdate)  
greenslider = tk.Scale(window, form_=0, to=255, command=sliderUpdate)    
blueslider = tk.Scale(window, form_=0, to=255, command=sliderUpdate)

canvas = tk.Canvas(window, width=1000, height= 500)

redslider.grid(row=1, column=1)
greenslider.grid(row=1, column=2)
blueslider.grid(row=1, column=3)
canvas.grid(row=2, column=1, columnspan=3)

window.mainloop()