# cv2 is the module import name for opencv-python
import cv2

"""
The OS module in Python provides functions for creating and removing a directory (folder),
fetching its contents, changing and identifying the current directory,
etc. You first need to import the os module to interact with the underlying operating system.
"""
import os

# Python Steganography module
from stegano import lsb
import math

# Extract frames (i.e digital imgs from video) in directory ./tmp
def frame_extraction(video):
    if not os.path.exists("./tmp"):
        os.makedirs("tmp")
    temp_folder = "./tmp"
    print("tmp directory is created")
    
    # we capture the video frame by frame
    vidcap = cv2.VideoCapture(video)
    count = 0

    while True:
        # This method takes no arguments and returns a tuple. 
        # The first returned value is a Boolean indicating if a frame was read correctly (True) or not (False).
        success, image = vidcap.read()
        if not success:
            break
        # save image
        cv2.imwrite(os.path.join(temp_folder, "{:d}.png".format(count)), image)
        count += 1
        
     
    
# split input text to be hidden
def split_string(s_str, count=10):
    per_c = math.ceil(len(s_str) / count)
    c_cout = 0
    out_str = ''
    split_list = []
    for s in s_str:
        out_str += s
        c_cout += 1
        if c_cout == per_c:
            split_list.append(out_str)
            out_str = ''
            c_cout = 0
    if c_cout != 0:
        split_list.append(out_str)
    return split_list


# hide split text in video frames
def encode_string(input_string, root="./tmp/"):
    split_string_list = split_string(input_string)
    for i in range(0, len(split_string_list)):
        f_name = "{}{}.png".format(root, i)
        # LSB-Steganography is a steganography technique in which we hide messages inside an image
        # by replacing Least significant bit of image with the bits of message to be hidden.
        secret_enc = lsb.hide(f_name, split_string_list[i])
        secret_enc.save(f_name)
        print("frame {} holds {}".format(f_name, split_string_list[i]))

# return original text data 
def decode_string():
    secret = []
    root = "./tmp/"
    for i in range(len(os.listdir(root))):
        f_name = "{}{}.png".format(root, i)
        secret_dec = lsb.reveal(f_name)
        if secret_dec == None:
            break
        secret.append(secret_dec)
    print("\nThe decoded text is: ")
    print(''.join([i for i in secret]))
    print("\n")



