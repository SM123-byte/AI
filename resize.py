import cv2

image = cv2.imread('/Users/swagatmohanty/Documents/Python/Images/example.jpg')
cv2.resizeWindow('loaded image', 800, 500)

cv2.imshow('loaded image', image)
cv2.waitKey(0)  # Wait for a key press
cv2.destroyAllWindows()  # Close the window

# Print image properties
print(f"Image Dimensions: {image.shape}")  # Height, Width, Channels