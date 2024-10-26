with open("books/frankenstein.txt") as f:
    file_contents = f.read()

words = file_contents.split()
lower_text = file_contents.lower()

char_count = {}

for char in lower_text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{len(words)} words found in the document")
for char in sorted_char_count:
    if char[0].isalpha():
        print(f"The '{char[0]}' character was found {char[1]} times")
print("--- End report ---")