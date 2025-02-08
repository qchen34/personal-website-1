# Personal Website Project

This project is a personal website project that aimed to showcase my projects and share my thoughts.
I will update the website as I build more projects. 

After the basic infrastructure is complete, I will make my website public with the domain https://chenqiwei.org 

P.S. I am not a professional developer, so my code looks like crap, any suggestions will be taken into consideration to improve my code for better understanding for sharing and community use.

## Project Structure

- **Backend**: A Flask server that handles model training and text generation.
- **Frontend**: A React application that provides the user interface.

## Project 1
The first project is simply a generator for shakespeare's text using nanoGPT. Thanks to https://github.com/karpathy/nanoGPT for the implementation. Credits to him for the nanoGPT code.

The main idea here for training is to first identify all the characters in the Shakespeare's text, then train the model on the characters. 

Based on karpathy's code, anyone can try to train the model based on shakespeare's text. 
1. run the prepare.py to get the train.bin, val.bin, and meta.pkl
2. run the run_training.py to train the model
3. Then run the sample.py to generate the text

The process of building this web app around the first project:
1. a frontend react-app to handle the requests from the webpage. which is generate_text.js.
2. a backend flask-app to handle the requests and output the generated text.

The original idea is to build a web app that allows users who don't know how to code to start toying with the parameters of the model, to get different pre-trained models and see the difference of the generated text. But obviously, this is not a cost-effective solution, it will cost a ton for a free project to rent a cloud based server to host the training and sampling process. With the parameter provided by claude 3.5, it takes my MBP M1 hours to train a model.

So the idea has changed to just showcase the result of the trained model's generated text. 

in the 2nd phase, I wanted to collect some data of my own, and train a Jordan Peterson's text generator. I valued Dr. Peterson's idea a lot, so I think it would be beneficial for people to see his suggestion or words of wisdom once in a while.


## Project 2
The second project is a chatbot that uses Deepseek API to simulate a therapy session. Aimming to imitate Jordan Peterson's philosophy in traditional and modern psychology on solving real-world probelms.