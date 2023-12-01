from PIL import Image
import os

def resize_images(input_folder, output_folder, target_size):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)

    for file in files:
        # Check if the file is an image (you may want to add more image file extensions)
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            # Open the image
            image_path = os.path.join(input_folder, file)
            img = Image.open(image_path)

            # Resize the image
            resized_img = img.resize(target_size)

            # Save the resized image to the output folder
            output_path = os.path.join(output_folder, file)
            resized_img.save(output_path)

if __name__ == "__main__":
    # Set the input and output folders, and the target size
    input_folder = "C:/Users/Aluno/Desktop/Python- FAVOR NÃO APAGAR/Streamlit/Trabalho_final"
    output_folder = "C:/Users/Aluno/Desktop/Python- FAVOR NÃO APAGAR/Streamlit/Trabalho_final/imagem"
    target_size = (400, 400)  # Set your desired target size

    # Call the function to resize images
    resize_images(input_folder, output_folder, target_size)
