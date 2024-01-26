import customtkinter as customtkinter
from settings import *

try:
    from ctypes import windll,byref,sizeof,c_int
except:
    pass

class App(customtkinter.CTk):
    def __init__(self):        
        
        #window setup
        super().__init__(fg_color=GREEN)
        self.title('')
        #self.iconbitmap('empty.ico')
        self.geometry('400x400')
        self.resizable(False,False)
        self.change_title_bar_color()
        
        
        #layout
        self.columnconfigure(0,weight=1)
        self.rowconfigure((0,1,2,3),weight=1,uniform='a')
        
        #widgets
        ResultText(self)
        WeightInput(self)
        HeightInput(self)
        UnitSwitcher(self)
    
    
        self.mainloop()
    
    def change_title_bar_color(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWWA_ATTRIBUTE = 35
            COLOR = TITLE_HEX_COLOR
            windll.dwmapi.DwmSetWindowAttribute(HWND,DWMA_ATTRIBUTE, byref(c_int(COLOR)),sizeof(c_int))
        except:
            pass    


class ResultText(customtkinter.CTkLabel):
    def __init__(self,parent):
        font = customtkinter.CTkFont(family=FONT,size=MAIN_TEXT_SIZE,weight='bold')
        super().__init__(master=parent,text=22.5 ,text_color=WHITE,font=font)
        self.grid(column =0, row =0 , rowspan=2 , sticky = 'nsew')

class WeightInput(customtkinter.CTkFrame):
    def __init__(self,parent):
        super().__init__(master=parent,fg_color=WHITE)
        self.grid(column =0,row=2,sticky='nsew', padx=10, pady=10)
        
        #layout
        self.rowconfigure(0,weight=1,uniform='b')
        self.columnconfigure(0,weight=2,uniform='b')
        self.columnconfigure(1,weight=1,uniform='b')
        self.columnconfigure(2,weight=3,uniform='b')
        self.columnconfigure(3,weight=1,uniform='b')
        self.columnconfigure(4,weight=2,uniform='b')
        
        #widgets
        font = customtkinter.CTkFont(family=FONT, size=INPUT_FONT_SIZE)
    
        label = customtkinter.CTkLabel(self,text='70Kg',text_color=BLACK, font=font)
        label.grid(row=0,column=2)
        
        #buttons
        
        minus_button = customtkinter.CTkButton(self,text='-',font=font, text_color=BLACK,fg_color=LIGHT_GRAY,hover_color=GRAY, corner_radius=BUTTON_CORNER_RADIUS)
        minus_button.grid(row=0,column=0 ,sticky='nswe')

        plus_button = customtkinter.CTkButton(self,text='+',font=font, text_color=BLACK,fg_color=LIGHT_GRAY,hover_color=GRAY, corner_radius=BUTTON_CORNER_RADIUS)
        plus_button.grid(row=0,column=4,sticky='nswe')
        
    
        small_plus_button = customtkinter.CTkButton(self,text='+',font=font, text_color=BLACK,fg_color=LIGHT_GRAY,hover_color=GRAY, corner_radius=BUTTON_CORNER_RADIUS)
        small_plus_button.grid(row=0,column=3,ipady=4 ,padx=2)
        
        small_minus_button = customtkinter.CTkButton(self,text='-',font=font, text_color=BLACK,fg_color=LIGHT_GRAY,hover_color=GRAY, corner_radius=BUTTON_CORNER_RADIUS)
        small_minus_button.grid(row=0,column=1 ,ipady=4 ,padx=2)
        


class HeightInput(customtkinter.CTkFrame):
    def __init__(self,parent):
        super().__init__(master=parent,fg_color=WHITE)
        self.grid(row = 3, column=0, sticky='nsew' , padx=10 ,pady=10)
        
        font = customtkinter.CTkFont(family=FONT, size=INPUT_FONT_SIZE)
        #widgets
        slider =customtkinter.CTkSlider(
            master=self,
            button_color=GREEN,
            button_hover_color=GRAY,
            progress_color=GREEN,
            fg_color=LIGHT_GRAY)
        
        slider.pack(side = 'left', fill='x', expand= True,pady = 10 , padx =10)
        
        output_text = customtkinter.CTkLabel(self,text="1.86m", text_color=BLACK , font=font)
        output_text.pack(side='left' ,padx=20)
        

class UnitSwitcher(customtkinter.CTkLabel):
    def __init__(self,parent):
        super().__init__(master=parent,text='metric',text_color=DARK_GREEN,font=customtkinter.CTkFont(family=FONT,size=SWITCH_FONT_SIZE,weight='bold'))
        
        self.place(relx=0.98,rely=0.01, anchor='ne')
        
        
        
        
if __name__=='__main__':
    App()