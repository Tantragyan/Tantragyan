# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:59:04 2020

@author: vyomk
"""

import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor

root = tk.Tk()
style = ttk.Style(root)

print(askcolor((255, 255, 0), root))
root.mainloop()
