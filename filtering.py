import cv2
import numpy as np
import matplotlib.pyplot as plt

def display_image(title, image):
    plt.figure(figsize= (8,8))
    if len(image.shape) == 2:
        plt.imshow(image, cmap= 'gray')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    
    plt.title(title)
    plt.axis("off")
    plt.show()

def interactive_edge_detection(image_path):
        image = cv2.imread(image_path)
        if image is None:
            print("Image Not Found!")
            return
        
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        display_image("Orignal Grayscale Image", gray_image)

        print("Select an option (1-6)")
        print("1. Sobel Edge Detection")
        print("2. Canny Edge Detection")
        print("3. Laplacian Edge Detection")
        print("4. Gaussian Smoothing")
        print("5. Median Filtering")
        print("6. Exit")

        while True:
            choice = input("Enter your choice (1-6): ")
            
            if choice == '1':
                sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize= 3)
                sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize= 3)
                combined_sobel = cv2.bitwise_or(sobel_x.astype(np.uint8), sobel_y.astype(np.uint8))
                display_image("Sobel Edge Detection", combined_sobel)

            elif choice == '2':
                print("Adjust Threshold For Canny (Default 100-200): ")
                lt = int(input("Enter lower threshold: "))
                ut = int(input("Enter upper threshold: "))
                edges = cv2.Canny(gray_image, lt, ut)
                display_image("Canny Edge Detection", edges)

            elif choice == '3':
                laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
                display_image("Laplacian Edge Detection", np.abs(laplacian).astype(np.uint8))

            elif choice == '4':
                print("Adjust Kernel Size for Gaussian Blur (Must be Odd!, Default = 5): ")
                k = int(input("Enter Kernel Size (odd number): "))
                blur = cv2.GaussianBlur(image, (k, k), 0)
                display_image("Gaussian Smoothing", blur)

            elif choice == '5':
                print("Adjust Kernel Size for Median Filtering (Must be Odd!, Default = 5): ")
                k = int(input("Enter Kernel Size (odd number): "))
                median_filtered = cv2.medianBlur(image, k)
                display_image("Median Filtering", median_filtered)

            elif choice == '6':
                print("Exiting...")
                break

            else: 
                print("Invalid Choice")

interactive_edge_detection('/Users/swagatmohanty/Documents/Python 2/example 3.jpg')