import tkinter as tk

def show_coordinates(event):
    x, y = event.x_root, event.y_root
    coords_label.config(text=f"X: {x}, Y: {y}")

# Create the main window
root = tk.Tk()
root.title("Mouse Coordinates")

# Create a label to display the coordinates
coords_label = tk.Label(root, text="Move the mouse to see coordinates", font=("Helvetica", 16), bg="black", fg="white")
coords_label.place(relx=0.01, rely=0.95, anchor='sw')  # Bottom-left corner

# Bind the mouse movement event to the function
root.bind('<Motion>', show_coordinates)

# Run the Tkinter event loop
root.mainloop()
