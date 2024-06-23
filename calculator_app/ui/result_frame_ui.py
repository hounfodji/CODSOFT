import customtkinter


class ResultFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.resultbox = customtkinter.CTkTextbox(self)
        self.resultbox.grid(row=0, column=0, padx=10,sticky="nsew")

        
