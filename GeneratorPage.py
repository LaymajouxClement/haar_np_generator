import tkinter as tk
import MenuPage
import TrainPage
import cv2
import os
from PIL import Image,ImageTk,ImageDraw

class GeneratorPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.menu:MenuPage.MenuPage = controller.get_frame(MenuPage.MenuPage)
        self.img = None
        self.images = {}
        self.h = self.controller.h # app heigth
        self.w = self.controller.w # app width
        self.nbImage = 0
        self.rects = {}
        self.image_rects = []
        self.rectX = -1
        self.rectY = -1
        self.directory = ""

        #Menu Button
        self.menu_button = tk.Button(self, text="Menu",command=lambda: controller.show_frame(MenuPage.MenuPage))
        self.menu_button.grid(row = 0, column = 0)

        #Generator Button
        self.generator_button = tk.Button(self, text="Generator",relief="sunken")
        self.generator_button.grid(row = 0, column = 1)

        #Train Button
        self.train_button = tk.Button(self, text="Train",state = tk.DISABLED,command=lambda: controller.show_frame(TrainPage.TrainPage))
        self.train_button.grid(row = 0, column = 2)

        #Video/Photo
        self.imgTk = ImageTk.PhotoImage(image=Image.open("C:\\Users\\Clément\\Desktop\\haar-np-generator\\images\\blank.png"))
        self.canvas:tk.Canvas = tk.Canvas(self, cursor="tcross",width= self.w*70/100, height= self.w*70/100)
        self.canvas.create_image(0,0,anchor=tk.NW,image=self.imgTk)
        self.canvas.grid(row=2,column=3)

        #Validate Button
        self.validate_button = tk.Button(self, text="Valider",command=lambda: self.validate())
        self.validate_button.grid(row = 1, column =1)

        #Erase Button TODO
        # self.erase_button = tk.Button(self, text="Effacer")
        # self.erase_button.grid(row = 2, column = 1)

        #Cancel Button TODO
        # self.cancel_button = tk.Button(self, text="Annuler")
        # self.cancel_button.grid(row = 3, column = 1)

        #binding for mouse motion
        self.canvas.bind("<Button-1>", self.click)

    def validate(self,isPhoto:bool=True):
        self.rects[self.nbImage] = self.image_rects # warning see if it's an hard copy
        self.image_rects = []
        
        #save photo in data
        self.img.save(os.path.join(self.directory,'positive',str(self.nbImage)+'.png'),'png')
        # transform canva to negative canva
        img = ImageDraw.Draw(self.img)
        for rect in self.rects[self.nbImage]:
            img.rectangle(rect,fill="white")
        self.img.save(os.path.join(self.directory,'negative',str(self.nbImage)+'.png'),'png')
        #TODO ! ! ! UPDATE DAT FILES

        self.nbImage = self.nbImage +1
        if isPhoto==True:#after validate return to menu for a photo
            self.controller.show_frame(MenuPage.MenuPage)
            self.canvas

    def click(self,event):
        if self.rectX!= event.x and self.rectY!=event.y:
            if self.rectX==-1 or self.rectY==-1: # first initialization / every 2 clicks
                self.rectX = event.x
                self.rectY = event.y
            else:
                self.canvas.create_rectangle((self.rectX, self.rectY), (event.x, event.y))
                self.image_rects.append((self.rectX, self.rectY,event.x, event.y))
                self.rectX=-1
                self.rectY=-1
        else: # do nothing
            pass


    def updateImg(self):
        self.directory = self.menu.save_path.get()
        
        try:
            # creating folders if needed
            if not os.path.exists(os.path.join(self.directory,"positive")):
                os.makedirs(os.path.join(self.directory,"positive"))
            if not os.path.exists(os.path.join(self.directory,"negative")):
                os.makedirs(os.path.join(self.directory,"negative"))
        except OSError:
            print ('Error: Creating directory')

        try:#photo
            self.img = Image.open(self.menu.file.name)
            # self.img.thumbnail((h,w), Image.ANTIALIAS)
            self.img.thumbnail((self.w*70/100,self.h*70/100), Image.ANTIALIAS)
            self.imgTk = ImageTk.PhotoImage(image=self.img)
        except:#video
            cam = cv2.VideoCapture(self.menu.file.name)

            _,frame = cam.read()
            self.img = Image.fromarray(frame)
            self.img.thumbnail((self.w*70/100,self.h*70/100), Image.ANTIALIAS)
            self.imgTk = ImageTk.PhotoImage(image=self.img)

        self.canvas.destroy()
        self.canvas:tk.Canvas = tk.Canvas(self, cursor="tcross",width= self.w*70/100, height= self.h*70/100)
        self.canvas.create_image(0,0,anchor=tk.NW,image=self.imgTk)
        self.canvas.grid(row=2,column=3,padx=(0,0),pady=(0,0))

        #binding for mouse motion
        self.canvas.bind("<Button-1>", self.click)




