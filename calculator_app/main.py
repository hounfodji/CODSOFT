import customtkinter

from ui.operation_frame_ui import OperationsFrame
from ui.result_frame_ui import ResultFrame

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__() 
        
        
        
        self.title("C A L C U L A T O R")
        self.geometry("350x450")
        self.minsize(350,450)
        self.maxsize(1500, 1000)
        # self.resizable(width=True,height=False)
        # self.grid_rowconfigure((1), minsize=100, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        self.resultbox_frame = ResultFrame(self)
        self.resultbox_frame.grid(row=0, column=0, padx=10,sticky="nsew")
        
        self.checkbox_frame = OperationsFrame(self)
        self.checkbox_frame.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nsew")
        
        
        
        
app = App()
app.mainloop()