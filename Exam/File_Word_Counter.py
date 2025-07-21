def word_counter(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read().lower()
    except FileNotFoundError:
        print("File not found.")
        return