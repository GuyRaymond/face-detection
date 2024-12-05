import cv2
import os
from utils import detect_faces, draw_rectangles

def process_image(input_path, output_path):
    # Load the image
    image = cv2.imread(input_path)
    if image is None:
        raise FileNotFoundError(f"Input image not found at {input_path}")

    # Detect faces
    faces = detect_faces(image)

    # Draw rectangles around faces
    output_image = draw_rectangles(image, faces)

    # Save the processed image
    cv2.imwrite(output_path, output_image)

if __name__ == "__main__":
    INPUT_IMAGE = "images/input.jpg"
    OUTPUT_IMAGE = "images/output.jpg"
    process_image(INPUT_IMAGE, OUTPUT_IMAGE)
    print(f"Processed image saved at {OUTPUT_IMAGE}")
