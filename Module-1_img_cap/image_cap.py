import requests
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load BLIP model and processor
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load your image
img_path = "assets/sample.jpeg"  # Make sure this path exists
image = Image.open(img_path).convert('RGB')

# Prepare inputs and generate caption
inputs = processor(images=image, text="a photo of", return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=50)

# Decode and display caption
caption = processor.decode(outputs[0], skip_special_tokens=True)
print("Generated Caption:", caption)
