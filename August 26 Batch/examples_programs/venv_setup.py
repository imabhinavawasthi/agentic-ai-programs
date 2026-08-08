data = {
    "name": "Abhinav Awasthi",
    "role": "Software Engineer",
    "skills": ["Python", "JavaScript", "Django", "React"]
}

print(data["name"])
print(data["role"])
print(data["skills"])

######################
# To create a virtual environment in Python, you can use the `venv` module. Here are the steps to set it up:
# 1. Open your terminal or command prompt.
# 2. Navigate to the directory where you want to create the virtual environment.
# 3. Run the following command to create a virtual environment:
#    python -m venv myenv
#    Replace `myenv` with the desired name for your virtual environment.
# 4. Activate the virtual environment:
#    - On Windows:
#      myenv\Scripts\activate
#    - On macOS and Linux:
#      source myenv/bin/activate
# 5. Once activated, you can install packages using pip, and they will be isolated from the global Python environment.
# 6. To deactivate the virtual environment, simply run:
#    deactivate