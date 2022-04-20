from hidingImage import image
from hidingText import Text


def hideImage():
    frame_count = image.frame_extraction(input("Enter Video path name"))
    image.encode_video(input("Enter Image path name"), frame_count)


def hideTxt():
    while True:
        print("1.Hide a message in video\t2.Reveal the secret from video")
        print("any other value to exit")
        choice = input()
        if choice == '1':
            input_string = input("Enter the input string :")
            f_name = input("Enter the name of the video: ")
            Text.frame_extraction(f_name)
            Text.encode_string(input_string)
        elif choice == '2':
            Text.decode_string(input("enter the name of video with extension: "))
        else:
            break


print("1- Text\n2- Image\n3- Video")
c = int(input("Select file type from 1 to 3 : "))

if c == 1:
    hideTxt()
elif c == 2:
    hideImage()
elif c == 3:
    pass
else:
    print("Invalid Number!!")
