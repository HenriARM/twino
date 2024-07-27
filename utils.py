import fitz  # PyMuPDF
from io import BytesIO


def is_scanned_pdf(pdf_bytes: bytes) -> bool:
    """
    Checks if a PDF file is likely a scanned document.

    Args:
        pdf_bytes (str): The PDF file as bytes.

    Returns:
        bool: True if the PDF is likely a scanned document, False otherwise.
    """
    # Open the PDF file
    pdf_document = fitz.open("pdf", pdf_bytes)

    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text = page.get_text()

        # If any page contains text, it's not a scanned document
        if text.strip():
            return False

    # If no text is found on any page, it's likely a scanned document
    return True


def pdf_to_images(pdf_bytes: bytes, folder_name: str) -> None:
    """
    Converts each page of a PDF file to an image and uploads the images to an S3 bucket.

    Args:
        pdf_bytes (bytes): The PDF file as bytes.
        bucket_name (str): The name of the S3 bucket.
        folder_name (str): The folder name within the S3 bucket.
        s3_client (BaseClient): The initialized S3 client.
    """
    # Open the PDF file
    pdf_document = fitz.open("pdf", pdf_bytes)

    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap()  # Render page to an image

        # Save the image to an in-memory bytes buffer
        img_buffer = BytesIO()
        img_buffer.write(pix.tobytes("png"))
        img_buffer.seek(0)

        # Create a unique object name
        object_name = f"{folder_name}/page_{page_num + 1}.png"

        # upload image locally
        with open(object_name, "wb") as file:
            file.write(img_buffer.read())


def extract_images_from_pdf(pdf_bytes: bytes, folder_name: str) -> None:
    """
    Extracts images from a PDF and uploads them directly to an S3 bucket.

    Args:
        pdf_bytes (bytes): The PDF file as bytes.
        bucket_name (str): The name of the S3 bucket.
        folder_name (str): The folder name within the S3 bucket.
        s3_client (BaseClient): The initialized S3 client.
    """
    pdf_document = fitz.open("pdf", pdf_bytes)
    image_count = 0

    # Iterate through each page
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        images = page.get_images(full=True)

        # Extract and upload each image
        for img in images:
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_extension = base_image["ext"]

            # Create a unique object name
            object_name = f"{folder_name}/page_{page_num + 1}_image_{image_count + 1}.{image_extension}"

            # upload image locally
            with open(object_name, "wb") as file:
                file.write(image_bytes)

            image_count += 1

    print(f"Extracted and uploaded {image_count} images from the PDF")
