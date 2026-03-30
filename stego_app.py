import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def display_image(image_data, title):
    """Helper function to show images cleanly."""
    plt.figure(figsize=(6, 6))
    plt.imshow(cv2.cvtColor(image_data, cv2.COLOR_BGR2RGB))
    plt.title(title, fontsize=14, fontweight='bold')
    plt.axis('off')
    plt.show()

def main():
    print("========================================")
    print("   IMAGE STEGANOGRAPHY APPLICATION")
    print("========================================")
    
    # 1. Get user input for file names
    cover_name = input("Enter the cover image file name (e.g., IMG_2826.jpeg): ")
    secret_name = input("Enter the secret image file name (e.g., IMG_2828.jpeg): ")

    # 2. Check if files exist before trying to open them
    if not os.path.exists(cover_name) or not os.path.exists(secret_name):
        print("\n❌ ERROR: One or both files not found. Please check the names and try again.")
        return

    # 3. Read images
    img1 = cv2.imread(cover_name)
    img2 = cv2.imread(secret_name)

    # 4. Process Images
    print("\nProcessing images...")
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # Encode (4-bit LSB)
    hidden = (img1 & 240) | (img2 >> 4)
    
    print("\n✅ Success! The secret image has been hidden inside the cover image.")
    display_image(hidden, "Hidden Image (Stego)")

    # 5. Extraction
    choice = input("\nDo you want to extract the secret image now? (y/n): ")
    if choice.lower() in ['y', 'yes']:
        extracted = (hidden & 15) << 4
        print("\n✅ Extracting...")
        display_image(extracted, "Extracted Secret Image")
    else:
        print("\nExiting application. Goodbye!")

if __name__ == "__main__":
    main()