import tkinter as tk
import GeneratorPage
import MenuPage

class TrainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #Menu Button
        self.menu_button = tk.Button(self, text="Menu",command=lambda: controller.show_frame(MenuPage.MenuPage))
        self.menu_button.grid(row = 0, column = 0)

        #Generator Button
        self.generator_button = tk.Button(self, text="Generator",command=lambda: controller.show_frame(GeneratorPage.GeneratorPage))
        self.generator_button.grid(row = 0, column = 1)

        #Train Button
        self.train_button = tk.Button(self, text="Train",relief="sunken")
        self.train_button.grid(row = 0, column = 2)
