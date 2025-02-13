import os
import ctypes
import json
from tkinter import Tk, Label, Button, filedialog, colorchooser

class QuantumGuard:
    def __init__(self, root):
        self.root = root
        self.root.title("QuantumGuard - Custom Themes and Visual Styles")
        self.theme_data = {}

        self.label = Label(root, text="QuantumGuard - Customize Your Windows Theme", font=("Arial", 16))
        self.label.pack(pady=10)

        self.load_button = Button(root, text="Load Theme", command=self.load_theme)
        self.load_button.pack(pady=5)

        self.save_button = Button(root, text="Save Theme", command=self.save_theme)
        self.save_button.pack(pady=5)

        self.apply_button = Button(root, text="Apply Theme", command=self.apply_theme)
        self.apply_button.pack(pady=5)

        self.color_button = Button(root, text="Choose Background Color", command=self.choose_color)
        self.color_button.pack(pady=5)

    def load_theme(self):
        theme_file = filedialog.askopenfilename(title="Select Theme File", filetypes=[("JSON Files", "*.json")])
        if theme_file:
            with open(theme_file, 'r') as file:
                self.theme_data = json.load(file)
            self.apply_theme()

    def save_theme(self):
        theme_file = filedialog.asksaveasfilename(title="Save Theme File", defaultextension=".json", filetypes=[("JSON Files", "*.json")])
        if theme_file:
            with open(theme_file, 'w') as file:
                json.dump(self.theme_data, file, indent=4)

    def apply_theme(self):
        if "bg_color" in self.theme_data:
            bg_color = self.theme_data["bg_color"]
            self.set_background_color(bg_color)

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Choose Background Color")[1]
        if color_code:
            self.theme_data["bg_color"] = color_code
            self.set_background_color(color_code)

    def set_background_color(self, color):
        try:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, color, 0)
            self.label.config(text=f"Background Color Set to: {color}")
        except Exception as e:
            self.label.config(text=f"Failed to set color: {str(e)}")

if __name__ == "__main__":
    root = Tk()
    app = QuantumGuard(root)
    root.mainloop()