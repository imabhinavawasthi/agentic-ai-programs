prompt = """
I need to create a file named {},
which will have {} lines of text, on the topic:
{}
"""
# in this prompt, first variable is file_name, second variable is line_count, and third variable is topic_name


print(prompt.format("f-string.pdf", 40, "Introduction to f-string in Python"))

print(prompt.format("agentic-ai.pdf", 100, "Introduction to agentic-ai in Python"))