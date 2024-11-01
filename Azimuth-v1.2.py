from itertools import cycle
import sqlite3
import tkinter as tk
import customtkinter
from PIL import Image, ImageTk, ImageSequence
import time
import warnings
from math import cos, pi
from tkinter import Canvas, Label
import random
import os




warnings.filterwarnings("ignore", category=UserWarning, module="customtkinter")
warnings.filterwarnings("ignore", category=UserWarning, module="PIL")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


CREATOR_NOTE = '''
⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏   ⏏

    Created by: Astroolean
    Released: 11/01/2024
    Version: 1.2
    Latest update: 11/01/2024


Disclaimer for the program Azimuth

The Azimuth program ("Azimuth") is provided as a free tool for educational and experimental purposes only. 
The developer of Azimuth makes no warranty, express or implied, and hereby disclaim and negate all other 
warranty including, without limitation, implied warranty or conditions of merchantability, fitness for a 
particular purpose, or non-infringement of intellectual property or other violation of rights.

The use of Azimuth is solely at the user's own risk. Under no circumstances shall the developer or contributors 
of Azimuth be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, 
but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) 
however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or 
otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.

This disclaimer of liability applies to any damages or injury, caused by any failure of performance, error, omission, 
interruption, deletion, defect, delay in operation or transmission, computer virus, communication line failure, theft 
or destruction or unauthorized access to, alteration of, or use of record, whether for breach of contract, tortious 
behavior, negligence, or under any other cause of action.

The developer of Azimuth does not condone or endorse any illegal activities that might be conducted using this software. 
The responsibility for ensuring compliance with local laws and regulations lies solely with the user. The developer will 
not be held responsible for any unlawful or unauthorized use of Azimuth.

By using Azimuth, users acknowledge and agree to this disclaimer. If you do not agree with these terms and conditions, you 
should refrain from using Azimuth. Goodbye and please have a wonderful day!


class AstrooleanSignature:
    def __init__(self, NAME="Astroolean"):
        self.NAME = NAME
    def signature(self):
        Astro = "Astro - The online name ive always went by."
        Boolean = "Boolean - Embracing the simplicity of true/false."
        return f"{"self.NAME"} Signature:\\n{Astro}\\n{Boolean}\\nAll-in-all its just Astroolean."
Astroolean = AstrooleanSignature()
print(Astroolean.signature())
'''

class AzimuthApp():
    def __init__(self):
        #self.CUSTOM_LOADING = LoadingScreen()
        self.AZIMUTH = customtkinter.CTk()
        self.BUTTON_COLOR = ["#ff0000", "#00ff00", "#0000ff", "#ffff00", "#ff00ff", "#00ffff"]
        self.USERNAME_COLOR = ["#ffffff", "#000000", "#333333", "#666666", "#999999", "#cccccc"]
        self.CURRENT_TAB = None
        self.PROGRAMS = []
        print(f"{CREATOR_NOTE}")  
        self.gif_path = os.path.join(os.path.dirname(__file__), "Logo", "Azimuth Logo.gif")
        self.target_size = (335, 335)  # Define your target width and height here
        self.AzimuthGUI()

    def PlayGif(self):
        self.gif_image = Image.open(self.gif_path)

        # Resize each frame to make the logo slightly bigger
        self.target_size = (self.target_size[0] + 10, self.target_size[1])  # Increase the width and height by 20 pixels
        self.gif_frames = []
        for frame in ImageSequence.Iterator(self.gif_image):
            resized_frame = frame.resize(self.target_size, Image.Resampling.LANCZOS)
            self.gif_frames.append(ImageTk.PhotoImage(resized_frame))

        self.gif_frame_index = 0
        self.gif_delay = self.gif_image.info.get('duration', 10)

        # Add a Label to display the GIF
        self.gif_label = customtkinter.CTkLabel(self.AZIMUTH, text="")
        self.gif_label.place(x=10, y=455)

        self.PauseAnimations()
        self.UpdateGifFrame()

    def UpdateGifFrame(self):
        self.gif_label.configure(image=self.gif_frames[self.gif_frame_index])
        self.gif_frame_index = (self.gif_frame_index + 1) % len(self.gif_frames)
    
        if self.gif_frame_index == 0:
            # If the GIF has finished playing, resume other animations
            self.ResumeAnimations()

        # Continue updating the GIF frames
        self.AZIMUTH.after(self.gif_delay, self.UpdateGifFrame)

    def PauseAnimations(self):
        """Pauses other animations while GIF is playing."""
        # Cancel ongoing color cycling or animations by pausing them
        self.AZIMUTH.after_cancel(self.color_cycle_after_id)
        # Optionally, set a flag if needed to indicate paused state

    def ResumeAnimations(self):
        """Resumes animations after GIF playback or when necessary."""
        # Restart the color cycling or animations
        self.color_cycle_after_id = self.AZIMUTH.after(150, self.ArrowButtonColorCycle)
        # Reset flag if necessary

    def UpdateLog(self):
        # Create a transparent frame for the update log text and lock its size
        self.update_log_frame = customtkinter.CTkCanvas(self.AZIMUTH, width=380, height=585, background="Blue")
        self.update_log_frame.place(x=355, y=10)

        UP = ("Pixel Calculon", 18)
        DOWN = ("Pixel Calculon", 12)

        # Define the pages of the update log, including version and updated date
        pages = [
            {
                "version": " VERSION:  1.0",
                "updated": " UPDATED:  1/26/2024",
                "content": """
➤ Added an update log to view 
   recent updates and fixes. 
   Giving a way to see all 
   progress made along the way.

➤ Fixed the buttons that were
   in each of the tab windows.
   Now they are working correct
   as intended.

➤ Fixed the issue where the
   UpdateLog is still seen via
   going into each tab window.

➤ Added a creator note to 
   include signature and ToS.
   As well as a few more 
   watermarks and such.

➤ Tuned a bit to account for
   lag and instability as well
   as a further precaution.
"""
            },
            {
                "version": " VERSION:  1.1",
                "updated": " UPDATED:  8/14/2024",
                "content": """
➤ Improved the update log 
   via design and usability. 
   Massive improvements.

➤ Fixed an issue where when
   you swap between tab 
   buttons quickly it will 
   glitch out the update log.

➤ Made it so the update log 
   always shows the latest 
   update log.

➤ Implemented an are you sure
   question upon closing the 
   application via the logout
   button. 

➤ Repurposed an old icon I had
   for this project. Simple 
   clean and straightforward 
   logo.
"""
            },
            {
                "version": " VERSION:  1.2",
                "updated": " UPDATED:  11/01/2024",
                "content": """
➤ Completely reworked every 
   single button. Massive
   overall improvement.

➤ ...

➤ ...

➤ ...

➤ ...
"""
            }
        ]

        # Initialize the current page index to the most recent page
        self.current_page = len(pages) - 1  # This will set it to the last page (most recent)

        # Calculate wraplength based on the frame width, slightly reduced to fit within margins
        wrap_length = self.update_log_frame.winfo_width() - 30  # Added padding to avoid text cutoff

        # Labels for version and update text
        self.update_log_image_label = customtkinter.CTkLabel(self.update_log_frame, text="", font=UP, text_color="white")
        self.update_log_image_label.place(x=15, y=7.5)  # Adjusted placement

        # Label for the content text with a fixed height
        self.update_log_text = customtkinter.CTkLabel(self.update_log_frame, 
                                                      text="", 
                                                      font=DOWN, 
                                                      wraplength=wrap_length, 
                                                      anchor="w", 
                                                      justify="left", 
                                                      padx=5,  # Add small horizontal padding
                                                      pady=5,  # Add small vertical padding
                                                      text_color="white",
                                                      height=180)  # Set a fixed height for the label
        self.update_log_text.place(x=15, y=50)  # Adjusted placement

        # Function to update the label text based on the current page
        def update_label_text():
            current_page_data = pages[self.current_page]
            version_text = f"{current_page_data['version']}\n{current_page_data['updated']}"
            self.update_log_image_label.configure(text=version_text)
            self.update_log_text.configure(text=current_page_data['content'])

        # Functions to handle page navigation
        def go_back():
            if self.current_page > 0:
                self.current_page -= 1
                update_label_text()

        def go_forward():
            if self.current_page < len(pages) - 1:
                self.current_page += 1
                update_label_text()

        # Create forward and back buttons
        button_width = 100  # Adjust this as necessary
        self.button_frame = customtkinter.CTkFrame(self.update_log_frame, fg_color="transparent")
        self.button_frame.place(relx=0.5, rely=1.0, anchor='s', y=-10)  # Centered

        self.back_button = customtkinter.CTkButton(self.button_frame, text="◄", command=go_back, width=button_width)
        self.back_button.pack(side="left", padx=5)

        # Create a canvas for displaying the current page number
        self.page_display_canvas = customtkinter.CTkCanvas(self.button_frame, width=45, height=30, background="Blue")
        self.page_display_canvas.pack(side="left", padx=5)
        self.page_display_text = self.page_display_canvas.create_text(25, 15, text=str(self.current_page + 1), font=UP, fill="Blue")

        self.forward_button = customtkinter.CTkButton(self.button_frame, text="►", command=go_forward, width=button_width)
        self.forward_button.pack(side="left", padx=5)

        # Start the color-cycling for the buttons
        self.ArrowButtonColorCycle()

        # Display the initial page
        update_label_text()

    def ArrowButtonColorCycle(self):
        CURRENT_TIME = time.time()
        WAVE_SPEED = 64  
        CURRENT_INDEX = int(CURRENT_TIME * WAVE_SPEED * 8) % len(self.BUTTON_COLOR)
        BUTTON = self.BUTTON_COLOR[CURRENT_INDEX]
        TEXT_COLOR = self.USERNAME_COLOR[CURRENT_INDEX]

        self.back_button.configure(
            fg_color=BUTTON,
            text_color=TEXT_COLOR,
            border_width=1,
            corner_radius=1,
            border_spacing=1,
            hover=True
        )
        self.forward_button.configure(
            fg_color=BUTTON,
            text_color=TEXT_COLOR,
            border_width=1,
            corner_radius=1,
            border_spacing=1,
            hover=True
        )

        # Update the page display canvas background and text color
        self.page_display_canvas.configure(background=BUTTON)
        self.page_display_canvas.itemconfig(self.page_display_text, fill=TEXT_COLOR, text=str(self.current_page + 1))

        # Store the after_id to pause the animation if needed
        self.color_cycle_after_id = self.AZIMUTH.after(150, self.ArrowButtonColorCycle)

    def CustomInfo(self, TITLE, MESSAGE, ASH):
        INFO = customtkinter.CTkToplevel()
        INFO.title(TITLE)
        INFO.overrideredirect(True)
    
        # Set the constants for the popup size and button dimensions
        AVAILABLE_WIDTH = 600  # Fixed width to match ShowConfirmation
        WINDOW_HEIGHT = 150    # Fixed height to match ShowConfirmation
    
        # Calculate the position for the popup at the bottom-right corner
        RIGHT_EDGE_WINDOW_X = self.AZIMUTH.winfo_width()
        RIGHT_EDGE_WINDOW_Y = self.AZIMUTH.winfo_height()
        Y_POSITION = RIGHT_EDGE_WINDOW_Y - WINDOW_HEIGHT - 15  # Same Y position calculation as ShowConfirmation
        X_POSITION = RIGHT_EDGE_WINDOW_X - AVAILABLE_WIDTH - 5   # Same X position calculation as ShowConfirmation
    
        # Set the geometry of the popup
        INFO.geometry(f"{AVAILABLE_WIDTH}x{WINDOW_HEIGHT}+{X_POSITION}+{Y_POSITION}")
    
        # Ensure the main window stays on top after a short delay
        self.AZIMUTH.after(150)
    
        # Create the canvas for the popup
        self.INFO_CUSTOM = customtkinter.CTkCanvas(INFO, width=AVAILABLE_WIDTH, height=WINDOW_HEIGHT)
        self.INFO_CUSTOM.pack(expand=True, fill="both")
    
        # Initialize the background of the popup
        self.InitializeBackground(self.INFO_CUSTOM)
    
        # Add the message text to the canvas, centered horizontally
        self.INFO_TEXT_ID = self.INFO_CUSTOM.create_text(
            AVAILABLE_WIDTH // 2, 
            30,  # Adjusted Y position to leave space for buttons
            text=MESSAGE, 
            font=self.FONT, 
            anchor="center"
        )
    
        # Calculate button positions
        button_width = 125
        button_spacing = 20  # Adjusted spacing between buttons
        total_button_width = button_width
    
        ok_button_x = (AVAILABLE_WIDTH - total_button_width) // 2
    
        # Create OK button
        self.INFO_BUTTON = customtkinter.CTkCanvas(self.INFO_CUSTOM, width=button_width, height=50, highlightthickness=0)
        self.INFO_BUTTON.place(x=ok_button_x, y=WINDOW_HEIGHT - 75)
        ok_button_bg_image = Image.open("background2.jpg").resize((button_width, 50))
        ok_button_bg_photo = ImageTk.PhotoImage(ok_button_bg_image)
        self.INFO_BUTTON.create_image(0, 0, image=ok_button_bg_photo, anchor="nw")
        self.INFO_BUTTON.create_text(button_width // 2, 25, text="OK", fill="white", font=("Pixel Calculon", 16))
        self.INFO_BUTTON.bind("<Button-1>", lambda event: self.CloseGUI(INFO))
        self.INFO_BUTTON.image = ok_button_bg_photo
    
        # Start the color cycling for the button
        self.BUTTON_COLOR = self.InfoCycle()
    
        # Set a flag indicating that the info popup is open
        self.INFO_OPEN = True
    
        # Start the color cycling effect for the text
        self.InfoColor()
    
        # Update the text color dynamically
        self.UpdateInfoTextColor(self.INFO_CUSTOM)
        
    def InitializeBackground(self, INITIALIZE):
        AZIMUTH_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        IMAGE_PATH = os.path.join(AZIMUTH_DIRECTORY, 'Background2.jpg')
        IMAGE = Image.open(IMAGE_PATH)
        CUSTOM_BACKGROUND_IMAGE = ImageTk.PhotoImage(IMAGE)
        INITIALIZE.create_image(0, 0, 
                             image=CUSTOM_BACKGROUND_IMAGE, 
                             anchor="nw")
        INITIALIZE.image = CUSTOM_BACKGROUND_IMAGE 

    def UpdateInfoTextColor(self, frame):
        CURRENT_TIME = time.time()
        WAVE_SPEED = 64
        CURRENT_INDEX = int(CURRENT_TIME * WAVE_SPEED * 8) % len(self.USERNAME_COLOR)
        COLOR = self.USERNAME_COLOR[CURRENT_INDEX]
        
        # Update the text color of the confirmation message
        frame.itemconfigure(self.INFO_TEXT_ID, fill=COLOR)
        frame.after(150, lambda: self.UpdateInfoTextColor(frame))

    def InfoColor(self):
        if hasattr(self, 'INFO_BUTTON') and self.INFO_BUTTON.winfo_exists():
            try:
                CURRENT_TIME = time.time()
                WAVE_SPEED = 64  
                CURRENT_INDEX = int(CURRENT_TIME * WAVE_SPEED * 8) % len(self.BUTTON_COLOR)
                BUTTON = self.BUTTON_COLOR[CURRENT_INDEX]
                TEXT_COLOR = self.USERNAME_COLOR[CURRENT_INDEX]

                self.INFO_BUTTON.configure(
                    fg_color=BUTTON,
                    text_color=TEXT_COLOR,
                    border_width=1,
                    corner_radius=1,
                    border_spacing=1,
                    hover=True
                )
                self.AZIMUTH.after(150, self.InfoColor)
            except tk.TclError as e:
                print(f"TclError in InfoColor: {e}")
        else:
            for after_id in self.AFTER:
                self.AZIMUTH.after_cancel(after_id)
            self.AFTER.clear()

    def InfoCycle(self, num_colors=1000):
        COLORS = [
            "#{:02x}{:02x}{:02x}".format(
                int(1 + 1 * cos(2 * pi * i / num_colors + 1 / 3)), 
                int(1 + 1 * cos(2 * pi * i / num_colors + 2 * pi / 3)), 
                int(128 + 127 * cos(2 * pi * i / num_colors + 4 * pi / 3)), 
            )
            for i in range(num_colors)
        ]
        return COLORS

    def CloseGUI(self, popup):
        try:
            if popup.winfo_exists():
                popup.destroy()
        except tk.TclError as e:
            print(f"TclError: {e}")

    def TabButtons(self, text, index, x, y):
        # Increase the width of the button
        button_width = 200  # Adjust this value as needed

        # Create a canvas for the button background with the new width
        button_canvas = customtkinter.CTkCanvas(self.AZIMUTH, width=button_width, height=50, highlightthickness=0)
        button_canvas.place(x=x, y=y)

        # Load and place the background image on the canvas separately for each button
        button_bg_image = Image.open("background2.jpg").resize((button_width, 50))  # Update with correct dimensions
        button_bg_photo = ImageTk.PhotoImage(button_bg_image)

        # Create a new image for each button to avoid reusing the same object
        button_canvas.create_image(0, 0, image=button_bg_photo, anchor="nw")

        # Add text to the canvas, centered and initially white
        text_id = button_canvas.create_text(button_width // 2, 25, text=text, fill="white", font=("Pixel Calculon", 16))

        # Handle button clicks manually
        button_canvas.bind("<Button-1>", lambda event: self.ToggleTab(index))

        # Keep reference to the image to avoid garbage collection
        button_canvas.image = button_bg_photo

        # Start cycling text color
        self.TabTextColor(button_canvas, text_id)

        return button_canvas

    def VerticalTabs(self):
        AZIMUTH_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        BACKGROUND_PATH = os.path.join(AZIMUTH_DIRECTORY, 
                                       'LoadingUI', 
                                       'Loading.jpg')
        CUSTOM_BACKGROUND = Image.open(BACKGROUND_PATH)
        CUSTOM_BACKGROUND = ImageTk.PhotoImage(CUSTOM_BACKGROUND) 
        self.TAB_CONTENT = customtkinter.CTkFrame(self.AZIMUTH)
        self.TAB_CONTENT.pack(side='left', 
                              expand=True, 
                              fill='both')
        self.TAB_CONTENT.pack_forget()
        self.TABS = []

        # Create each button separately with unique text and position
        buttons = [
            {"text": "Button 1", "y_pos": 10},
            {"text": "Button 2", "y_pos": 69},
            {"text": "Button 3", "y_pos": 128},
            {"text": "Button 4", "y_pos": 187},
            {"text": "Button 5", "y_pos": 246},
            {"text": "Button 6", "y_pos": 305},
            {"text": "Button 7", "y_pos": 364},
            {"text": "Button 8", "y_pos": 423},
            {"text": "Button 9", "y_pos": 482},
            {"text": "Button 10", "y_pos": 541},
        ]

        for i, button in enumerate(buttons):
            X = 770
            Y = button["y_pos"]  # Use predefined Y positions for each button
            HOT_FIX = self.TabButtons(button["text"], i, X, Y)  # Create each button with its own label
            self.TABS.append(HOT_FIX)
            content = TabContent(self.TAB_CONTENT, i)
            self.PROGRAMS.append(content)

    def TabTextColor(self, canvas, text_id):
        CURRENT_TIME = time.time()
        WAVE_SPEED = 64
        CURRENT_INDEX = int(CURRENT_TIME * WAVE_SPEED * 8) % len(self.USERNAME_COLOR)
        COLOR = self.USERNAME_COLOR[CURRENT_INDEX]
        
        # Update text color dynamically
        canvas.itemconfigure(text_id, fill=COLOR)
        
        # Continue cycling
        self.AZIMUTH.after(150, lambda: self.TabTextColor(canvas, text_id))

    def ToggleTab(self, index):
        if self.CURRENT_TAB == index:
            # Hide the tab content and show the update log
            self.PROGRAMS[index].tab_content_frame.place_forget()
            self.TAB_CONTENT.pack_forget()
            self.update_log_frame.place(x=355, y=10)  # Show the update log frame
            self.CURRENT_TAB = None
        else:
            # Show the tab content and hide the update log
            self.TAB_CONTENT.pack(side='left', expand=True, fill='both')
            self.update_log_frame.place_forget()  # Hide the update log frame
            for tab_content in self.PROGRAMS:
                tab_content.tab_content_frame.place_forget()
            self.PROGRAMS[index].ShowContent()
            self.CURRENT_TAB = index

    def AzimuthGUI(self):
        APP_BACKGROUND = Image.open("Primary.jpg")
        APP_BACKGROUND = ImageTk.PhotoImage(APP_BACKGROUND)
        BACKGROUND_LABEL = customtkinter.CTkLabel(self.AZIMUTH, image=APP_BACKGROUND)
        BACKGROUND_LABEL.place(relwidth=1, relheight=1)
        self.FONT = ("Pixel Calculon", 18)
        self.USERNAME_COLOR = self.EntryCycle()
        self.BUTTON_COLOR = self.ButtonCycle()
        self.APP = customtkinter.CTkCanvas(self.AZIMUTH, width=800, height=600)
        self.CURRENT_USERNAME = self.APP
        self.CURRENT_USERNAME.place(relwidth=1, relheight=1)
        self.CURRENT_USERNAME.create_image(0, 0, anchor="nw", image=APP_BACKGROUND)
        self.CURRENT_USERNAME.create_text(0, 0, text="", font=self.FONT)
        self.AZIMUTH.overrideredirect(True)
        self.AZIMUTH.resizable(False, False)
        self.AFTER = []
        self.CANVAS = None
        self.TAB_CONTENT = None
        self.TABS = []
        self.CURRENT_TAB = None
        self.PROGRAMS = []
        self.CenterGUI()
        self.UpdateLog()
        self.UserPassEntry()
        self.UserButtons()
        self.ActiveUser()
        self.ButtonBind()
        self.EntryColor()
        self.VerticalTabs()
        self.ArrowButtonColorCycle()
        # Start the GIF playback
        self.PlayGif()

    def AzimuthIcon(self, gif_path):
        ICON_IMAGE = Image.open(gif_path)
        ICON_IMAGE = ImageTk.PhotoImage(ICON_IMAGE)
        self.AZIMUTH.tk.call('wm', 
                             'iconphoto', 
                             self.AZIMUTH._w, 
                             ICON_IMAGE)

    def CenterGUI(self):
        SCREEN_WIDTH = 1920
        SCREEN_HEIGHT = 1080
        WINDOW_WIDTH = 990
        WINDOW_HEIGHT = 800
        X = (SCREEN_WIDTH - WINDOW_WIDTH) // 48
        Y = (SCREEN_HEIGHT - WINDOW_HEIGHT) // 24

        self.AZIMUTH.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{X}+{Y}")

    def EntryColor(self):
        CURRENT_TIME = time.time()
        WAVE_SPEED = 64 
        CURRENT_INDEX = int(CURRENT_TIME * WAVE_SPEED * 8) % len(self.USERNAME_COLOR)
        COLOR = self.USERNAME_COLOR[CURRENT_INDEX]
        self.UserEntry.configure(placeholder_text_color=COLOR,
                                 border_color=COLOR,
                                 text_color=COLOR,
                                 bg_color="transparent")
        self.PassEntry.configure(placeholder_text_color=COLOR,
                                 border_color=COLOR,
                                 text_color=COLOR,
                                 bg_color="transparent")
        self.AZIMUTH.after(150, self.EntryColor)

    def EntryCycle(self, num_colors=1000):
        COLORS = [
            "#{:02x}{:02x}{:02x}".format(
                int(96 + 16 * cos(2 * pi * i / num_colors + 1 / 3)), 
                int(128 + 127 * cos(2 * pi * i / num_colors + 2 * pi / 3)), 
                int(128 + 127 * cos(2 * pi * i / num_colors + 4 * pi / 3)), 
            )
            for i in range(num_colors)
        ]
        return COLORS

    def ButtonCycle(self, num_colors=1000):
        COLORS = [
            "#{:02x}{:02x}{:02x}".format(
                int(1 + 1 * cos(2 * pi * i / num_colors + 1 / 3)), 
                int(1 + 1 * cos(2 * pi * i / num_colors + 2 * pi / 3)), 
                int(128 + 127 * cos(2 * pi * i / num_colors + 4 * pi / 3)), 
            )
            for i in range(num_colors)
        ]
        return COLORS

    def ActiveUser(self):
        self.CURRENT_USERNAME_ID = self.APP.create_text(175, 
                                                        155, 
                                                        text="", 
                                                        fill="white") 

    def UsernameCycle(self):
        FONT = ("Pixel Calculon", 25)
        CURRENT_TIME = time.time()
        WAVE_SPEED = 64 
        CURRENT_INDEX = int(CURRENT_TIME * WAVE_SPEED * 8) % len(self.USERNAME_COLOR)
        COLOR = self.USERNAME_COLOR[CURRENT_INDEX]
        USERNAME = self.APP.itemcget(self.CURRENT_USERNAME_ID, 
                                     'text')
        if not USERNAME:
            return
        self.APP.itemconfigure(self.CURRENT_USERNAME_ID, 
                               text=USERNAME,
                               font=FONT, 
                               fill=COLOR)
        self.AZIMUTH.after(150, self.UsernameCycle)  

    def UserPassEntry(self):
        FONT = ("Pixel Calculon", 24)
        X_USER = 12.5  
        Y_USER = 12.5  
        X_PASS = 12.5  
        Y_PASS = 62.5  
        self.UserEntry = customtkinter.CTkEntry(master=self.AZIMUTH, 
                                                placeholder_text="U s e r n a m e", 
                                                width=262.5, 
                                                height=40, 
                                                font=FONT)
        self.UserEntry.place(x=X_USER, y=Y_USER)
        self.PassEntry = customtkinter.CTkEntry(master=self.AZIMUTH, 
                                                placeholder_text="P a s s w o r d", 
                                                show="*", 
                                                width=262.5, 
                                                height=40, 
                                                font=FONT)
        self.PassEntry.place(x=X_PASS, y=Y_PASS)

    def UserButtons(self):
        # Define button width and height
        button_width = 330
        button_height = 50

        # Define button positions to align them like before
        button_positions = [
            {"text": "A c c e s s", "y_pos": 190},
            {"text": "L o g o u t", "y_pos": 245},
            {"text": "C r e a t e", "y_pos": 300},
            {"text": "D e l e t e", "y_pos": 355},
        ]

        for button in button_positions:
            # Create a canvas for each button with dynamic text color
            button_canvas = customtkinter.CTkCanvas(self.AZIMUTH, width=button_width, height=button_height, highlightthickness=0)
            button_canvas.place(x=15, y=button["y_pos"])

            # Load and place the background image on the canvas
            button_bg_image = Image.open("background2.jpg").resize((button_width, button_height))
            button_bg_photo = ImageTk.PhotoImage(button_bg_image)
            button_canvas.create_image(0, 0, image=button_bg_photo, anchor="nw")

            # Add text to the canvas, centered
            button_text_id = button_canvas.create_text(button_width // 2, button_height // 2 + 5, text=button["text"], fill="white", font=("Pixel Calculon", 18))

            # Bind the appropriate command for each button
            if button["text"] == "A c c e s s":
                button_canvas.bind("<Button-1>", lambda event: self.LoginAccount())
            elif button["text"] == "L o g o u t":
                button_canvas.bind("<Button-1>", lambda event: self.LogoutAccount())
            elif button["text"] == "C r e a t e":
                button_canvas.bind("<Button-1>", lambda event: self.RegisterAccount())
            elif button["text"] == "D e l e t e":
                button_canvas.bind("<Button-1>", lambda event: self.DeleteAccount())

            # Keep reference to the image to avoid garbage collection
            button_canvas.image = button_bg_photo

            # Start the color cycling for the text
            self.TabTextColor(button_canvas, button_text_id)

    def LoginAction(self):
        self.LoginAccount()

    def LogoutAction(self):
        self.LogoutAccount()

    def RegisterAction(self):
        self.RegisterAccount()

    def DeleteAction(self):
        self.DeleteAccount()

    def ButtonBind(self):
        self.AZIMUTH.bind('<Return>', lambda event: self.LoginAction())
        self.AZIMUTH.bind('<Escape>', lambda event: self.LogoutAction())

    def LoginAccount(self):
        CURRENT_USER = self.APP.itemcget(self.CURRENT_USERNAME_ID, 'text')
        try:
            if CURRENT_USER:
                self.CustomInfo("Failure!", f"   Logged in as {CURRENT_USER}...", self.FONT)
            else:
                DATABASE = sqlite3.connect("main.db")
                LOOKUP = DATABASE.cursor()
                LOOKUP.execute('SELECT * FROM user WHERE username=? AND password=?', (self.UserEntry.get(), self.PassEntry.get()))
                USER = LOOKUP.fetchone()
                DATABASE.close()
                if USER:
                    USERNAME = self.UserEntry.get()
                
                    self.CustomInfo("Success!", "   Welcome to Azimuth V1.2 \n   Created by: Astroolean", self.FONT)
                    self.logged_text = f"{USERNAME}"
                    self.APP.itemconfigure(self.CURRENT_USERNAME_ID, text=self.logged_text, font=self.FONT)
                    self.UsernameCycle() 
                else:
                    self.CustomInfo("Failure!", "   Invalid username/password...", self.FONT)
        except Exception as e:
            print(f"Error during login: {e}")
                
    def LogoutAccount(self):
        CURRENT_USER = self.APP.itemcget(self.CURRENT_USERNAME_ID, 'text')
    
        if CURRENT_USER:  # If a user is logged in
            self.APP.itemconfigure(self.CURRENT_USERNAME_ID, text="", font=self.FONT)
            self.UserEntry.delete(0, tk.END)
            self.PassEntry.delete(0, tk.END)
            self.CustomInfo("Logged Out", "   Successfully logged out...", self.FONT)
        else:  # If no user is logged in, show the confirmation dialog
            self.ShowConfirmation("Exit Application", "   Are you sure you want to exit?")

    def ShowConfirmation(self, TITLE, MESSAGE):
        def on_confirm():
            self.AZIMUTH.destroy()  # Close the application

        def on_cancel():
            confirmation_popup.destroy()  # Close the confirmation dialog

        confirmation_popup = customtkinter.CTkToplevel()
        confirmation_popup.title(TITLE)
        confirmation_popup.overrideredirect(True)

        # Adjust these values to change the popup size
        AVAILABLE_WIDTH = 600  # Example fixed width, adjust as necessary
        WINDOW_HEIGHT = 150    # Example fixed height, adjust as necessary

        # Calculate the position for the popup
        RIGHT_EDGE_WINDOW_X = self.AZIMUTH.winfo_width()
        RIGHT_EDGE_WINDOW_Y = self.AZIMUTH.winfo_height()
        Y_POSITION = RIGHT_EDGE_WINDOW_Y - WINDOW_HEIGHT - 15
        X_POSITION = RIGHT_EDGE_WINDOW_X - AVAILABLE_WIDTH - 5

        # Set the geometry of the popup
        confirmation_popup.geometry(f"{AVAILABLE_WIDTH}x{WINDOW_HEIGHT}+{X_POSITION}+{Y_POSITION}")
        confirmation_popup.attributes('-topmost', True)
        self.AZIMUTH.after(150)

        # Create the canvas for the popup
        confirmation_frame = customtkinter.CTkCanvas(confirmation_popup, width=AVAILABLE_WIDTH, height=WINDOW_HEIGHT)
        confirmation_frame.pack(expand=True, fill="both")

        # Initialize the background of the popup
        self.InitializeBackground(confirmation_frame)

        # Create the text for the confirmation message and store the text ID
        self.INFO_TEXT_ID = confirmation_frame.create_text(
            AVAILABLE_WIDTH // 2, 
            30,  # Adjusted Y position to leave space for buttons
            text=MESSAGE, 
            font=self.FONT, 
            anchor="center"
        )

        # Calculate the center positions for the buttons with slightly reduced spacing
        button_width = 125
        button_spacing = 20  # Adjusted spacing between buttons
        total_button_width = 2 * button_width + button_spacing

        yes_button_x = (AVAILABLE_WIDTH - total_button_width) - 125
        no_button_x = yes_button_x + button_width + button_spacing

        # Create Yes button
        yes_button_canvas = customtkinter.CTkCanvas(confirmation_frame, width=button_width, height=50, highlightthickness=0)
        yes_button_canvas.place(x=yes_button_x, y=WINDOW_HEIGHT - 75)
        yes_button_bg_image = Image.open("background2.jpg").resize((button_width, 50))
        yes_button_bg_photo = ImageTk.PhotoImage(yes_button_bg_image)
        yes_button_canvas.create_image(0, 0, image=yes_button_bg_photo, anchor="nw")
        yes_button_canvas.create_text(button_width // 2, 25, text="Yes", fill="white", font=("Pixel Calculon", 16))
        yes_button_canvas.bind("<Button-1>", lambda event: on_confirm())
        yes_button_canvas.image = yes_button_bg_photo

        # Create No button
        no_button_canvas = customtkinter.CTkCanvas(confirmation_frame, width=button_width, height=50, highlightthickness=0)
        no_button_canvas.place(x=no_button_x, y=WINDOW_HEIGHT - 75)
        no_button_bg_image = Image.open("background2.jpg").resize((button_width, 50))
        no_button_bg_photo = ImageTk.PhotoImage(no_button_bg_image)
        no_button_canvas.create_image(0, 0, image=no_button_bg_photo, anchor="nw")
        no_button_canvas.create_text(button_width // 2, 25, text="No", fill="white", font=("Pixel Calculon", 16))
        no_button_canvas.bind("<Button-1>", lambda event: on_cancel())
        no_button_canvas.image = no_button_bg_photo
        self.InfoColor()
        self.UpdateInfoTextColor(confirmation_frame)

    def UpdateConfirmationTextColor(self, frame, text_id):
        CURRENT_TIME = time.time()
        WAVE_SPEED = 64
        CURRENT_INDEX = int(CURRENT_TIME * WAVE_SPEED * 8) % len(self.USERNAME_COLOR)
        COLOR = self.USERNAME_COLOR[CURRENT_INDEX]
        frame.itemconfigure(text_id, fill=COLOR)
        frame.after(150, lambda: self.UpdateConfirmationTextColor(frame, text_id))

    def ConfirmationButtonColorCycle(self, yes_button, no_button):
        if yes_button.winfo_exists() and no_button.winfo_exists():  # Check if both buttons still exist
            CURRENT_TIME = time.time()
            WAVE_SPEED = 64  
            CURRENT_INDEX = int(CURRENT_TIME * WAVE_SPEED * 8) % len(self.BUTTON_COLOR)
            BUTTON_COLOR = self.BUTTON_COLOR[CURRENT_INDEX]
            TEXT_COLOR = self.USERNAME_COLOR[CURRENT_INDEX]

            # Update the colors for both the Yes and No buttons, preserving other styles
            yes_button.configure(
                fg_color=BUTTON_COLOR,
                text_color=TEXT_COLOR,
                border_color="white",  # Set the border color
                border_width=1,  # Set the border width
                corner_radius=8  # Ensure consistent corner radius
            )
            no_button.configure(
                fg_color=BUTTON_COLOR,
                text_color=TEXT_COLOR,
                border_color="white",  # Set the border color
                border_width=1,  # Set the border width
                corner_radius=8  # Ensure consistent corner radius
            )

            # Use `after` to continue the color-cycling effect
            self.AZIMUTH.after(150, lambda: self.ConfirmationButtonColorCycle(yes_button, no_button))

    def RegisterAccount(self):
        USERNAME = self.UserEntry.get()
        PASSWORD = self.PassEntry.get()
        DATABASE = sqlite3.connect("main.db")
        LOOKUP = DATABASE.cursor()
        LOOKUP.execute('SELECT * FROM user WHERE username=?', 
                       (USERNAME,))
        EXISTING_USER = LOOKUP.fetchone()
        if EXISTING_USER:
            self.CenterGUI()
            self.CustomInfo("Registration Error", 
                            "   Username already exists...", 
                            self.FONT)
        else:
            LOOKUP.execute('INSERT INTO user (username, password) VALUES (?, ?)', 
                           (USERNAME, PASSWORD))
            DATABASE.commit()
            self.CenterGUI()
            self.CustomInfo("Registration Successful", 
                            f"   Account created {USERNAME}...", 
                            self.FONT)
        DATABASE.close()

    def DeleteAccount(self):
        DATABASE = sqlite3.connect("main.db")
        LOOKUP = DATABASE.cursor()
        CURRENT_USERNAME = self.CURRENT_USERNAME.itemcget(self.CURRENT_USERNAME_ID, "text")
        if CURRENT_USERNAME:
            LOOKUP.execute('SELECT * FROM user WHERE username=?', 
                           (self.UserEntry.get(),))
            EXISTING_USER = LOOKUP.fetchone()
            if EXISTING_USER:
                LOOKUP.execute('DELETE FROM user WHERE username=?', 
                               (self.UserEntry.get(),))
                DATABASE.commit()
                self.CustomInfo(
                    f"Successfully Deleted",
                    f"   Account {self.UserEntry.get()} removed...",
                    self.FONT,
                )
                self.CURRENT_USERNAME.itemconfigure(self.CURRENT_USERNAME_ID, text="", 
                                                font=self.FONT)
                self.UserEntry.delete(0, 
                                      tk.END)
                self.PassEntry.delete(0, 
                                      tk.END)
            else:
                self.CenterGUI()
                self.CustomInfo("Invalid Error", 
                                "Are you retarded?", 
                                self.FONT)
        else:
            self.CenterGUI()
            self.CustomInfo("Access Denied", 
                            "   Are you retarded?", 
                            self.FONT)
        DATABASE.close()


class ProgressBar(customtkinter.CTkFrame):
    def __init__(self, master=None, position='bottom', **kwargs):
        super().__init__(master, **kwargs)
        self.CUSTOM_PROGRESS = customtkinter.CTkCanvas(self, 
                                                       width=1800, 
                                                       height=50)
        self.CUSTOM_PROGRESS.pack(fill='x', 
                                  padx=0, 
                                  pady=0.5, 
                                  ipadx=0, 
                                  ipady=0)
        self.CUSTOM_WIDTH = 750
        self.CUSTOM_LAYOUT = self.CUSTOM_PROGRESS.create_rectangle(0, 
                                                                   0, 
                                                                   self.CUSTOM_WIDTH, 
                                                                   50, 
                                                                   fill='#0000FF')
        self.PROGRESS_TEXT = self.CUSTOM_PROGRESS.create_text(self.CUSTOM_WIDTH, 
                                                              25, 
                                                              text="0%", 
                                                              anchor="w", 
                                                              font=("Pixel Calculon", 12), 
                                                              fill="white")
        self.PROGRESS_POSITION(position)
        self.FONT = ("Pixel Calculon", 24)

    def PROGRESS_POSITION(self, position):
        if position == 'bottom':
            self.pack_configure(expand=True)
        else:
            x, y = position
            self.place_configure(x=95, y=y + 15)

    def START_PROGRESS(self):
        pass

    def STOP_PROGRESS(self):
        pass

    def SET_PROGRESS(self, value):
        self.CUSTOM_WIDTH = int(value * 1800)
        self.CUSTOM_PROGRESS.coords(self.CUSTOM_LAYOUT, 
                                    0, 
                                    0, 
                                    self.CUSTOM_WIDTH, 
                                    50)
        TEXT_POSITION = self.CUSTOM_WIDTH - 100 if self.CUSTOM_WIDTH else self.CUSTOM_WIDTH
        self.CUSTOM_PROGRESS.coords(self.PROGRESS_TEXT, 
                                    TEXT_POSITION, 
                                    25)
        self.CUSTOM_PROGRESS.itemconfigure(self.PROGRESS_TEXT, 
                                           text=f"{int(value * 100)}%",
                                           fill="White",
                                           font=self.FONT)


class LoadingScreen:
    def __init__(self):
        self.CUSTOM_LOADING = customtkinter.CTk()
        self.CUSTOM_LOADING.overrideredirect(True)
        self.CUSTOM_LOADING.geometry("800x600")
        self.CUSTOM_TASKS = [
        (" ➤ Initializing Azimuth V1.2 standby        ➤ Successful connection ➤ Version 1.2 ➤ Loading please wait ",  1),
        (" ➤ Initializing Azimuth V1.2 standby        ➤ Successful connection ➤ Version 1.2 ➤ Loading please wait ",  1), 
        (" ➤ Initializing Azimuth V1.2 standby        ➤ Successful connection ➤ Version 1.2 ➤ Loading please wait ",  1),
        (" ➤ Initializing Azimuth V1.2 standby        ➤ Successful connection ➤ Version 1.2 ➤ Loading please wait ",  1),    
        (" ➤ Loading Bullshit upon bullshit           ➤ Successful connection ➤ Version 1.2 ➤ Loading please wait ",  1),     
        (" ➤ Loading Elon Musks bank statements       ➤ Successful connection ➤ Version 1.2 ➤ Loading please wait ",  1),  
        (" ➤ Loading the entirety of Auschwitz        ➤ Successful connection ➤ Version 1.2 ➤ Loading please wait ",  1),     
        (" ➤ Loading the long lost cure for cancer    ➤ Successful connection ➤ Version 1.2 ➤ Loading please wait ",  1), 
        (" ➤ Loading the browsing history of everyone ➤ Successful connection ➤ Version 1.2 ➤ Loading please wait ",  1), 
        (" ➤ Loading my cat Misty attempting to hunt  ➤ Successful connection ➤ Version 1.2 ➤ Loading please wait ",  1),     
        (" ➤ Loading Michael Myers get ready to run   ➤ Successful connection ➤ Version 1.2 ➤ Loading please wait ",  1),
        (" ➤ Loading my missing braincell             ➤ Successful connection ➤ Version 1.2 ➤ Loading please wait ",  1),
        (" ➤ Try logging in for a better experience   ➤ Successful connection ➤ Version 1.2 ➤ Use at your own risk",  1),
        (" ➤ Try logging in for a better experience   ➤ Successful connection ➤ Version 1.2 ➤ Use at your own risk",  1),                       
        ]
        self.CUSTOM_BANNER = f"""   Version: 1.2 ➤ By: Astroolean
        """
        self.AFTER = [] 
        X = 0
        Y = 50
        AZIMUTH_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        BACKGROUND_PATH = os.path.join(AZIMUTH_DIRECTORY, 
                                             'LoadingUI', 
                                             'Loading.jpg')
        CUSTOM_BACKGROUND = Image.open(BACKGROUND_PATH)
        CUSTOM_BACKGROUND = ImageTk.PhotoImage(CUSTOM_BACKGROUND)
        self.CYCLE_TEXT = self.TEST_COLOR()
        self.CYCLE_TASK = self.TASK_COLOR()
        self.CUSTOM_BANNER_CANVAS = customtkinter.CTkCanvas(self.CUSTOM_LOADING, 
                                                            width=800, 
                                                            height=600)
        self.CUSTOM_BANNER_CANVAS.place(relwidth=1, 
                                        relheight=1)
        self.CUSTOM_BANNER_CANVAS.create_image(0, 
                                               0, 
                                               anchor="nw", 
                                               image=CUSTOM_BACKGROUND)
        self.CenterGUI()
        X = 100
        Y = 150
        self.CUSTOM_BAR = ProgressBar(self.CUSTOM_LOADING, 
                                            position=(X, Y))
        self.CUSTOM_BAR.START_PROGRESS()
        self.CUSTOM_LOADING.update()
        self.Loading()
        time.sleep(1)
        self.CloseWindow() 

    def Loading(self):
        TOTAL = random.randint(150, 300)
        TASK_COUNT = len(self.CUSTOM_TASKS)
        for i in range(TOTAL):
            if not self.CUSTOM_LOADING.winfo_exists():
                return 
            time.sleep(0.01)
            VALUE = (i + 1) / TOTAL
            self.CUSTOM_BAR.SET_PROGRESS(VALUE)
            CURRENT_TASK_INDEX = int(VALUE * TASK_COUNT)
            if CURRENT_TASK_INDEX < TASK_COUNT:
                self.CURRENT_TASK_TEXT = self.CUSTOM_TASKS[CURRENT_TASK_INDEX][0]
                self.TASK_TEXT(self.CURRENT_TASK_TEXT)
                self.UPDATE_TASK_COLOR()
            self.CUSTOM_LOADING.update_idletasks()
        self.CUSTOM_BAR.STOP_PROGRESS()

    def CenterGUI(self):
        SCREEN_WIDTH = self.CUSTOM_LOADING.winfo_screenwidth()
        SCREEN_HEIGHT = self.CUSTOM_LOADING.winfo_screenheight()
        WINDOW_WIDTH = 1915
        WINDOW_HEIGHT = 225
        X = (SCREEN_WIDTH - WINDOW_WIDTH) // 2
        Y = (SCREEN_HEIGHT - WINDOW_HEIGHT) // 1.75
        self.CUSTOM_LOADING.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{X}+{Y}")

    def CloseWindow(self):
        for after_id in self.AFTER:
            self.CUSTOM_LOADING.after_cancel(after_id)
        self.CUSTOM_LOADING.destroy()

    def UPDATE_TASK_COLOR(self):
        try:
            if not self.CUSTOM_LOADING.winfo_exists():
                return
            CURRENT_TIME = time.time()
            WAVE_SPEED = 2
            WAVE_LENGTH = len(self.CURRENT_TASK_TEXT)
            self.CUSTOM_BANNER_CANVAS.delete("task_text_color_wave") 
            TEXT_WIDTH = 15 * WAVE_LENGTH 
            X = (1825 - TEXT_WIDTH) // 2 
            for i, char in enumerate(self.CURRENT_TASK_TEXT):
                LETTER_TIME = CURRENT_TIME - (i / WAVE_LENGTH) * WAVE_SPEED
                CURRENT_INDEX = int(LETTER_TIME * 64) % len(self.CYCLE_TASK)
                COLOR = self.CYCLE_TASK[CURRENT_INDEX]
                POSITION = X + i * 16 
                self.CUSTOM_BANNER_CANVAS.create_text(POSITION, 
                                                      125, 
                                                      text=char, 
                                                      font=("Pixel Calculon", 16), 
                                                      fill=COLOR, 
                                                      tags="task_text_color_wave", 
                                                      anchor="ne")
            after_id = self.CUSTOM_LOADING.after(50, self.UPDATE_TASK_COLOR)
            self.AFTER.append(after_id)  
        except Exception as e:
            print("An unexpected error occurred:", e)

    def UPDATE_TEXT_COLOR(self):
        try:
            if not self.CUSTOM_LOADING.winfo_exists():
                return  
            CURRENT_TIME = time.time()
            WAVE_SPEED = 64
            WAVE_LENGTH = len(self.CUSTOM_BANNER)
            self.CUSTOM_BANNER_CANVAS.delete("text") 
            for i, char in enumerate(self.CUSTOM_BANNER):
                WAVE_INDEX = (WAVE_LENGTH - i + CURRENT_TIME * WAVE_SPEED) % WAVE_LENGTH
                COLOR_INDEX = int(WAVE_INDEX / WAVE_LENGTH * len(self.CYCLE_TEXT))
                COLOR = self.CYCLE_TEXT[COLOR_INDEX]
                POSITION = i * 50 
                self.CUSTOM_BANNER_CANVAS.create_text(POSITION, 
                                                      50,
                                                      text=char, 
                                                      font=("Pixel Calculon", 48), 
                                                      fill=COLOR, 
                                                      tags="text",
                                                      justify="left")
            after_id = self.CUSTOM_LOADING.after(50, self.UPDATE_TEXT_COLOR)
            self.AFTER.append(after_id)
        except Exception as e:
            print("An unexpected error occurred:", e)

    def TASK_TEXT(self, text):
        self.CUSTOM_BANNER_CANVAS.delete("task_text")  
        self.CUSTOM_BANNER_CANVAS.create_text(2692, 
                                              9226, 
                                              text="", 
                                              tags="task_text")
        self.UPDATE_TEXT_COLOR() 

    def TASK_COLOR(self, num_colors=1000):
        TASK_COLORS = [
            "#{:02x}{:02x}{:02x}".format(
                int(128 + 127 * cos(16 * pi * i / num_colors)),
                int(128 + 127 * cos(16 * pi * i / num_colors + 2 * pi / 3)),
                int(128 + 127 * cos(16 * pi * i / num_colors + 4 * pi / 3)),
            )
            for i in range(num_colors)
        ]
        return TASK_COLORS

    def TEST_COLOR(self, num_colors=1000):
        TEXT_COLORS = [
            "#{:02x}{:02x}{:02x}".format(
                int(96 + 16 * cos(2 * pi * i / num_colors + 1 / 3)), 
                int(128 + 127 * cos(2 * pi * i / num_colors + 2 * pi / 3)), 
                int(128 + 127 * cos(2 * pi * i / num_colors + 4 * pi / 3)), 
            )
            for i in range(num_colors)
        ]
        return TEXT_COLORS


class TabContent:
    PROGRAMS = []
    def __init__(self, PARENT, INDEX):
        self.PARENT = PARENT
        self.INDEX = INDEX
        self.BUTTONS = []  
        AZIMUTH_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        BACKGROUND_PATH = os.path.join(AZIMUTH_DIRECTORY, 'LoadingUI', 'Loading.jpg')
        CUSTOM_BACKGROUND = Image.open(BACKGROUND_PATH)
        self.CUSTOM_BACKGROUND = ImageTk.PhotoImage(CUSTOM_BACKGROUND)
        self.tab_content_frame = customtkinter.CTkFrame(PARENT)
        self.tab_content_frame.place_forget()
        BACKGROUND = Label(self.tab_content_frame, image=self.CUSTOM_BACKGROUND, borderwidth=0)
        BACKGROUND.place(x=0, y=0, relwidth=1, relheight=1)
        self.tab_content_frame.configure(width=400, height=300) 
        self.APP = customtkinter.CTkButton(
            self.tab_content_frame,
            text=f'APP {INDEX + 1}',
            command=lambda: self.ButtonAction(('APP', INDEX)) 
        )
        self.APP.pack(padx=10, pady=10)
        self.HELP = customtkinter.CTkButton(
            self.tab_content_frame,
            text=f'HELP {INDEX + 1}',
            command=lambda: self.ButtonAction(('HELP', INDEX))
        )
        self.HELP.pack(padx=10, pady=10)
        TabContent.PROGRAMS.append(self.tab_content_frame)

    def ShowContent(self):
        self.PARENT.pack(side='left', expand=True, fill='both')
        for tab_content in TabContent.PROGRAMS:
            tab_content.place_forget()
        self.tab_content_frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    def CreateButton(self, TEXT, INDEX):
        BUTTON_COMMAND = lambda i=INDEX: self.ButtonAction(i)
        BUTTON = customtkinter.CTkButton(self.tab_content_frame, text=TEXT, command=BUTTON_COMMAND)
        BUTTON.pack(padx=10, pady=10)
        self.BUTTONS.append(BUTTON)

    def ButtonAction(self, INFO):
        BUTTON_TYPE, index = INFO
        if BUTTON_TYPE == 'APP':
            if index + 1 == 1:
                print(f"Test...1")
            if index + 1 == 2:
                print(f"Test...2")
            if index + 1 == 3:
                print(f"Test...3")
            if index + 1 == 4:
                print(f"Test...4")
            if index + 1 == 5:
                print(f"Test...5")
            if index + 1 == 6:
                print(f"Test...6")
            if index + 1 == 7:
                print(f"Test...7")
            if index + 1 == 8:
                print(f"Test...8")
            if index + 1 == 9:
                print(f"Test...9")
            if index + 1 == 10:
                print(f"Test...10")
        elif BUTTON_TYPE == 'HELP':
            if index + 1 == 1:
                print(f"1")
            if index + 1 == 2:
                print(f"2")
            if index + 1 == 3:
                print(f"3")
            if index + 1 == 4:
                print(f"4")
            if index + 1 == 5:
                print(f"5")
            if index + 1 == 6:
                print(f"6")
            if index + 1 == 7:
                print(f"7")
            if index + 1 == 8:
                print(f"8")
            if index + 1 == 9:
                print(f"9")
            if index + 1 == 10:
                print(f"10")




if __name__ == "__main__":   
    try:
        APP = AzimuthApp()
        APP.AZIMUTH.mainloop()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")