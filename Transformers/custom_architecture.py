from transformers import DistilBertConfig

config = DistilBertConfig()
print(config)

'''
DistilBertConfig {
  "activation": "gelu",
  "attention_dropout": 0.1,
  "dim": 768,
  "dropout": 0.1,
  "hidden_dim": 3072,
  "initializer_range": 0.02,
  "max_position_embeddings": 512,
  "model_type": "distilbert",
  "n_heads": 12,
  "n_layers": 6,
  "pad_token_id": 0,
  "qa_dropout": 0.1,
  "seq_classif_dropout": 0.2,
  "sinusoidal_pos_embds": false,
  "transformers_version": "4.16.2",
  "vocab_size": 30522
}
'''

## Now we would like to have activation function relu and attention_dropout=0.4
my_config = DistilBertConfig(activation="relu", attention_dropout=0.4)
print(my_config)
'''
DistilBertConfig {
  "activation": "relu",
  "attention_dropout": 0.4,
  "dim": 768,
  "dropout": 0.1,
  "hidden_dim": 3072,
  "initializer_range": 0.02,
  "max_position_embeddings": 512,
  "model_type": "distilbert",
  "n_heads": 12,
  "n_layers": 6,from transformers import DistilBertModel

my_config = DistilBertConfig.from_pretrained("./your_model_save_path/config.json")
model = DistilBertModel(my_config)
  "pad_token_id": 0,
  "qa_dropout": 0.1,
  "seq_classif_dropout": 0.2,
  "sinusoidal_pos_embds": false,
  "transformers_version": "4.16.2",
  "vocab_size": 30522
}
'''

## Saving model config
my_config.save_pretrained(save_directory="./your_model_save_path")

## Reusing model
my_config = DistilBertConfig.from_pretrained("./your_model_save_path/config.json")

from transformers import DistilBertModel
model = DistilBertModel(my_config)

## Loading model above way initializes model using random weights and needs large amount of data so that it can be used
## Another way is load model using pretrained one and then changing architecture
model = DistilBertModel.from_pretrained("distilbert-base-uncased", config=my_config)



