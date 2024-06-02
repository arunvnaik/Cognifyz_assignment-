def count_words_in_file(file_path):
    word_counts = {}
    
    try:
        
        with open(file_path, 'r') as file:
            # Read the file content
            text = file.read()
            
            # Split text into words and count them
            words = text.split()
            for word in words:
                word = word.lower().strip(".,!?\"'()[]{}:;")
                if word:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
        
        # Sort the word counts dictionary alphabetically by word
        sorted_word_counts = dict(sorted(word_counts.items()))
        
        # Display the word counts
        for word, count in sorted_word_counts.items():
            print(f"{word}: {count}")
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
file_path = input("Enter the path to the text file: ")
count_words_in_file(file_path)
