import os
import shutil

# Define the path to your repository
repo_path = "A:\\Adan\\GitHub\\Portfolio"

# Ensure we're in the correct directory
os.chdir(repo_path)

# Get all Jupyter Notebook files
notebooks = [f for f in os.listdir() if f.endswith(".ipynb")]

for notebook in notebooks:
    # Create a folder name based on the notebook name (without extension)
    notebook_name = os.path.splitext(notebook)[0]
    notebook_folder = os.path.join(repo_path, notebook_name)

    # Create the notebook folder if it doesn't exist
    os.makedirs(notebook_folder, exist_ok=True)

    # Move the notebook file into its folder
    shutil.move(notebook, os.path.join(notebook_folder, notebook))

    # Create a README.md file
    readme_path = os.path.join(notebook_folder, "README.md")
    with open(readme_path, "w") as f:
        f.write(f"# {notebook_name}\n\nDescription of the notebook.\n")

    # Create a data subfolder
    data_folder = os.path.join(notebook_folder, "data")
    os.makedirs(data_folder, exist_ok=True)

print("Reorganization complete!")