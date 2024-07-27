import os

from utils import is_scanned_pdf, pdf_to_images, extract_images_from_pdf


folder_path = "data/Piemērs 1"
processed_folder_path = "data/processed/Piemērs 1"

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


# TODO: Spring 2016 doesn't work well (2nd page shows images which are not there and is_scan should run on each page)
# TODO: how to detect image extracted is a text or just some small logo?
# TODO: Error in 2nd Example "Processing file: sllaries from Orange for the last 12 months_Redacted.pdf MuPDF error: format error: cmsOpenProfileFromMem failed"
# TODO: 3d Example - input can also be straight up image or scan can consist .jpx format image