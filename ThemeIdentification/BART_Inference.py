# Importing required libraries

import os
import re
import emoji
import nltk
import string
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from sklearn.metrics import *

nltk.download('punkt')

# If there's a GPU available...
if torch.cuda.is_available():

    # Tell PyTorch to use the GPU.
    device = torch.device("cuda")

    print('There are %d GPU(s) available.' % torch.cuda.device_count())

    print('We will use the GPU:', torch.cuda.get_device_name())

# If not...
else:
    print('No GPU available, using the CPU instead.')
    device = torch.device("cpu")


def re_sub(pattern, repl,text):
    return re.sub(pattern, repl, text)

def preprocess_sent(sent):
    sent = re.sub(r"http\S+", "", sent)
    sent = re.sub(r"@\S+", "@user", sent)

    # print(sent)
    sent = re_sub(r"[-+]?[.\d]*[\d]+[:,.\d]*", "",sent)
    sent = emoji.demojize(sent)
    sent = re_sub(r"[:\*]", " ",sent)
    return sent

def clean_text(text):
  sentences = nltk.sent_tokenize(text.strip())
  sentences_cleaned = [s for sent in sentences for s in sent.split("\n")]
  sentences_cleaned_no_titles = [preprocess_sent(sent) for sent in sentences_cleaned
                                 if len(sent) > 0 and
                                 sent[-1] in string.punctuation]
  text_cleaned = "\n".join(sentences_cleaned_no_titles)
  return text_cleaned

def preprocess_data(text):
    prefix = "summarize: "

    texts_cleaned = clean_text(text)
    inputs = prefix + texts_cleaned
    return inputs

def get_output(text):
    text = [preprocess_data(t) for t in text]
    input_ids = tokenizer(text, max_length = max_input_length, truncation=True, padding=True, return_tensors="pt").input_ids

    outputs = model.generate(input_ids.to(device), max_new_tokens = max_target_length)

    decoded_preds = tokenizer.batch_decode(outputs, skip_special_tokens=True)

    return {"content" : text, "themes" : decoded_preds}

if __name__ == '__main__':
    max_input_length = 1024
    max_target_length = 1024

    # Initializing the models
    # To get output of BART model on theme identification task replace the following path with actual model weights
    cwd = os.getcwd()
    model_checkpoint = f"{cwd}/ThemeIdentification/bart-base/"

    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)
    model.to(device)
    model.eval()

    input = "WRITE_YOUR_INPUT_HERE"

    output = get_output(input)["themes"]
    output = list(set(output))
    print(f"Themes identified in the review : {input} are : \n {output}")