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
subfolders = {
    "01_Concept and Pre-Production": ["03_References", "04_Concept Art", "05_Mood Boards", "01_Scripts", "02_Meeting Notes"],
    "02_Storyboarding and Pre-visualization": ["01_Storyboards", "03_Animatics", "04_Previs Renders", "02_Shot Lists", "05_Revisions"],
    "03_R&D and Asset Creation": ["01_Research Documents", "06_Tools and Plugins", "02_3D Models", "03_Textures", "04_Materials", "05_Asset Libraries"],
    "04_Match-moving and Tracking": ["01_Raw Footage", "02_Tracking Data", "05_Matchmoving Projects", "03_Camera Data", "04_Lens Distortion"],
    "05_Layout & Animation": ["01_Layout Files", "02_Animation Blocking", "03_Animation Curves", "05_Final Animations", "04_Motion Capture Data"],
    "06_Simulation": ["01_Simulation Projects", "05_Cache Files", "02_Particle Simulations", "04_Fluid Simulations", "03_Destruction Simulations"],
    "07_Lighting and Rendering": ["02_Lighting Setups", "01_HDRIs", "03_Render Settings", "04_Render Layers", "05_Final Renders"],
    "08_Compositing": ["01_Compositing Projects", "02_Render Passes", "03_Matte Paintings", "04_Keying Files", "05_Final Comps"],
    "09_Review and Iteration": ["01_Review Renders", "04_Feedback Notes", "03_Versions", "05_Approval Documents", "02_Meeting Recordings"],
    "10_Final Delivery": ["04_Master Files", "05_Delivery Formats", "03_QC Reports", "02_Backup Files", "01_Client Feedback"]
}

# Get the current working directory
current_directory = os.getcwd()

# Create the main folder path
main_folder_path = os.path.join(current_directory, main_folder)

# Create the main folder
os.makedirs(main_folder_path, exist_ok=True)

# Create subfolders and their respective sub-subfolders
for subfolder, sub_subfolders in subfolders.items():
    subfolder_path = os.path.join(main_folder_path, subfolder)
    os.makedirs(subfolder_path, exist_ok=True)
    for sub_subfolder in sub_subfolders:
        sub_subfolder_path = os.path.join(subfolder_path, sub_subfolder)
        os.makedirs(sub_subfolder_path, exist_ok=True)

print(f"Folder structure created successfully in {main_folder_path}")
