from PIL import Image

srcImageUrl = "/mnt/data/project1.jpg"
outputImageUrl = "/mnt/data/project1.webp"

# Load the JPEG images
img1 = Image.open("/mnt/data/project1.jpg")
img2 = Image.open("/mnt/data/project2.jpg")

# Convert and save as WEBP
img1.save("/mnt/data/project1.webp", "WEBP")
img2.save("/mnt/data/project2.webp", "WEBP")

# Provide the paths to the new files
"/mnt/data/project1.webp", "/mnt/data/project2.webp"
