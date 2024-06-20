# Theme Identification model

This folder contains code (in file `BART_Inference.py`) to get output from our fine-tuned theme identification model.

## Instructions for running the model

### Download Model Weights

- Download model weights of fine-tuned BART base model from [here](https://data.mendeley.com/datasets/kyg8whhfkk/1).
- Place the model weights in folder ./bart-base


### Install requirements

The code is written in `Python3` and tested in `Python3.10`. The following python packages are the required dependencies

- `transformers`
- `torch`
- `nltk`
- `emoji`

### Run the code

To make the program straightforward, we didn't include any cmdline parameters.
- The input can be provided by replacing "WRITE_YOUR_INPUT_HERE" in line 81 
- The model can be run using 
```
python3 BART_Inference.py
``` 
It will show the identified themes in the stdout. 

### NOTES

- Make sure the directory "ThemeIdentification" has following structure
```
ThemeIdentification
│   README.md
│   BART_Inference.py   
│
└─── bart-base
    │   config.json
    │   generate_config.json
    │   ....
```