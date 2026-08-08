prompt1 = """
I need to create a file named introduction.pdf,
which will have 10 lines of text, on the topic:
Introduction to Python
"""
print(prompt1)

prompt2 = """
I need to create a file named pydantic.pdf,
which will have 20 lines of text, on the topic:
Introduction to Pydantic
"""
print(prompt2)

prompt3 = """
I need to create a file named fastapi.pdf,
which will have 30 lines of text, on the topic:
Introduction to FastAPI
"""
print(prompt3)

file_name = "f-string.pdf"
line_count = 40
topic_name = "Introduction to f-string in Python"

prompt = f"""
I need to create a file named {file_name},
which will have {line_count} lines of text, on the topic:
{topic_name}
"""
print(prompt)