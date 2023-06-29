#speed typing test
import time
import random

def calculate_typing_speed(start_time, end_time, typed_text):
    elapsed_time = end_time - start_time
    words = typed_text.split()
    num_words = len(words)
    num_characters = len(typed_text)
    typing_speed = (num_words / elapsed_time) * 60
    return typing_speed

def run_typing_test():
    print("Welcome to the Speed Typing Test!")
    print("Type the following text as quickly and accurately as possible:")
    print(reference_text)
    print("Press Enter when you're ready to start.")

    input("")

    print("Timer starts now...")

    time.sleep(1)  # Delay before starting the timer

    start_time = time.time()

    typed_text = input("Start typing: ")

    end_time = time.time()

    typing_speed = calculate_typing_speed(start_time, end_time, typed_text)

    print("\n--- Speed Typing Test Results ---")
    print("Reference Text Length:", len(reference_text), "characters")
    print("Typed Text Length:", len(typed_text), "characters")
    print("Total Time:", round(end_time - start_time, 2), "seconds")
    print("Typing Speed:", round(typing_speed, 2), "words per minute")

    calculate_typing_accuracy(reference_text, typed_text)

def calculate_typing_accuracy(reference_text, typed_text):
    reference_words = reference_text.split()
    typed_words = typed_text.split()
    correct_words = 0

    for reference_word, typed_word in zip(reference_words, typed_words):
        if reference_word == typed_word:
            correct_words += 1

    accuracy = (correct_words / len(reference_words)) * 100
    print("Accuracy:", round(accuracy, 2), "%")

# Example usage:
reference_text = "The quick brown fox jumps over the lazy dog."

run_typing_test()
