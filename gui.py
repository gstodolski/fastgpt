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
        self.window.geometry("800x600")
        self.window.config(bg="#FAF9F6")

        # Navigation bar
        self.navigation = tk.Frame(self.window, bg="#4F62F8", height=40)
        self.navigation.pack(side="top", fill="x")
        # Logo
        self.label = tk.Label(self.navigation, text="smalltalk", fg="#FFFFFF", bg="#4F62F8", font=("Silom", 24, "bold"))
        self.label.pack(side="left", padx=40, pady=8)

        # Template input
        self.template_label = tk.Label(self.window, text="Template", font=("Menlo", 20, "bold"), anchor="w", fg="#081EC4", bg="#FAF9F6")
        self.template_label.pack(side="top", padx=40, pady=(32, 8), anchor="w")
        # Active template frame
        self.active_template_frame = tk.Frame(self.window, bg="#FAF9F6")
        self.active_template_frame.pack(side="top", fill="x", padx=40, pady=(0, 20))
        # Active template selector
        self.active_template_label = tk.Label(self.active_template_frame, text="Active template: ", font=("Arial", 16, "bold"), anchor="w", fg="#000000", bg="#FAF9F6")
        self.active_template_label.pack(side="left", anchor="w")
        self.active_template_text = tk.Button(self.active_template_frame, text=self.get_active_template(), command=self.open_template_window, bg="#FAF9F6", fg="#081EC4", font=("Arial", 16, "bold"), borderwidth=0, relief="flat")
        self.active_template_text.pack(side="left", anchor="w")

        # Content of active template
        self.template_box = tk.Text(self.window, bg="#FAF9F6", fg="#000000", font=("Arial", 16), wrap="word", height=4, highlightthickness=0)
        self.template_box.pack(side="top", fill="both", expand=True, padx=40, pady=(0, 8))
        self.template_box.insert("end", self.get_content())
        self.template_box.configure(state="disabled")
        # Submit button
        self.submit_button = tk.Button(self.window, text="Run ChatGPT", command=self.submit, fg="#176345", font=("Menlo", 16, "bold"), borderwidth=0, relief="flat", height=2, width=10, highlightcolor="#176345", highlightbackground="#176345")
        self.submit_button.pack(side="top", padx=40, pady=(0, 32), anchor="e")

        # Output window
        self.output_label = tk.Label(self.window, text="Output", font=("Menlo", 20, "bold"), anchor="w", fg="#081EC4", bg="#FAF9F6")
        self.output_label.pack(side="top", padx=40, pady=(24, 16), anchor="w")
        self.output_box = tk.Text(self.window, bg="#FAF9F6", fg="#000000", insertbackground="#000000", height=10, width=60, font=("Arial", 16))
        self.output_box.pack(side="bottom", fill="both", expand=True, padx=40, pady=(0, 32))

        self.window.mainloop()
    
    def open_template_window(self):
        """Open the template window"""
        self.template_window = tk.Toplevel(self.window)
        self.template_window.title("Templates")
        self.template_window.geometry("800x600")
        self.template_window.config(bg="#FAF9F6")
        list = tk.Variable(value=self.app.get_template_names())

        # Template listbox header
        self.template_label = tk.Label(self.template_window, text="Templates", font=("Menlo", 20, "bold"), anchor="w", fg="#081EC4", bg="#FAF9F6")
        self.template_label.pack(side="top", padx=40, pady=(32, 0), anchor="w")
        self.template_instructions = tk.Label(self.template_window, text="Click an existing template to use.", font=("Arial", 14), anchor="w", fg="#000000", bg="#FAF9F6")
        self.template_instructions.pack(side="top", padx=40, pady=(0, 8), anchor="w")
        # Template listbox
        self.template_list = tk.Listbox(self.template_window, listvariable=list, bg="#FAF9F6", fg="#000000", font=("Arial", 16), selectmode="single", border=2)
        self.template_list.pack(side="top", fill="both", expand=True, padx=40, pady=(0, 16))
        # Delete button
        self.template_button_frame = tk.Frame(self.template_window, bg="#FAF9F6")
        self.template_button_frame.pack(side="top", fill="x", padx=40, pady=(0, 16))
        self.delete_template_button = tk.Button(self.template_button_frame, text="Delete template", bg="#FAF9F6", fg="#081EC4", font=("Arial", 16, "bold"), borderwidth=0)
        self.delete_template_button.pack(side="left", anchor="w")

        # New template frame
        self.new_template_label = tk.Label(self.template_window, text="New template", font=("Menlo", 20, "bold"), anchor="w", fg="#081EC4", bg="#FAF9F6")
        self.new_template_label.pack(side="top", padx=40, pady=(8, 0), anchor="w")
        self.instructions_1 = tk.Label(self.template_window, text="Enter a title and content for your new template. For a string variable, type $var$ where var is the title.", font=("Arial", 14), anchor="w", fg="#000000", bg="#FAF9F6")
        self.instructions_1.pack(side="top", padx=40, pady=(2, 0), anchor="w")
        self.instructions_2 = tk.Label(self.template_window, text="For a number variable titled num, type #num#. For a date variable titled birthday, type *birthday*.", font=("Arial", 14), anchor="w", fg="#000000", bg="#FAF9F6")
        self.instructions_2.pack(side="top", padx=40, pady=(0, 4), anchor="w")
        # Form for new template
        self.title_label = tk.Label(self.template_window, text="Title", bg="#FAF9F6", fg="#000000", font=("Arial", 16, "bold"))
        self.title_label.pack(side="top", padx=40, anchor="w")
        self.new_template_title_box = tk.Entry(self.template_window, bg="#FAF9F6", fg="#000000", font=("Arial", 14), highlightthickness=2, relief="flat")
        self.new_template_title_box.pack(side="top", fill="x", expand=False, padx=40)
        self.content_label = tk.Label(self.template_window, text="Content", bg="#FAF9F6", fg="#000000", font=("Arial", 16, "bold"))
        self.content_label.pack(side="top", padx=40, anchor="w")
        self.new_template_content_box = tk.Entry(self.template_window, bg="#FAF9F6", fg="#000000", font=("Arial", 14), highlightthickness=2, relief="flat")
        self.new_template_content_box.pack(side="top", fill="both", expand=False, padx=40, pady=(0, 16))
        self.new_template_button = tk.Button(self.template_window, text="New template", command=self.new_template, bg="#FAF9F6", fg="#081EC4", font=("Arial", 16, "bold"), borderwidth=0)
        self.new_template_button.pack(side="left", padx=40, pady=(0, 16), anchor="w")

        self.template_list.bind("<<ListboxSelect>>", self.select_template)

        self.template_window.mainloop()
        self.window.mainloop()

    def get_content(self):
        """Get the content of the active template"""
        if self.active_template:
            return self.active_template.string
        return "Select an existing template or create a new one."
    
    def get_active_template(self):
        """Get the title of the active template"""
        if self.active_template:
            return self.active_template.title
        return "No template selected"
    
    def select_template(self, event):
        """Select a template"""
        selection = self.template_list.curselection()
        if selection:
            template = self.app.templates[selection[0]]
            self.active_template = template
            self.active_template_text.config(text=self.get_active_template())
            content = self.get_content()
            self.template_box.configure(state="normal")
            self.template_box.delete("1.0", "end")
            self.template_box.insert("end", content)
            self.display_content()
            self.template_box.configure(state="disabled")

    def new_template(self):
        """Create a new template"""
        title = self.new_template_title_box.get()
        content = self.new_template_content_box.get()
        self.app.add_template(title, content)
        self.template_list.insert(tk.END, title)
        self.new_template_title_box.delete(0, tk.END)
        self.new_template_content_box.delete(0, tk.END)

    def display_content(self):
        """Display the content of the active template"""
        if self.active_template:
            self.template_box.configure(state="normal")
            for var in self.active_template.get_variables():
                symbol = ""
                if var.type == "text":
                    symbol = "$"
                elif var.type == "number":
                    symbol = "#"
                elif var.type == "date":
                    symbol = "*"
                variable = symbol + var.name + symbol
                start = self.template_box.search(variable, "1.0", "end")
                # Display variables
                if var.value is not None and start == "":
                    continue
                elif var.value is None:
                    self.template_box.tag_add(variable, start, f"{start}+{len(variable)}c")
                    self.template_box.tag_config(variable, foreground="#FF5964", font=("Arial", 16, "bold"))
                    self.template_box.tag_bind(variable, "<Button-1>", self.edit_variable)
                else:
                    # Replace the variable with its value
                    end = f"{start}+{len(variable)}c"
                    self.template_box.delete(start, end)
                    self.template_box.insert(start, var.value)
                    start = self.template_box.search(var.value, "1.0", "end")
                    self.template_box.tag_add(variable, start, f"{start}+{len(var.value)}c")
                    self.template_box.tag_config(variable, foreground="#239567", font=("Arial", 16, "bold"))
                    self.template_box.tag_bind(variable, "<Button-1>", self.edit_variable)
            self.template_box.configure(state="disabled")
    
    def edit_variable(self, event):
        """Edit a variable"""
        tag = self.template_box.tag_names("current")[0]
        var = self.active_template.get_variable(tag[1:-1])
        if var.type == "text":
            self.edit_text_variable(var)
        elif var.type == "number":
            self.edit_number_variable(var)
        elif var.type == "date":
            self.edit_date_variable(var)

    def edit_text_variable(self, var):
        """Open a pop up window to edit a text variable"""
        self.text_window = tk.Toplevel(self.window)
        self.text_window.title("Edit variable")
        self.text_window.geometry("300x200")
        self.text_window.resizable(False, False)
        self.text_window.configure(bg="#FAF9F6")
        self.text_window.transient(self.window)

        self.text_label = tk.Label(self.text_window, text="Edit variable", bg="#FAF9F6", fg="#000000", font=("Arial", 16, "bold"))
        self.text_label.pack(side="top", padx=40, pady=(16, 0), anchor="w")
        self.text_instructions = tk.Label(self.text_window, text="Value of " + var.name + ":", font=("Arial", 14), anchor="w", fg="#000000", bg="#FAF9F6")
        self.text_instructions.pack(side="top", padx=40, pady=(2, 0), anchor="w")
        self.text_box = tk.Entry(self.text_window, bg="#FAF9F6", fg="#000000", font=("Arial", 14), highlightthickness=2, relief="flat")
        self.text_box.pack(side="top", fill="x", expand=False, padx=40, pady=(0, 4))
        self.text_button = tk.Button(self.text_window, text="Assign value", command=lambda: self.assign_value(var), bg="#FAF9F6", fg="#081EC4", font=("Arial", 16, "bold"), borderwidth=0)
        self.text_button.pack(side="left", padx=40, pady=(0, 16), anchor="w")

    def assign_value(self, var):
        """Assign a value to a variable"""
        value = self.text_box.get()
        var.set_value(value)
        self.display_content()
        self.text_window.destroy()

    def submit(self):
        """Submit the form"""
        response = self.active_template.execute_template()
        self.output_box.insert(tk.END, response)
    
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
