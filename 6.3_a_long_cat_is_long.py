"""
Yaakov Haimoff
"""
import string

def count_words():
    """
    Counts the number of characters in each word of a given text.

    Returns:
    dict: A dictionary where the keys are the words in the text and the values
    are the lengths of those words.
    """
    return {t: len(t) for t in text.split()}


text = """
You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat."""

# Remove all punctuation characters
translator = str.maketrans('', '', string.punctuation)
text = text.translate(translator)

print(count_words())
