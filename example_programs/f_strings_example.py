project_name = "f_strings_example"
file_name = "hello.py"
python_version = "3.6"

prompt_to_create_python_project = f"""
Please create a python project
with the name {project_name} and add 
a file named {file_name} in it.
In the file {file_name}, write a code snippet 
that demonstrates the use print, also use
python version {python_version}.
"""

print(prompt_to_create_python_project)

prompt_to_create_python_project = """
Please create a python project
with the name {} and add 
a file named {} in it.
In the file {}, write a code snippet 
that demonstrates the use print, also use
python version {}.
"""

print(prompt_to_create_python_project.format(project_name, file_name, file_name, python_version))
print(prompt_to_create_python_project.format("project1", "file1.py", "file1.py", "3.8"))
print(prompt_to_create_python_project.format("project2", "file2.py", "file2.py", "3.9"))