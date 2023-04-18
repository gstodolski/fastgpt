import tkinter as tk
from tkinter import ttk
from app import App
import pickle

class Gui:
    """Create a GUI for the application"""
    def __init__(self):
        self.app = App()
        self.active_template = None

        self.window = tk.Tk()
        self.window.title("smalltalk")
        self.window.geometry("750x500")
        self.window.config(bg="#FAF9F6")

        # Navigation bar
        self.navigation = tk.Frame(self.window, bg="#1E1E1E", height=40)
        self.navigation.pack(side="top", fill="x")
        # Logo
        self.label = tk.Label(self.navigation, text="smalltalk", fg="#FFFFFF", bg="#1E1E1E", font=("Silom", 24, "bold"))
        self.label.pack(side="left", padx=40, pady=8)

        # Template input
        self.template_label = tk.Label(self.window, text="Template", font=("Menlo", 20, "bold"), anchor="w", fg="navy", bg="#FAF9F6")
        self.template_label.pack(side="top", padx=40, pady=(32, 8), anchor="w")

        self.active_template_frame = tk.Frame(self.window, bg="#FAF9F6")
        self.active_template_frame.pack(side="top", fill="x", padx=40, pady=(0, 20))

        self.active_template_label = tk.Label(self.active_template_frame, text="Active template: ", font=("Arial", 16, "bold"), anchor="w", fg="navy", bg="#FAF9F6")
        self.active_template_label.pack(side="left", anchor="w")
        self.active_template_text = tk.Button(self.active_template_frame, text=self.get_active_template(), command=self.open_template_window, bg="#FAF9F6", fg="navy", font=("Arial", 16, "bold"), borderwidth=0)
        self.active_template_text.pack(side="left", anchor="w")

        self.template_box = tk.Label(self.window, bg="#FAF9F6", fg="#000000", font=("Arial", 18), anchor="nw")
        self.template_box.pack(side="top", fill="both", expand=True, padx=40, pady=(0, 16))
        self.template_box.config(text=self.get_content())

        # Output window
        self.output_label = tk.Label(self.window, text="Output", font=("Menlo", 20, "bold"), anchor="w", fg="navy", bg="#FAF9F6")
        self.output_label.pack(side="top", padx=40, pady=(24, 16), anchor="w")
        self.output_box = tk.Text(self.window, bg="#FAF9F6", fg="#000000", insertbackground="#000000", height=10, width=60, font=("Arial", 20))
        self.output_box.pack(side="bottom", fill="both", expand=True, padx=40, pady=(0, 32))

        self.window.mainloop()
    
    def open_template_window(self):
        """Open the template window"""
        self.template_window = tk.Toplevel(self.window)
        self.template_window.title("Templates")
        self.template_window.geometry("800x600")
        self.template_window.config(bg="#FAF9F6")

        self.template_label = tk.Label(self.template_window, text="Templates", font=("Menlo", 20, "bold"), anchor="w", fg="navy", bg="#FAF9F6")
        self.template_label.pack(side="top", padx=40, pady=(32, 8), anchor="w")

        self.template_list = tk.Listbox(self.template_window, bg="#FAF9F6", fg="#000000", font=("Arial", 18), selectmode="single")
        self.template_list.pack(side="top", fill="both", expand=True, padx=40, pady=(0, 16))

        self.template_button_frame = tk.Frame(self.template_window, bg="#FAF9F6")
        self.template_button_frame.pack(side="top", fill="x", padx=40, pady=(0, 16))

        self.new_template_button = tk.Button(self.template_button_frame, text="New template", bg="#FAF9F6", fg="navy", font=("Arial", 16, "bold"), borderwidth=0)
        self.new_template_button.pack(side="left", pady=(0, 16), anchor="w")
        self.delete_template_button = tk.Button(self.template_button_frame, text="Delete template", bg="#FAF9F6", fg="navy", font=("Arial", 16, "bold"), borderwidth=0)
        self.delete_template_button.pack(side="left", pady=(0, 16), anchor="w")

        self.template_window.mainloop()

    def get_content(self):
        """Get the content of the active template"""
        if self.active_template:
            return self.active_template.get_content()
        return "Content"
    
    def get_active_template(self):
        """Get the title of the active template"""
        if self.active_template:
            return self.active_template.title
        return "None"
    
    def save_app(self):
        """Save the application"""
        with open("app.pkl", "wb") as f:
            pickle.dump(self.app, f)

    def load_app(self):
        """Load the application"""
        with open("app.pkl", "rb") as f:
            self.app = pickle.load(f)

if __name__ == "__main__":
    Gui()
