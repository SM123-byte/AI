# This code doesn't work as I'm not able to get OpenCv and therefore I don't know whether the code is correct

import cv2 
import colorama
from colorama import Fore, Style

def resize(image_path):
    image = cv2.imread(image_path)

    if image is None:
        print(Fore.RED + "ERROR: This file can't seem to open!")
        return
    
    size =  {

       "small": (300, 200),
       "medium": (800, 600),
       "large":  (1280, 720)
    }
    
    for label, dim in size.items():
        resized = cv2.resize(image, dim, interpolation=cv2.INTER_LINEAR)

        window_name = f"Resized - {label} ({dim[0]}x{dim[1]})" 
        cv2.imshow(window_name, resized)

        filename = f"resized_{label}.jpg"
        cv2.imwrite(filename, resized)
        print(f"Saved: {filename}")

    print("Press any key on an image window to close")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    resize("/Users/swagatmohanty/Documents/Python/Images/example.jpg")