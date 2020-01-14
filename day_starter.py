import tkinter as tk #standart GUI package.
from tkinter import filedialog, Text
import os #allows us to run the apps that we add to our app.

root = tk.Tk() #this holds the  app, the entire structure of the app. Somehting like a frame.
apps = [] #here we append all the apps we select to execute

if os.path.isfile('save.txt'): #loading the previously saved file apps. We create a tempApp arraye formt the save.txt file and load it in the apps array used by the definitions.
    with open('save.txt', 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = tempApps
        apps = [x for x in tempApps if x.strip()] #removing the empty spaces from the temp array and loading it in the apps array

def addApp(): #adding the function to open the file explorer to the button


    for widget in frame.winfo_children(): #removing everything forehand in the arrayd and then attaching the updated version of the list
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select File", 
    filetypes = (("executables", "*.exe"), ("allfiles" , "*.*")))

    apps.append(filename) #we append the filepath to the array

    for app in apps:
        label = tk.Label(frame, text=app, bg = "gray")
        label.pack()

def runnApp(): #Looping thru the array of apps (filepaths) and starting them
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, height = 700, width = 700, bg = "#263D42") #Here we customize the canvas
canvas.pack() #attach it ot the root of the app and this way the settings/customization are applied

frame = tk.Frame(root, bg = 'white') #add a container/frame inside the canvas
frame.place(relwidth=0.8, relheight = 0.8, relx = 0.1, rely = 0.1) #add customization to the container/frame like placing inside the canvas, color etc.

openFile = tk.Button(root, text = 'Open App', padx = 10, pady = 5, fg = "white", bg ='#263D42', command = addApp) #we create and customize a button
openFile.pack() #attach the button to the root of the app

runApps = tk.Button(root, text = 'Run App', padx = 10, pady = 5, fg = "white", bg ='#263D42', command= runnApp) #we create and customize a button
runApps.pack()

for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()
    
root.mainloop()

with open('save.txt', 'w') as f: #we save the apps paths we added to our App in a text file
    for app in apps:
        f.write(app + ',')
