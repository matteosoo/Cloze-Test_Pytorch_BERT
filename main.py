import torch
from pytorch_pretrained_bert import BertTokenizer, BertForMaskedLM
import gensim.downloader as api
import time
import sys

# load data
desk = input("Please input the location of the data file: "'\n')
filename = input("Please input the name of the data file: "'\n')
f = open(desk + filename, "r",encoding='UTF-8')
list = f.readlines()[0:21]

start_time = time.time()

for i in range(len(list)):
    list[i] = list[i].strip()
list[20] = list[20].split('\t',3)
list[20][0] = list[20][0].replace("XXXXX","_")
pre_text = ''
for i in range(20):
    pre_text+= list[i]+' '
target_text = list[20][0]
choices = list[20][3].split("|")

print(pre_text,'\n',target_text,'\n',choices,'\n')

# Load pre-trained model with masked language model head
bert_version = 'bert-large-uncased'
model = BertForMaskedLM.from_pretrained(bert_version)

# Preprocess text
text = pre_text + target_text

# Prevent RuntimeError
if len(text)>2000:
  pre_text = ''
  for i in range(10,20):
    pre_text += list[i]+' '
  text = pre_text + target_text
  print('After decreasing the sentences... ''\n')

tokenizer = BertTokenizer.from_pretrained(bert_version)
tokenized_text = tokenizer.tokenize(text)
mask_positions = []
for i in range(len(tokenized_text)):
    if tokenized_text[i] == '_':
        tokenized_text[i] = '[MASK]'
        mask_positions.append(i)

# Predict missing words from left to right
model.eval()
predicted_token = ''
for mask_pos in mask_positions:
    # Convert tokens to vocab indices
    token_ids = tokenizer.convert_tokens_to_ids(tokenized_text)
    tokens_tensor = torch.tensor([token_ids])
    # print('tokens_tensor: ''\n',tokens_tensor)
    # Call BERT to predict token at this position
    try:
      predictions = model(tokens_tensor)[0, mask_pos]
    except RuntimeError:
      sys.exit('Oops! Sorry for your input 1-20 articles are too long. Try to decrease your sentences.')
    else:
      predictions = model(tokens_tensor)[0, mask_pos]
    # print("type.predictions:",type(predictions))
    # print("predictions:"'\n',predictions)
    predicted_index = torch.argmax(predictions).item()
    # print('predicted_index''\n',predicted_index)
    predicted_token = tokenizer.convert_ids_to_tokens([predicted_index])[0]
    print('predicted_token:''\n',predicted_token)
    
    # for i in range(10):
    #   predicted_token1 = tokenizer.convert_ids_to_tokens([predicted_index-i])[0]
    #   print('predicted_token(+1):',predicted_token1)
    
    # Update text
    tokenized_text[mask_pos] = predicted_token

for mask_pos in mask_positions:
    tokenized_text[mask_pos] = "_" + tokenized_text[mask_pos] + "_"
result = ' '.join(tokenized_text).replace(' ##', '').replace(pre_text,'')

result21 = target_text.replace('_',tokenized_text[mask_pos])
print('After predicting: ''\n', result21)

answer_number = -1
for answer_index in range(10):
  # use word2vec to find the most similar answer if the prediction is not in the selection
  if  predicted_token in choices:
    if predicted_token == choices[answer_index]:
      answer_number = answer_index
      break
  else:
    info = api.info()
    model = api.load("word2vec-google-news-300")
    similarity_list = []
    for similarity_index in range(10):
      try:
        similarity = model.similarity(predicted_token,choices[similarity_index])
      except KeyError:
        similarity = 0.0000000001
      else:
        similarity = model.similarity(predicted_token,choices[similarity_index])
        similarity = similarity.item() #.item(): convert np.float to float type
      similarity_list.append(similarity)
    print('similarity_list: ''\n',similarity_list)
    most_similar = max(similarity_list)
    most_similar_index = similarity_list.index(max(similarity_list))
    print('Most similar answer is: ''\n',most_similar_index+1,' ',choices[most_similar_index],' ',most_similar)
    
    answer_number = most_similar_index
    predicted_token = choices[most_similar_index]
    break
    
print('The Answer is: ''\n', answer_number+1,' ', predicted_token)

print("--- %s seconds ---" % (time.time() - start_time))