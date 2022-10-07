import tkinter as tk
import MenuPage
import TrainPage
import cv2
import os
from PIL import Image,ImageTk

class GeneratorPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.menu:MenuPage.MenuPage = controller.get_frame(MenuPage.MenuPage)
        self.img = None
        self.images = {}
        self.h = self.controller.h # app heigth
        self.w = self.controller.w # app width
        self.nbRects = 0
        self.rects = {}
        self.rectX = -1
        self.rectY = -1

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
        self.validate_button = tk.Button(self, text="Valider")
        self.validate_button.grid(row = 1, column =1)

        #Erase Button
        self.erase_button = tk.Button(self, text="Effacer")
        self.erase_button.grid(row = 2, column = 1)

        #Cancel Button
        self.cancel_button = tk.Button(self, text="Annuler")
        self.cancel_button.grid(row = 3, column = 1)

        #binding for mouse motion
        self.canvas.bind("<Button-1>", self.click)

    def click(self,event):
        if self.rectX!= event.x and self.rectY!=event.y:
            if self.rectX==-1 or self.rectY==-1: # first initialization
                self.rectX = event.x
                self.rectY = event.y
            else:
                self.canvas.create_rectangle((self.rectX, self.rectY), (event.x, event.y))
                self.rectX=-1
                self.rectY=-1
        else: # do nothing
            pass


    def updateImg(self):
        directory = os.path.join(self.menu.save_path.get(),'data')
        
        try:
            # creating a folder named data
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print ('Error: Creating directory')

        try:#photo
            self.img = Image.open(self.menu.file.name)
            # self.img.thumbnail((h,w), Image.ANTIALIAS)
            self.img.thumbnail((self.w*70/100,self.h*70/100), Image.ANTIALIAS)
            self.imgTk = ImageTk.PhotoImage(image=self.img)
        except:#video
            cam = cv2.VideoCapture(self.menu.file.name)
            currentframe = 0
            while(True):
                # reading from frame
                ret,frame = cam.read()
                if ret:
                    # if video is still left continue creating images
                    name = str(currentframe) + '.jpg'
                    # increasing counter so that it will
                    # show how many frames are created
                    self.images[currentframe] = currentframe
                    currentframe += 1
                else:
                    break
            self.img = self.images["0.jpg"] #get the first image

        self.canvas.destroy()
        self.canvas:tk.Canvas = tk.Canvas(self, cursor="tcross",width= self.w*70/100, height= self.h*70/100)
        self.canvas.create_image(0,0,anchor=tk.NW,image=self.imgTk)
        self.canvas.grid(row=2,column=3)

        #binding for mouse motion
        self.canvas.bind("<Button-1>", self.click)




