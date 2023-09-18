There are two types of sampling 
* Greedy Sampling: In this the most probable word is choosen, but sometimes it enters into repetative word loop
* Random Sampling: In this words at random are chosen according to probability distribution, but in this way coherence is not there

  So to have something between we have some **hyperparmeters**

  * top_p: It is the probability which is threshold for cumulative probability and words at random are selected from this list
  * top_k: It is the number of top k words chosen and words at random are chosen from this list according to probability
 
    Other Hyperparametes that are written to control text generation
    
  * Max_new_tokens: The maximum tokens an AI model can generate.
  * Temperature: It controls the distribution of output words.
  
    * Low temperature ==> More concentrated distribution==> Less randomness
    * High temperature ==> diluted distribution==> More randomness

- [ ] Add more parameters from chatgpt api
