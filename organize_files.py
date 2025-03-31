import os

# Get all .ipynb files in the current directory
files = [file for file in os.listdir() if file.endswith('.ipynb')]

for file in files:
    # Get the project name (file name without extension)
    project_name = os.path.splitext(file)[0]

    # Create a folder and subfolder
    os.makedirs(f"{project_name}/data", exist_ok=True)

    # Move the .ipynb file into the project folder
    os.rename(file, f"{project_name}/{file}")

    # Create a README.md file with a basic description
    with open(f"{project_name}/README.md", "w") as readme:
        readme.write(f"# {project_name} Project\n\nThis folder contains the `{file}` project and its related data.")