#!/usr/bin/env python3
import model
import random, sys

def generate(size, model_collection, single = False):
    model_data = model_collection.get_model(size).ngrams
    if size == 1:
        focus = '<s>'
        sentence = '<s>'
        while('</s>' not in focus):
            select = random.random()
            generated = ''
            hold_prob = 0
            for prob in model_data:
                if select >= prob and hold_prob <= prob:
                    generated = model_data[prob]
                    hold_prob = prob

            if (focus == '<s>' and generated == '<\s>') or generated == '<s>':
                continue
            elif single:
                return generated
            else:
                sentence += f' {generated}'
                focus = generated
                hold_prob = 0

        return sentence

    else:
        focus = generate(size - 1, model_collection, True)
        sentence = f'<s> {focus}'
        while('</s>' not in focus):
            select = random.random()
            generated = ''
            hold_prob = 0
            for prob in model_data[focus]:
                if select >= prob and hold_prob <= prob:
                    generated = model_data[focus][prob]
                    hold_prob = prob

            if single:
                return focus + ' ' + generated
            else:
                sentence += f' {generated}'
                if size == 2:
                    focus = generated
                else:
                    focus = ' '.join(focus.split()[1:]) + ' ' + generated
                hold_prob = 0

        return sentence

# Execution 
if __name__ == '__main__':
    models = model.Model_Collection(sys.argv[1])

    content = "\\1grams:\n"
    content += generate(1, models) + '\n'
    content += generate(1, models) + '\n'
    content += generate(1, models) + '\n'
    content += generate(1, models) + '\n'
    content += generate(1, models) + '\n'
    content += '\n'

    content += "\\2grams:\n"
    content += generate(2, models) + '\n'
    content += generate(2, models) + '\n'
    content += generate(2, models) + '\n'
    content += generate(2, models) + '\n'
    content += generate(2, models) + '\n'
    content += '\n'

    content += "\\3grams:\n"
    content += generate(3, models) + '\n'
    content += generate(3, models) + '\n'
    content += generate(3, models) + '\n'
    content += generate(3, models) + '\n'
    content += generate(3, models) + '\n'

    with open(sys.argv[2], 'w') as output:
        output.write(content)
                   
