import tkinter as tk
from template import Template

class Gui:
    """Create a GUI for the application"""
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("smalltalk")
        self.window.geometry("1500x1000")

        self.nav_bar = tk.Frame(self.window)
        self.template_frame = tk.Frame(self.window)
        self.output_frame = tk.Frame(self.window)

        # Navigation bar
        tk.Label(self.nav_bar, text="Navigation Bar", font=("Arial", 24)).grid(row=1, column=1)

        self.nav_bar.grid(row=1, column=1)

        self.window.mainloop()

if __name__ == "__main__":
    Gui()
