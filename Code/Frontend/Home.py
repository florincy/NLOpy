import tkinter as tk
from PIL import Image, ImageTk
import os

class Home:
    def __init__(self, master=None):
        self.master = master
        self.master.title("NLO data app")

        # Create a main frame
        self.main_frame = tk.Frame(master)  # Use a light purple background
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Create a label for the title
        title_label = tk.Label(self.main_frame, text="Welcome to NLOpy!", font=("Calibri", 24), bg="#E6E6FA")
        title_label.pack(pady=(20, 10))  

        # Create a label for the description
        description_text = ("NLOpy is an application for dealing with NLO inputs and outputs from Gaussian 16.0 software, "
                            "given the laborious work required to do such calculations. Enjoy!")
        description_label = tk.Label(self.main_frame, text=description_text, 
                                     font=("Calibri", 16), wraplength=600, justify="left")
        description_label.pack(pady=(0, 20))  
        
        #Paths to images
        current_dir = os.path.dirname(__file__)
        nqtcm_path = os.path.join(current_dir, 'nqtcm.png')
        nlopy_path = os.path.join(current_dir, 'nlopy.png')
        
        self.photo_frame = tk.Frame(self.main_frame, bg="#E6E6FA")  # Use a light purple background
        self.photo_frame.pack()
        
        # Load and display imagees
        img1 = Image.open(nqtcm_path)  # Replace "your_image_file_path.jpg" with the path to your image file
        img1 = img1.resize((250, 100), Image.LANCZOS)  # Resize the image as needed
        photo1 = ImageTk.PhotoImage(img1)
        img2 = Image.open(nlopy_path)  # Replace "your_image_file_path.jpg" with the path to your image file
        img2 = img2.resize((170, 100), Image.LANCZOS)  # Resize the image as needed
        photo2 = ImageTk.PhotoImage(img2)
        image1_label = tk.Label(self.photo_frame, image=photo1)
        image1_label.image = photo1  # Keep a reference to the image to prevent garbage collection
        image1_label.pack(side="left",pady=20,padx=10)  # Add some padding after the image
        image2_label = tk.Label(self.photo_frame, image=photo2)
        image2_label.image = photo2  # Keep a reference to the image to prevent garbage collection
        image2_label.pack(side="left",pady=20, padx=10)  # Add some padding after the image
        
        # Create a label for the list title
        title_list_label = tk.Label(self.main_frame, text="Properties calculated:", font=("Calibri", 16,), bg="#E6E6FA")
        title_list_label.pack(pady=(20, 10))

        # Add items to the list
        # Define a bullet point Unicode character
        bullet = "\u2022"
        items = ["Polarizability", "Hyperpolarizability", "Second Hyperpolarizability", "Electric Dipole"]
        # Iterate over the items and create a label for each with bullet point styling
        for item in items:
            label_text = f"{bullet} {item}"  # Add bullet point before each item
            label = tk.Label(self.main_frame, text=label_text, font=("Calibri", 12))
            label.pack(pady=2, anchor="w", padx=20)  # Add some padding for indentation


