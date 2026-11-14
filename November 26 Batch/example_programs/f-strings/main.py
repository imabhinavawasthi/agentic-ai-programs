topic = "Agentic AI"
pages = 100

prompt = f"I need to write a {pages} pages of document on the topic - {topic}"
print(prompt)

prompt = "I need to write a {} pages of document on the topic - {}"
print(prompt.format(100, "Python"))