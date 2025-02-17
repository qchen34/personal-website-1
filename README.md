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

But if you tried to go to my website/projects, and clicked generate on some of the pre-trained models, you will find that the generated text is not that good. It was able to generate some words that is English, but you will find that the text is not coherent and sometimes it even generate some gibberish.

This is mainly due to the way of training the model, as a beginner, I started training the model in a easy way, which is on character level. 


## Project 2
The second project is a text generation tool mainly for pyschologyical therapy purpose. I have found that many young people are suffering from anxiety and depression, in the past few years, technology has developed in a very fast pace, while many students are pursuing a career in the tech industry, focusing on the "stem" subjects, yet lack the education or resources to learn about the humanistic side of the world. 

The second project will implement a state-of-the-art text generation model, and fine tune it based on the psychological datas that I have collected. So that it can be used to generate daily psychological therapy text. 

The main reason that I decided not to build a chatbot is due to cost issues, as you may all know that supporting the server of a LLM chatbot is very expensive. 

The steps of building this project is as follows:
1. Load the pre-trained models from huggingface.
2. Fine-tune the model based on the psychological datas.
