# Importing Modules

import cv2
import numpy as np

image = cv2.imread("/Users/swagatmohanty/Documents/Python 2/example 2.jpg")

# Exception Handling

if image is None:
    raise ValueError("Image not availabe")

# Give Variables

(h, w) = image.shape[:2]

start_point = (20, h // 2)
end_point = (w-2, h//2)

# Arrowed Line

cv2.arrowedLine(image, start_point, end_point, (0, 255, 0), 2, tipLength=0.03)
cv2.arrowedLine(image, start_point, end_point, (0, 255, 0), 2, tipLength=0.03)

# Lines

cv2.line(image, (20, h//2 - 20), (20, h//2 + 20), (0, 255, 0), 2)
cv2.line(image, (w-20, h//2 - 20), (w-20, h//2 + 20), (0, 255, 0), 2)

# Put Text

cv2.putText(image, f"Width {w} px", (w//2 - 100, h//2 - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8,(0, 255, 0), 2)

# Show all result

cv2.imshow("Width Measurement", image)
cv2.waitKey(0)
cv2.destroyAllWindows()