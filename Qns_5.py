file_name = 'sample-file.txt'

total_words = 0
line_count = 0

with open(file_name, 'r') as file:
    for line in file:
        # Count the number of lines with 'q' (case-insensitive)
        if 'q' in line.lower():
            line_count += 1
        # Split the line into words and count the words
        words = line.split()
        total_words += len(words)

if line_count > 0:
    average_words_per_line = total_words / line_count
else:
    average_words_per_line = 0

print(f"Number of lines with 'q': {line_count}")
print(f"Average number of words in lines: {average_words_per_line:.2f}")
