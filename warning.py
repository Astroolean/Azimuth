import tkinter as tk
from PIL import Image, ImageTk
import colorsys
import time

class AzimuthApp:
    def __init__(self):
        self.Azimuth = tk.Tk()
        self.color_cycle = ['#FF0000', '#00FF00', '#0000FF']
        self.text_label = tk.Label(self.Azimuth, text="Hello, World!", font=("Pixel Calculon", 18))
        self.text_label.pack(pady=30, padx=10, fill="both", expand=True)

        self.Azimuth.after(1, self.update_text_color)
        self.Azimuth.mainloop()

    def update_text_color(self):
        current_time = time.time()
        wave_speed = 1.0

        text = self.text_label.cget("text")
        wave_length = len(text)

        if wave_length == 0:
            return

        for i, char in enumerate(text):
            letter_time = current_time - (i / wave_length) * wave_speed
            current_index = int(letter_time * 2) % len(self.color_cycle)
            color = self.interpolate_color(self.color_cycle[current_index], self.color_cycle[(current_index + 1) % len(self.color_cycle)])

            char_index = f"{i + 1}.0"  # Tkinter indices start from 1, not 0
            self.text_label.configure(fg=color)
            self.text_label.tag_configure("color", foreground=color)
            self.text_label.tag_add("color", char_index)

        self.Azimuth.after(100, self.update_text_color)

    def interpolate_color(self, start_color, end_color):
        start_rgb = [int(start_color[i:i+2], 16) for i in (1, 3, 5)]
        end_rgb = [int(end_color[i:i+2], 16) for i in (1, 3, 5)]

        current_rgb = [
            int(start + (end - start) / 2) for start, end in zip(start_rgb, end_rgb)
        ]

        current_color = "#{:02X}{:02X}{:02X}".format(*current_rgb)
        return current_color

if __name__ == "__main__":
    app = AzimuthApp()