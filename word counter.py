# Task: Create a Word Counter



# Prompt the user to enter a text
user_paragraph = input("Enter a text: ")


# Check if the input is empty
if (not user_paragraph):
    print("No text entered, try again! ")
else:
    # Convert the input to uppercase
    user_paragraph = user_paragraph.upper()

# Initialize a counter for words (assuming at least one word exists)
wordcounter = 1

# Initialize an index for iterating through the characters of the paragraph
i = 0

# Iterate through each character of the user's input
while(i<len(user_paragraph)):
    # Check if the character is a space
    if(user_paragraph[i] == " "):
        # If a space is found, increment the word counter and move to the next character
        wordcounter += 1
        i += 1
    else:
        # If not a space, move to the next character
        i += 1

# Print the total word count
print("The counted words: " + str(wordcounter))