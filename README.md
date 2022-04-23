# Video steganography
 **It's a branch of data hiding, which is a technique that embeds messages into cover content which is Video in our case** 

**Files Types we wanna hide**
- TEXT - IMAGES

## logic
- **Data Encryption and Decryption using Cryptography algorithms**
- **Hiding these data in video for a higher level of security**

## Understanding the Process of Video Steganography

**Each time we deal with videos, we are actually dealing with the sequence of frames themselves. Each frame is just an image, which might be represented as an m    x n array of pixels, where (m,n) is picture size. Each pixel might be represented as colour intensity, depending on which colour model we are using (gray-      scale, RGB,BGR).**

## ABOUT THE CODE

- **Libraries for Python like cv2 and Stegano have been used.**
- **The library used in this process is stegano. This library makes use of the LSB (Least Significant Bit) technique.**
