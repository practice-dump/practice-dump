Parameter-Efficient Fine Tuning (PEFT) methods freeze the pretrained model parameters during fine-tuning and add a small number of trainable parameters (the adapters) on top of it. The adapters are trained to learn task-specific information. 

Adapters trained with PEFT are also usually an order of magnitude smaller than the full model, making it convenient to share, store, and load them.

### To Do
- [ ] PEFT documentation
- [ ] Read pprs on blog
