import customtkinter
customtkinter.deactivate_automatic_dpi_awareness()
class DisplayGUI:
    def __init__(self):
        self.display_setup()

    def login(self):
        print("Test login")

    def display_setup(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        self.root = customtkinter.CTk()
        self.root.geometry("500x350")

        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=False)

        # Create a canvas
        self.canvas = customtkinter.CTkCanvas(master=self.frame)
        self.canvas.pack(fill="both", expand=True)

    def add_component(self, component):
        component.pack(pady=12, padx=10)

    def run(self):
        self.root.mainloop()
