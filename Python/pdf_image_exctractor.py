# Extracts Images from PDF
import fitz  # PyMuPDF
import PIL.Image  # pillow
import io


pdf = fitz.open("Electronic_Waste_Reduction_Through_Devices_and_Printed_Circuit_Boards_Designed_for_Circularity.pdf")
counter = 1
for i in range(len(pdf)):
    page = pdf[i]
    images = page.get_images()
    for image in images:
        base_img = pdf.extract_image(image[0])
        image_data = base_img['image']
        img = PIL.Image.open(io.BytesIO(image_data))
        ext = base_img['ext']
        img.save(open(f"img/image{counter}.{ext}", "wb"))
        counter += 1
