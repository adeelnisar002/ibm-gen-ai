import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# Load model and processor
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Define caption function
def caption_image(input_image: np.ndarray):
    raw_image = Image.fromarray(input_image).convert("RGB")
    inputs = processor(images=raw_image, text="a photo of", return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=50)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption

# Launch Gradio UI
iface = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(),
    outputs="text",
    title="Image Captioning App",
    description="Upload an image to generate a caption using the BLIP model."
)

iface.launch()
