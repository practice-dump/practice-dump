from datasets import load_dataset

lj_speech = load_dataset("lj_speech", split="train")

lj_speech = lj_speech.map(remove_columns=["file", "id", "normalized_text"]) ## Removing additional columns

lj_speech = lj_speech.cast_column("audio", Audio(sampling_rate=16000)) ## making sampling rate as we require for our processor

from transformers import AutoProcessor

processor = AutoProcessor.from_pretrained("facebook/wav2vec2-base-960h")

def prepare_dataset(example): ##function to process the audio data contained in array to input_values, and tokenize text to labels.
    audio = example["audio"]

    example.update(processor(audio=audio["array"], text=example["text"], sampling_rate=16000))

    return example

prepare_dataset(lj_speech[0])


'''
'input_values': [array([-6.6753007e-03, -7.9126023e-03, -7.1924743e-03, ...,
          7.1743531e-03,  1.4386778e-03, -2.2044291e-05], dtype=float32)],
 'labels': [23,3,3,3,3,31,2] ## Changed values to just show output
'''
