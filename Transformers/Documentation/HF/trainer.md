Trainer has these arguments

* model : name of model name
* args : TrainerArguments
* data_collator : Used to form batch from a list of elements of train_dataset or eval_dataset.
* train_dataset : Training Dataset
* eval_dataset : Validation Dataset
* tokenizer : tokenizer
* model_init : A different way to initate model, "A function that instantiates the model to be used. If provided, each call to train() will start from a new instance of the model as given by this function."
* compute_metrics : function used to calculate metrics
* callbacks : list of callbacks to customize the training loop
* optimizers :  A tuple containing the optimizer and the scheduler to use. Would default to AdamW and get_linear_schedule_with_warmup()
* preprocess_logits_for_metrics : (This is new for me) " A function that preprocess the logits right before caching them at each evaluation step. Must take two tensors, the logits and the labels, and return the logits once processed as desired. The modifications made by this function will be reflected in the predictions received by compute_metrics.
Note that the labels (second parameter) will be None if the dataset does not have them."
