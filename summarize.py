import os
from openai import OpenAI
from vision import extract_text
import re
from dotenv import load_dotenv
import base64

load_dotenv()


def sort_key_func(file):
    """Extracts the page number from the file name for sorting."""
    match = re.search(r"page_(\d+)", file)
    return int(match.group(1)) if match else 0


def process_images_in_folder(folder_path):
    for root, dirs, _ in os.walk(folder_path):
        for dir in dirs:
            print(f"\n\n-------------------")
            print(f"Processing file {dir}")
            images_path = os.path.join(root, dir)
            images = [img for img in os.listdir(images_path) if img.endswith(".png")]
            sorted_images = sorted(images, key=sort_key_func)

            for image in sorted_images:
                image_path = os.path.join(images_path, image)
                with open(image_path, "rb") as image_file:
                    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
                print(f"\n    image {image}")
                print(f"        {extract_text(client, encoded_string, is_base64=True)}")


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
main_folder_path = "data/processed/Piemērs 1"
process_images_in_folder(main_folder_path)

# TODO: can we send all images as a one request? or there is not enough input context?