import tkinter as tk
from tkinter import filedialog as fd
import GeneratorPage
import TrainPage

class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.selected = tk.BooleanVar()
        self.file = False
        self.save_folder = False
        self.filetypes = {
            True:(('IMAGE', ('*.png','*.jpg','*.jpeg')),),
            False:(('VIDEO', ('*.mp4','*.avi')),),
        }

        #Menu Button
        self.menu_button = tk.Button(self, text="Menu",relief="sunken")
        self.menu_button.grid(row = 0, column = 0)

        #Generator Button
        self.generator_button = tk.Button(self, text="Generator", state = tk.DISABLED,command=lambda: controller.show_frame(GeneratorPage.GeneratorPage))
        self.generator_button.grid(row = 0, column = 1)

        #Train Button
        self.train_button = tk.Button(self,text="Train",state = tk.DISABLED,command=lambda: controller.show_frame(TrainPage.TrainPage))
        self.train_button.grid(row = 0, column = 2)
      
        #Photo option
        self.photo = tk.Radiobutton(self, text='photo', value=True, variable=self.selected)
        self.photo.grid(row=1,column=3)

        #Video option
        self.video = tk.Radiobutton(self, text='video', value=False, variable=self.selected)
        self.video.grid(row=1,column=4)
        
        #filename dialog
        self.file_button = tk.Button(self,text="Ouvrir un fichier",command=lambda:self.askOpenFile() )
        self.file_button.grid(row=2,column=4)

        #path input
        self.pathfile = tk.Entry(self, state =tk.DISABLED)
        self.pathfile.grid(row=2,column=5,columnspan=3)

        #save_filename dialog
        self.save_button = tk.Button(self,text="Sélectionner le dossier",command=lambda:self.askOpenDirectory() )
        self.save_button.grid(row=3,column=4)

        #save_path input
        self.save_path = tk.Entry(self, state =tk.DISABLED)
        self.save_path.grid(row=3,column=5,columnspan=3)

        #Generate Button
        self.generate_button = tk.Button(self, text="Generate", state = tk.DISABLED,command=lambda: controller.show_frame(GeneratorPage.GeneratorPage))
        self.generate_button.grid(row = 7, column = 5)

    def askOpenFile(self):
        self.file = fd.askopenfile(filetypes=self.filetypes[self.selected.get()])
        if self.file:
            self.pathfile['state'] = tk.NORMAL
            self.pathfile.insert(index=0,string=self.file.name)
            self.pathfile['state'] = tk.DISABLED

            #put generator button enabled
            if  self.file and self.save_folder:
                self.generator_button['state'] = tk.NORMAL
                self.generate_button['state'] = tk.NORMAL
        else:
            self.pathfile['state'] = tk.NORMAL
            self.pathfile.delete(0, tk.END)
            self.pathfile['state'] = tk.DISABLED

            self.generator_button['state'] = tk.DISABLED
            self.generate_button['state'] = tk.DISABLED

    def askOpenDirectory(self):
        self.save_folder = fd.askdirectory()
        if self.save_folder:
            self.save_path['state'] = tk.NORMAL
            self.save_path.insert(index=0,string=self.save_folder)
            self.save_path['state'] = tk.DISABLED

            #put generator button enabled
            if  self.file and self.save_folder:
                self.generator_button['state'] = tk.NORMAL
                self.generate_button['state'] = tk.NORMAL
        else:
            self.save_path['state'] = tk.NORMAL
            self.save_path.delete(0, tk.END)
            self.save_path['state'] = tk.DISABLED

            self.generator_button['state'] = tk.DISABLED
            self.generate_button['state'] = tk.DISABLED


        