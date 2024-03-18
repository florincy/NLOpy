import tkinter as tk
from PIL import Image, ImageTk

class Home:
    def __init__(self, master=None):
        self.master = master
        self.master.title("NLO data app")

        # Create a main frame
        self.main_frame = tk.Frame(master, bg="#E6E6FA")  # Use a light purple background
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Create a label for the title
        title_label = tk.Label(self.main_frame, text="Welcome to NLOpy!", font=("Calibri", 24, "italic"), bg="#E6E6FA")
        title_label.pack(pady=(20, 10))  # Add some padding at the top

        # Create a label for the description
        description_text = ("NLOpy is an application for dealing with NLO inputs and outputs from Gaussian 16.0 software, "
                            "given the laborious work required to do such calculations. Enjoy!")
        description_label = tk.Label(self.main_frame, text=description_text, 
                                     font=("Calibri", 16), bg="#E6E6FA", wraplength=600, justify="left")
        description_label.pack(pady=(0, 20))  # Add some padding at the bottom

        # Load and display an image
        img = Image.open("/home/florincy/NLO/Code/nqtcm.png")  # Replace "your_image_file_path.jpg" with the path to your image file
        img = img.resize((400, 160), Image.ANTIALIAS)  # Resize the image as needed
        photo = ImageTk.PhotoImage(img)
        image_label = tk.Label(self.main_frame, image=photo)
        image_label.image = photo  # Keep a reference to the image to prevent garbage collection
        image_label.pack(pady=20)  # Add some padding after the image
        # Create a label for the list title
        title_list_label = tk.Label(self.main_frame, text="Properties calculated:", font=("Calibri", 16,), bg="#E6E6FA")
        title_list_label.pack(pady=(20, 10))

        # Add items to the list
        items = ["Polarizability", "Hyperpolarizability", "Second Hyperpolarizability", "Electric Dipole"]
        for item in items:
            label = tk.Label(self.main_frame, text=item, font=("Calibri", 12), bg="#E6E6FA")
            label.pack(pady=5, anchor="w")


