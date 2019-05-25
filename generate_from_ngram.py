#!/usr/bin/env python3
import model
import random, sys

def generate(size, model_collection):
    model_data = model_collection.get_model(size).ngrams
    if size == 1:
        focus = '<s>'
        sentence = '<s>'
        while('</s>' not in focus):
            select = random.random()
            generated = ''
            for prob in model_data:
                if select < prob:
                    break
                else:
                    generated = model_data[prob]

            if (focus == '<s>' and generated == '<\s>') or generated == '<s>':
                continue
            else:
                sentence += f' {generated}'
                focus = generated
        return sentence

# Execution 

dickens = model.Model_Collection('data/examples/dickens_model.txt')

print("unigram sentences")
print(generate(1, dickens))


                

