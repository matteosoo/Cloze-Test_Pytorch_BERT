# Cloze-Test_Pytorch_BERT

## How to use?

* Download PyTorch:
  [Official PyTorch Website](http://pytorch.org/ "pytorch")
  
  or using command line:
  ```
  conda install pytorch torchvision -c pytorch
  # MacOS Binaries dont support CUDA, install from source if CUDA is needed
  ```

* With pip:
  ```
  pip install pytorch-pretrained-bert
  ```
  ```
  pip3 install --upgrade gensim
  ```

## Overview
Ten answers choices are given. Select the best answer to complete the sentence.
  
  * Example
  
    Create a text file and save in folder as follows:
    ```
    1 Longman , the third , looked at the others over his shoulder .
    2 Goldband , the fourth , had a gold sash round his waist ; and little Playman did nothing at all , and was the more proud .
    3 There was too much ostentation , and so I came away . '
    4 ` And now we are sitting and shining here ! '
    5 said the bit of bottle-glass .
    6 At that moment more water came into the gutter ; it streamed over the edges and washed the bit of bottle-glass away .
    7 ` Ah !
    8 now he has been promoted ! '
    9 said the Darning-needle . '
    10 I remain here ; I am too fine .
    11 But that is my pride , which is a sign of respectability ! '
    12 And she sat there very proudly , thinking lofty thoughts . '
    13 I really believe I must have been born a sunbeam , I am so fine !
    14 It seems to me as if the sunbeams were always looking under the water for me .
    15 Ah , I am so fine that my own mother can not find me !
    16 If I had my old eye which broke off , I believe I could weep ; but I ca n't -- it is not fine to weep ! '
    17 One day two street-urchins were playing and wading in the gutter , picking up old nails , pennies , and such things .
    18 It was rather dirty work , but it was a great delight to them .
    19 ` Oh , oh ! '
    20 cried out one , as he pricked himself with the Darning-needle ; ` he is a fine fellow though ! ' '
    21 I XXXXX not a fellow ; I am a young lady ! '	am		am|born|find|picking|pricked|said|sat|seems|streamed|thinking
    ```
    
  * Results
    

## Reference
  * BERT model: https://github.com/huggingface/pytorch-pretrained-BERT
  * gensim data: https://github.com/RaRe-Technologies/gensim-data
