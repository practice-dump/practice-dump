from transformers import AutoFeatureExtractor

feature_extractor = AutoFeatureExtractor.from_pretrained("facebook/wav2vec2-base")

##This model is trained on 16K Sampling rate so we need to convert our signal to 16K sampling rate

from datasets import load_dataset, Audio

dataset = load_dataset("PolyAI/minds14", name="en-US", split="train")

dataset[0]["audio"]

'''
{'array': array([ 0.        ,  0.00024414, -0.00024414, ..., -0.00024414,
         0.        ,  0.        ], dtype=float32),
 'path': '/root/.cache/huggingface/datasets/downloads/extracted/f14948e0e84be6/en-US~JOINT_ACCOUNT/602ba55abb1e6d0fbce92065.wav',
 'sampling_rate': 8000}
'''

'''
array is the speech signal loaded - and potentially resampled - as a 1D array.
path points to the location of the audio file.
sampling_rate refers to how many data points in the speech signal are measured per second.
'''

dataset = dataset.cast_column("audio", Audio(sampling_rate=16000)) ## Changing sampling rate

##passing audio through feature extractor
audio_input = [dataset[0]["audio"]["array"]]
feature_extractor(audio_input, sampling_rate=16000) ## recommended to give sampling_rate as an argument to help in debug

def preprocess_function(examples):
    audio_arrays = [x["array"] for x in examples["audio"]]
    inputs = feature_extractor(
        audio_arrays,
        sampling_rate=16000,
        padding=True,
        max_length=100000,
        truncation=True,
    )
    return inputs
  
  processed_dataset = preprocess_function(dataset)


###########
##Custom Feature Extractor

from transformers import Wav2Vec2FeatureExtractor

w2v2_extractor = Wav2Vec2FeatureExtractor(sampling_rate=8000, do_normalize=False)
print(w2v2_extractor)
