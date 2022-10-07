import tkinter as tk
from MenuPage import MenuPage
from GeneratorPage import GeneratorPage
from TrainPage import TrainPage

class HaarApp():
    def __init__(self,name) -> None:
        self.root = tk.Tk()
        self.frames = {}
        self.root.title(name)
        self.root.iconbitmap('./logo_haar_np_generator.ico')
        self.w, self.h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (self.w, self.h))
        self.root.resizable(width=False,height=False)

        container = tk.Frame(self.root) 
        container.pack(side = "top", fill = "both", expand = True)

        for F in (MenuPage, GeneratorPage, TrainPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(MenuPage)

    def get_frame(self,cont)->tk.Frame:
        return self.frames[cont]

    def show_frame(self, cont):
        if(cont==GeneratorPage):
            self.frames[cont].updateImg()
        frame:tk.Frame = self.frames[cont]
        frame.tkraise()

    def start(self):
        self.root.mainloop() # start the main window