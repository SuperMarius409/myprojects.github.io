import tkinter as tk
import time
"""from tkinter import filedialog
root = tk.Tk()
root.withdraw()
path = filedialog.askopenfilename(filetypes=(("text files","*.txt"), ("all files","*.*")))
print(path,'\n')
with open(path, 'r') as f:
    text = f.read()
print(text,'\n')"""
text = input('Paste here')
replace = text.replace('t', 'C4')\
    .replace('1', 'C2')\
    .replace('2', 'D2')\
    .replace('3', 'E2')\
    .replace('4', 'F2')\
    .replace('5', 'G2')\
    .replace('6', 'A2')\
    .replace('7', 'B2')\
    .replace('8', 'C3')\
    .replace('9', 'D3')\
    .replace('0', 'E3')\
    .replace('q', 'F3')\
    .replace('w', 'G3')\
    .replace('e', 'A3')\
    .replace('r', 'B3')\
    .replace('t', 'C4')\
    .replace('y', 'D4')\
    .replace('u', 'E4')\
    .replace('i', 'F4')\
    .replace('o', 'G4')\
    .replace('p', 'A4')\
    .replace('a', 'B4')\
    .replace('s', 'C5')\
    .replace('d', 'D5')\
    .replace('f', 'E5')\
    .replace('g', 'F5')\
    .replace('h', 'G5')\
    .replace('j', 'A5')\
    .replace('k', 'B5')\
    .replace('l', 'C6')\
    .replace('z', 'D6')\
    .replace('x', 'E6')\
    .replace('c', 'F6')\
    .replace('v', 'G6')\
    .replace('b', 'A6')\
    .replace('n', 'B6')\
    .replace('m', 'C7')
print('This is the replacement: \n')
print(replace)
time.sleep(7)