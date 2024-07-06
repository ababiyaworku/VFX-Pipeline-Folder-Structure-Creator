"""
██████╗░███████╗██╗░░░██╗░░░░░░██████╗░██╗░░░██╗░░░░░░░█████╗░██████╗░░█████╗░██████╗░░█████╗░██╗██╗░░░██╗░█████╗░
██╔══██╗██╔════╝██║░░░██║░░░░░░██╔══██╗╚██╗░██╔╝░░░░░░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║╚██╗░██╔╝██╔══██╗
██║░░██║█████╗░░╚██╗░██╔╝█████╗██████╦╝░╚████╔╝░█████╗███████║██████╦╝███████║██████╦╝███████║██║░╚████╔╝░███████║
██║░░██║██╔══╝░░░╚████╔╝░╚════╝██╔══██╗░░╚██╔╝░░╚════╝██╔══██║██╔══██╗██╔══██║██╔══██╗██╔══██║██║░░╚██╔╝░░██╔══██║
██████╔╝███████╗░░╚██╔╝░░░░░░░░██████╦╝░░░██║░░░░░░░░░██║░░██║██████╦╝██║░░██║██████╦╝██║░░██║██║░░░██║░░░██║░░██║
╚═════╝░╚══════╝░░░╚═╝░░░░░░░░░╚═════╝░░░░╚═╝░░░░░░░░░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝

"""
import os

# Define the main folder and subfolder names
main_folder = "VFX"
subfolders = [
    "01_Concept and Pre-Production",
    "02_Storyboarding and Pre-visualization",
    "03_R&D and Asset Creation",
    "04_Match-moving and Tracking",
    "05_Layout & Animation",
    "06_Simulation",
    "07_Lighting and Rendering",
    "08_Compositing",
    "09_Review and Iteration",
    "10_Final Delivery"
]

# Get the current working directory
current_directory = os.getcwd()

# Create the main folder path
main_folder_path = os.path.join(current_directory, main_folder)

# Create the main folder
os.makedirs(main_folder_path, exist_ok=True)

# Create subfolders
for subfolder in subfolders:
    subfolder_path = os.path.join(main_folder_path, subfolder)
    os.makedirs(subfolder_path, exist_ok=True)

print(f"Folder structure created successfully in {main_folder_path}")
