#!/usr/bin/env python3

from tkinter import *
import math
import tkinter.messagebox
from tkmacosx import Button



# from cx_Freeze import setup, Executable
# base = None
# executables = [Executable("calculator.py", base=base)]
# packages = ["idna"]
# options = {
#     'build_exe': {    
#         'packages':packages,
#     },
# }
# setup(
#     name = "Anto's Calculator",
#     options = options,
#     version = "1.0",
#     description = 'My calculator',
#     executables = executables
# )


calc_input = ""
operation = ""

def input_key(value):
  global calc_input
  global operation
  calc_input += str(value)


  #print(calc_input)
  calc_input_text.set(calc_input)
  if value == "+":
    operation = "+"
  if value == "-":
    operation = "-"
  if value == "x":
    operation = "x"
  if value == "÷":
    operation = "÷"

def equal():
  global calc_input
  global operation
  result = 0

  if operation == "+":
    additions = calc_input.split("+")
    print("addition", additions)
    for value in additions:       
      result += float(value)
  
  if operation == "-":
    soustractions = calc_input.split("-")
    for value in soustractions:
      result = -result - float(value)

  if operation == "x":
    multiplication = calc_input.split("x")
    result = 1 
    for value in multiplication:
      print(value, result)
      result = result * float(value)

  if operation == "÷":
    division = calc_input.split("÷")
    result = int(division[0])
    for value in division[1:]: 
      #print(value, result)
      result = result / float(value)
      #print(value, result)

  
  calc_input = ""
  calc_input_text.set(calc_input)
  result_text.set(result)
  #print(result)

def square():
  global calc_input
  result = int(calc_input) * int(calc_input)

  calc_input = ""
  calc_input_text.set(calc_input)
  result_text.set(result)

def percent():
  global calc_input
  result = int(calc_input) / 100

  calc_input = ""
  calc_input_text.set(calc_input)
  result_text.set(result)

def cos():
  global calc_input
  result = math.cos(float((calc_input)))
  calc_input_text.set(calc_input)
  result_text.set(result)
  print(result)
  
def tan():
  global calc_input
  result = math.tan(float((calc_input)))
  calc_input_text.set(calc_input)
  result_text.set(result)
  print(result)
  
def sin():
  global calc_input
  result = math.sin(float((calc_input)))
  calc_input_text.set(calc_input)
  result_text.set(result)
  print(result)

def exp():
  global calc_input
  e = calc_input.split("e")
  result = float(e[0])
  for value in e:
    result = float(value) * math.e
    calc_input_text.set(calc_input)
    result_text.set(result)
  print(result)



def clear():
  global calc_input
  global operation

  calc_input = ""
  operation = ""

  calc_input_text.set(calc_input)
  result_text.set(calc_input)
  result_bin.set(calc_input)

def base():
  global calc_input
  value = var.get()

  if value == 2:
    bina = bin(int(calc_input))
    result_bin.set(bina)
    calc_input=""
    calc_input_text.set(calc_input)

  if value == 10:
    i=0
    toDec = result_bin.get()
    toDec2 = result_text.get()
    length_str=len(toDec)
    length_str2=len(toDec2)


    sliced_toDec=toDec[length_str::-1]
    sliced_toDec2=toDec2[length_str2::-1] 
 
    decimal = 0
    if toDec:
      #print("bin")
      for val in sliced_toDec:
        if val =="b":
          break
        decimal += ((int(val))*(2**i))
        i+=1
      result_text.set(decimal)
    if toDec2:
      print("hex")
      for val in sliced_toDec2:
        if val =="x":
          break
        decimal += (int(val)*(16**i))
        i+=1
      result_text.set(decimal)

    else:
      print("hexa")

  if value == 16:
    hexa = hex(int(calc_input))
    result_text.set(hexa)
    calc_input=""
    calc_input_text.set(calc_input)



window = Tk()
window.configure(background="black")
window.title("Anto's Calculator")
window.geometry("490x280")
window.resizable(0, 0)



def Scientific():
  window.geometry("490x280+0+0")
 
 
def Standard():
  window.geometry("390x280+0+0")

def Quit():
  # window.quit()
  Quit = tkinter.messagebox.askyesno("Anto's Calculator", "Do you want to exit ?")

  if Quit > 0:
    window.destroy()
    return

menubar = Menu(window)


filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = "Standard", command = Standard)
filemenu.add_command(label = "Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = Quit)


window.config(menu=menubar)

var = IntVar()
R1 = Radiobutton(window, text="2", variable=var, value=2, command=base)
R1.grid(row=0, column=4)
R2 = Radiobutton(window, text="10", variable=var, value=10, command=base)
R2.grid(row=1, column=4)
R3 = Radiobutton(window, text="16", variable=var, value=16, command=base)
R3.grid(row=2, column=4)


# value = DoubleVar()
# scale = Scale(window, variable=value, length=50, orient=HORIZONTAL, from_=8, to=16)
# scale.grid(row=2, column=4)
# scale.set(10)

#Button(window, text="Fermer", command=window.quit).grid(row=0, column=3)

Button(window, text=" AC ", bg="orange", command=lambda: clear()).grid(row=3, column=0)
Button(window, text=" ² ", command=lambda: square()).grid(row=3, column=1)
Button(window, text=" % ", command=lambda: percent()).grid(row=3, column=2)
Button(window, text=" e ", command=lambda: exp()).grid(row=3, column=4)
Button(window, text=" tan ", command=lambda: tan()).grid(row=4, column=4)
Button(window, text=" cos ", command=lambda: cos()).grid(row=5, column=4)
Button(window, text=" sin ", command=lambda: sin()).grid(row=6, column=4)

Button(window, text=" . ", command=lambda: input_key(".")).grid(row=7, column=2)
Button(window, text=" 0 ", width=190, command=lambda: input_key("0")).grid(row=7, column=0, columnspan = 2)
Button(window, text=" 1 ", command=lambda: input_key("1")).grid(row=6, column=0)
Button(window, text=" 2 ", command=lambda: input_key("2")).grid(row=6, column=1)
Button(window, text=" 3 ", command=lambda: input_key("3")).grid(row=6, column=2)
Button(window, text=" 4 ", command=lambda: input_key("4")).grid(row=5, column=0)
Button(window, text=" 5 ", command=lambda: input_key("5")).grid(row=5, column=1)
Button(window, text=" 6 ", command=lambda: input_key("6")).grid(row=5, column=2)
Button(window, text=" 7 ", command=lambda: input_key("7")).grid(row=4, column=0)
Button(window, text=" 8 ", command=lambda: input_key("8")).grid(row=4, column=1)
Button(window, text=" 9 ", command=lambda: input_key("9")).grid(row=4, column=2)

Button(window, text=" ÷ ", bg="orange", command=lambda: input_key("÷")).grid(row=3, column=3)
Button(window, text=" x ", bg="orange", command=lambda: input_key("x")).grid(row=4, column=3)
Button(window, text=" + ", bg="orange", command=lambda: input_key("+")).grid(row=5, column=3)
Button(window, text=" - ", bg="orange", command=lambda: input_key("-")).grid(row=6, column=3)
Button(window, text=" = ", bg="orange", command=lambda: equal()).grid(row=7, column=3)

calc_input_text = StringVar()
calc_input_text.set("0.")
Label(window, width=35, height=2, font=('arial', 18, 'bold'), bg="black", textvariable=calc_input_text).grid(row=0, column=0, columnspan = 4)
result_text = StringVar()
Label(window, width=35, height=2, font=('arial', 18, 'bold'), bg="black", textvariable=result_text).grid(row=1, column=0, columnspan = 4)
result_bin = StringVar()
Label(window, width=35, height=2, font=('arial', 18, 'bold'), bg="black", textvariable=result_bin).grid(row=2, column=0, columnspan = 4)

window.mainloop()