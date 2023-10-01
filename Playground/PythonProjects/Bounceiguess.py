from tkinter import *
import random
import time
class Ball:
 def __init__(self, canvas, paddle, color):
     self.canvas = canvas
     self.paddle = paddle
     self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
     self.canvas.move(self.id, 245, 100)
     starts = [-3, -2, -1, 1, 2, 3]
     random.shuffle(starts)
     self.x = starts[0]
     self.y = -3
     self.canvas_height = self.canvas.winfo_height()
     self.canvas_width = self.canvas.winfo_width()
     self.hit_bottom = False