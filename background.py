from rembg import remove
from PIL import Image

input_image_path = input("Enter the path of the image: ")

remover = Image.open(input_image_path)

output = remove(remover)

print("The path of the Output (No extension): ")
output_image_path = input("Enter <<: ")+".png"
output.save(output_image_path)

print(f"Background removed and saved as {output_image_path}")
