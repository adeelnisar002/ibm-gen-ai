import os
import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load model
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

url = "https://en.wikipedia.org/wiki/IBM"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
img_elements = soup.find_all('img')

with open("1-image-captioning/captions.txt", "w") as f:
    for img_element in img_elements:
        img_url = img_element.get('src')
        if not img_url or 'svg' in img_url or '1x1' in img_url:
            continue
        if img_url.startswith('//'):
            img_url = 'https:' + img_url
        elif not img_url.startswith('http'):
            continue

        try:
            img_data = requests.get(img_url).content
            image = Image.open(BytesIO(img_data)).convert("RGB")

            if image.size[0] * image.size[1] < 400:
                continue

            inputs = processor(images=image, text="a photo of", return_tensors="pt")
            outputs = model.generate(**inputs, max_new_tokens=50)
            caption = processor.decode(outputs[0], skip_special_tokens=True)
            f.write(f"{img_url}: {caption}\n")
        except Exception as e:
            print(f"Error with image {img_url}: {e}")
