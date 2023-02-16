from transformers import pipeline
## We are creating a generator

def data():
    for i in range(1000):
        yield f"My example {i}"


pipe = pipeline(model="gpt2", device=0)
generated_characters = 0
for out in pipe(data()):
    generated_characters += len(out[0]["generated_text"])

# KeyDataset is a util that will just output the item we're interested in.

from transformers.pipelines.pt_utils import KeyDataset
from datasets import load_dataset

pipe = pipeline(model="hf-internal-testing/tiny-random-wav2vec2", device=0)
dataset = load_dataset("hf-internal-testing/librispeech_asr_dummy", "clean", split="validation[:10]")
## Directly iterating over dataset

for out in pipe(KeyDataset(dataset, "audio")):
    print(out)
