# Review Classification model

This folder contains code (in file `DeBERTa_Inference.py`) to get output from our fine-tuned Review Classification model.

## Instructions for running the model

### Download Model Weights

- Download model weights of fine-tuned DeBERTa-base model from [here](https://data.mendeley.com/datasets/kyg8whhfkk/1).
- Place the model weights in folder ./DeBERTa


### Install requirements

The code is written in `Python3` and tested in `Python3.10`. The following python packages are the required dependencies

- `transformers`
- `torch`
- `nltk`
- `emoji`

### Run the code

To make the program straightforward, we didn't include any cmdline parameters.
- The input can be provided by replacing "WRITE_YOUR_INPUT_HERE" in line 87
- The model can be run using 
```
python3 DeBERTa_Inference.py
``` 
It will show the identified category in the stdout. 

### NOTES

- Make sure the directory "ReviewClassification" has following structure
```
ReviewClassification
│   README.md
│   DeBERTa_Inference.py   
│
└─── DeBERTa
    │   config.json
    │   generate_config.json
    │   ....
```