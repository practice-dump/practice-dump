#Loading tokenizer using Autotokenizer module
## Converts text to integers
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

sequence = "In a hole in the ground there lived a hobbit."
print(tokenizer(sequence))

##It will return three components
#{'input_ids': [101, 1999, 1037, 4920, 1999, 1996, 2598, 2045, 2973, 1037, 7570, 10322, 4183, 1012, 102], ## This contains id to remap tokens
##from ids to string
# 'token_type_ids': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ## Signfies whether sentence is A or B (remember BERT pretraing)
# 'attention_mask': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]} ## Signifies whether the token is here or this just padding

#Loading ImageProcesser using AutoImageProcessor module
## For vision tasks, an image processor processes the image into the correct input format.

from transformers import AutoImageProcessor

image_processor = AutoImageProcessor.from_pretrained("google/vit-base-patch16-224")

# Loading feature extractor using AutoFeatureExtractor module
##For audio tasks, a feature extractor processes the audio signal the correct input format.
from transformers import AutoFeatureExtractor

feature_extractor = AutoFeatureExtractor.from_pretrained(
    "ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition")

# Loading Processor using AutoProcessor module
## Multimodal tasks require a processor that combines two types of preprocessing tools. For example, the LayoutLMV2 model
##requires an image processor to handle images and a tokenizer to handle text; a processor combines both of them.
from transformers import AutoProcessor

processor = AutoProcessor.from_pretrained("microsoft/layoutlmv2-base-uncased")

