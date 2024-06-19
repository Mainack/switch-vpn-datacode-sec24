# Importing required packages

import re
import os
import emoji
import nltk
import string
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
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
    model_inputs = tokenizer(inputs, max_length=max_input_length, truncation=True, return_tensors="pt")

    return model_inputs

def get_output(text):
    text_input = preprocess_data(text)
    with torch.no_grad():
        logits = model(text_input['input_ids'].to(device)).logits

    predicted_class_id = logits.argmax().item()
    return predicted_class_id

if __name__ ==  '__main__':
    max_input_length = 512
    max_target_length = 64

    # Initializing the models

    cwd = os.getcwd()
    model_checkpoint = f"{cwd}/ReviewClassification/DeBERTa"

    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
    model = AutoModelForSequenceClassification.from_pretrained(model_checkpoint, num_labels=3)

    model.to(device)
    model.eval()

    num_label_dict = {
        0 : "irrelevant",
        1 : "potential shift",
        2 : "actual shift"
    }

    input = "WRITE_YOUR_INPUT_HERE"

    output = num_label_dict[get_output(input)]
    print(f"The provided review '{input}' is categorised as : {output}")