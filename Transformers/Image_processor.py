from datasets import load_dataset

dataset = load_dataset("food101", split="train[:100]")

from transformers import AutoImageProcessor

image_processor = AutoImageProcessor.from_pretrained("google/vit-base-patch16-224")

##Image Augmentation is being done to make model robust and less prone to overfitting

from torchvision.transforms import RandomResizedCrop, ColorJitter, Compose

size = (
    image_processor.size["shortest_edge"]
    if "shortest_edge" in image_processor.size
    else (image_processor.size["height"], image_processor.size["width"])
)

_transforms = Compose([RandomResizedCrop(size), ColorJitter(brightness=0.5, hue=0.5)])

## Image Processing

def transforms(examples):
    images = [_transforms(img.convert("RGB")) for img in examples["image"]]
    examples["pixel_values"] = image_processor(images, do_resize=False, return_tensors="pt")["pixel_values"] 
    ## do_resize is kept as false as it has been already taken care while performing augmentation
    
    return examples

  dataset.set_transform(transforms) ## Doing preprocessing along with augmentation
  
  ## Just for Visualizing
  dataset[0].keys()
  ## (['image', 'label', 'pixel_values'])
  ## Model accepts 'pixel_values' as inputs
  
  import numpy as np
import matplotlib.pyplot as plt

img = dataset[0]["pixel_values"]
plt.imshow(img.permute(1, 2, 0))
