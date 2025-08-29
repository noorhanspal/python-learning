import re # regular expression module

text = input("Paste your text:\n")
words = re.findall(r"\b[\w']+\b", text)
chars_with_spaces = len(text)
chars_no_spaces = len(text.replace(" ", ""))
sentences = re.findall(r"[.!?]+", text)

print("Words:", len(words))
print("Characters (with spaces):", chars_with_spaces)
print("Characters (no spaces):", chars_no_spaces)
print("Sentences (approx):", len(sentences)) 