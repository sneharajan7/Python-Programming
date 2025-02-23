import enchant
import tkinter as tk

# Create an enchant dictionary for English
dictionary = enchant.Dict("en_US")

# Create the main window
window = tk.Tk()
window.title("Text Editor")

# Create a Text widget to display the text
text = tk.Text(window)
text.pack()

# Create a function to check the spelling of the text
def check_spelling():
    # Get the text from the Text widget
    text_string = text.get("1.0", "end")

    # Split the text into a list of words
    words = text_string.split()

    # Initialize a list to store the spelling mistakes
    spelling_mistakes = []

    # Iterate over the list of words
    for word in words:
        # If the word is not in the dictionary, add it to the list of spelling mistakes
        if not dictionary.check(word):
            spelling_mistakes.append(word)

    # If there are spelling mistakes, find a set of appropriate words for each mistake
    if spelling_mistakes:
        # Initialize a list to store the appropriate words
        appropriate_words = []

        # Iterate over the list of spelling mistakes
        for mistake in spelling_mistakes:
            # Find similar words and filter the list to include only those that are in the dictionary
            similar_words = [word for word in dictionary.suggest(mistake) if dictionary.check(word)]
            # Add the list of similar words to the list of appropriate words
            appropriate_words.extend(similar_words)

        # Display the spelling mistakes and appropriate words in a message box
        tk.messagebox.showinfo("Spelling Check", f"Spelling mistakes: {spelling_mistakes}\nAppropriate words: {appropriate_words}")
    else:
        # Display a message if there are no spelling mistakes
        tk.messagebox.showinfo("Spelling Check", "No spelling mistakes found.")

# Create a Button widget to trigger the spelling check
button = tk.Button(window, text="Check Spelling", command=check_spelling)
button.pack()

# Run the main loop
window.mainloop()
