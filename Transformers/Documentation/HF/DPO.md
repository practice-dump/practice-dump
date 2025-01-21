<details open>
  <summary> <h2>Introduction</h2></summary>
  
 
Direct Preference Optimization (DPO) simplifies preference alignment by directly optimizing models using preference data. This approach eliminates the need for **separate reward models** and complex reinforcement learning, making it more stable and efficient than traditional Reinforcement Learning from Human Feedback (RLHF).

</details>
<details open>
    <summary> <h2>Understanding DPO</h2></summary>
</details>

DPO recasts preference alignment as a classification problem on human preference data. Traditional RLHF approaches require training a separate reward model and using complex reinforcement learning algorithms like PPO to align model outputs. DPO simplifies this process by defining a loss function that directly optimizes the model's policy based on preferred vs non-preferred outputs.

<details>
  <summary> <h2>How does the DPO work</h2></summary>
The DPO process requires supervised fine-tuning (SFT) to adapt the model to the target domain. This creates a foundation for preference learning by training on standard instruction-following datasets. The model learns basic task completion while maintaining its general capabilities.

Next comes preference learning, where the model is trained on pairs of outputs - one preferred and one non-preferred. The preference pairs help the model understand which responses better align with human values and expectations.

The core innovation of DPO lies in **its direct optimization approach**. Rather than **training a separate reward model**, **DPO uses a binary cross-entropy loss to directly update the model weights based on preference data**. This streamlined process makes training more stable and efficient while achieving comparable or better results than traditional RLHF.

One can find a collection of DPO datasets on Hugging Face [here](https://huggingface.co/collections/argilla/preference-datasets-for-dpo-656f0ce6a00ad2dc33069478).

The first step is to train an SFT model, to ensure the data we train on is in-distribution for the DPO algorithm.

Then, fine-tuning a language model via DPO consists of two steps and is easier than PPO:

1) Data collection: Gather a preference dataset with positive and negative selected pairs of generation, given a prompt.
2) Optimization: Maximize the log-likelihood of the DPO loss directly.

</details>

<details>
    <summary> <h2>Implementation with TRL</h2></summary>

The Transformers Reinforcement Learning (TRL) library makes implementing DPO straightforward. The `DPOConfig` and `DPOTrainer` classes follow the same `transformers` style API.
Here's a basic example of setting up DPO training:

```python
from trl import DPOConfig, DPOTrainer

# Define arguments
training_args = DPOConfig(
    ...
)

# Initialize trainer
trainer = DPOTrainer(
    model,
    train_dataset=dataset,
    tokenizer=tokenizer,
    ...
)

# Train model
trainer.train()
```

The DPOTrainer supports both conversational and standard dataset format. When provided with a conversational dataset, the trainer will automatically apply the chat template to the dataset.

Although the DPOTrainer supports both explicit and implicit prompts, we recommend using explicit prompts. If provided with an implicit prompt dataset, the trainer will automatically extract the prompt from the "chosen" and "rejected" columns.

</details>

<details>
    <summary> <h2>Best Practices</h2></summary>
Data quality is crucial for successful DPO implementation. The preference dataset should include diverse examples covering different aspects of desired behavior. Clear annotation guidelines ensure consistent labeling of preferred and non-preferred responses. You can improve model performance by improving the quality of your preference dataset. For example, by filtering down larger datasets to include only high quality examples, or examples that relate to your use case.

During training, carefully monitor the loss convergence and validate performance on held-out data. The beta parameter may need adjustment to balance preference learning with maintaining the model's general capabilities. Regular evaluation on diverse prompts helps ensure the model is learning the intended preferences without overfitting.

Compare the model's outputs with the reference model to verify improvement in preference alignment. Testing on a variety of prompts, including edge cases, helps ensure robust preference learning across different scenarios.

</details>

<details>
    <summary> <h2>Logging Metrics</h2></summary>

While training and evaluating we record the following reward metrics:

* rewards/chosen: the mean difference between the log probabilities of the policy model and the reference model for the chosen responses scaled by beta
* rewards/rejected: the mean difference between the log probabilities of the policy model and the reference model for the rejected responses scaled by beta
* rewards/accuracies: mean of how often the chosen rewards are > than the corresponding rejected rewards
* rewards/margins: the mean difference between the chosen and corresponding rejected rewards

</details>

<details>
    <summary> <h2>Loss Function</h2></summary>
    
The DPO algorithm supports several loss functions. The loss function can be set using the loss_type parameter in the DPOConfig. 

### Label smoothing

The cDPO is a tweak on the DPO loss where we assume that the preference labels are **noisy** with some probability. In this approach, the **label_smoothing** parameter in the DPOConfig is used to **model the probability of existing label noise**. To apply this conservative loss, set label_smoothing to a value greater than 0.0 (between 0.0 and 0.5; the default is 0.0).

</details>
