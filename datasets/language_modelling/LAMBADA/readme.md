The LAMBADA evaluates the capabilities of computational models for text understanding by means of a word prediction task. LAMBADA is a collection of narrative passages sharing the characteristic that human subjects are able to guess **their last word** if they are exposed to the whole passage, but not if they only see the last sentence preceding the target word. To succeed on LAMBADA, computational models cannot simply rely on local context, but must be able to keep track of information in the broader discourse.

The LAMBADA dataset is extracted from BookCorpus and consists of 10022 passages, divided into 4869 development and 5153 test passages. The training data for language models to be tested on LAMBADA include the full text of 2662 novels (disjoint from those in dev+test), comprising 203 million words.

P.S When it was released in 2016: We show that LAMBADA exemplifies a wide range of linguistic phenomena, and that none of several state-of-the-art language models reaches accuracy above 1% on this novel benchmark.
We thus propose LAMBADA as a challenging test set, meant to encourage the development of new models capable of genuine understanding of broad context in natural language text.

Important links

* [Research PPR](https://arxiv.org/pdf/1606.06031.pdf)
* [Hugging face](https://huggingface.co/datasets/lambada)
