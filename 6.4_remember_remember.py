"""
Yaakov Haimoff
"""
from PIL import Image
import numpy as np


def decode_message(image_path):
    """
    Decodes a secret message encoded as a black in a white barcode image file.

    Parameters:
    image_path (str): The file path of the image.

    Returns:
    str: The decoded message.
    """
    # Open the image file and convert it to a numpy array
    image = Image.open(image_path)
    # finds the black pixels in the image and converts them to characters in a string
    return ''.join([chr(i) for i in np.argmax(np.array(image) == 1, axis=0)])



print(decode_message("code.png"))
