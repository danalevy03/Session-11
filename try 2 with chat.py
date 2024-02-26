def print_b_words(file_name):
    try:
        with open(file_name, 'r') as file:
            words = file.read().split()

            # Print 3-letter words starting with 'b'
            for word in words:
                if len(word) == 3 and word.startswith('b'):
                    print(word)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_name = 'bet.txt'  # Replace with your actual file name
print_b_words(file_name)


