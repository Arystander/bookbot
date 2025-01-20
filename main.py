import string

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(file_contents)

def word_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    return len(words)

def char_count():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    lowercase_text = file_contents.lower()
    char_count = {}

    for char in lowercase_text:
        if char in string.ascii_lowercase:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    return char_count

word_count_var = word_count()

report_lines = []
report_lines.append("--- Begin report of books/frankenstein.txt ---")
report_lines.append(f"{word_count_var} words found in the document")
report_lines.append("")

char_count_dict = char_count()

sorted_char_count = sorted(char_count_dict.items(), key=lambda item: item[1], reverse=True)

for char, count in sorted_char_count:
    report_lines.append(f"The '{char}' character was found {count} times")

report_lines.append("--- End report ---")

print(report_lines)