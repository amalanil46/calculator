import tkinter as tk

LIGHT_GRAY ="#F5F5F5"
class calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")

        self.display_frame = self.creat_display_frame()
        self.buttons_frame = self.creat_buttons_frame()

    def creat_display_frame(self):
        frame = tk.Frame(self.window, height=221,bg=LIGHT_GRAY)
        frame.pack(expand=True,fill="both")
        return frame

    def creat_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True,fill="both")



    def run(self):
         self.window.mainloop()

if __name__ =="__main__":
    calc=calculator()
    calc.run()


