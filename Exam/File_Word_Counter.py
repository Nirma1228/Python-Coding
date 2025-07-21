def word_counter(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()
    except FileNotFoundError:
        print("File not found.")
        return

    words = text.split()
    count = {}

    for word in words:
        word = word.strip(".,!?()[]{}\"'")  # remove punctuation
        count[word] = count.get(word, 0) + 1

    for word, freq in sorted(count.items(), key=lambda x: x[1], reverse=True):
        print(f"{word}: {freq}")

# Replace with your own file path
word_counter("sample.txt")
