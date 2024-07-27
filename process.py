import os

from utils import is_scanned_pdf, pdf_to_images, extract_images_from_pdf


folder_path = "data/Piemērs 1"
processed_folder_path = "processed"

for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        print(f"Processing file: {filename}")
        file_path = os.path.join(folder_path, filename)
        with open(file_path, "rb") as file:
            file_bytes = file.read()

        # Remove .pdf extension
        output_folder = os.path.join(processed_folder_path, filename[:-4])
        os.makedirs(output_folder, exist_ok=True)

        if is_scanned_pdf(file_bytes):
            extract_images_from_pdf(file_bytes, output_folder)
        else:
            pdf_to_images(file_bytes, output_folder)


# TODO: Spring 2016 doesn't work well
# TODO: put into processed/Piemers1 processed/Piemers2 processed/Piemers3
