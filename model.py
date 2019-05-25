import re

class Model:
    def __init__(self, material, ngram_size):
        self.size = ngram_size
        self.ngrams = {}

        total_probability = 0
        if self.size == 1:
            for ngram in material:
                self.ngrams.update({total_probability: ngram[3]})
                total_probability += float(ngram[1]) 
        else:
            for ngram in material:
                key, result = ' '.join(ngram[3].split()[:-1]), ngram[3].split()[-1]
                if key not in self.ngrams:
                    self.ngrams.update({key:{float(ngram[1]): result}})
                else:
                    self.ngrams[key].update({total_probability: result})
                    total_probability = max([prb for prb in self.ngrams[key]])
                    total_probability += float(ngram[1])

            
    def __str__(self):
        content = '(' + str(int(self.size)) + ')\n'
        if self.size == 1:
            for prob, word in self.ngrams.items():
                content += f'{prob} : {word}\n'
        else:
            for word in self.ngrams:   
                content += f'{word}\n'
                for prob, result in self.ngrams[word].items():
                    content += f'\t{prob} : {result}\n'
        content += '\n'
        return content
        


# Creates models and allows access to them later. 
# Also, allows you to write output 

class Model_Collection:
    def __init__(self, input):
        self.models = {}
        with open(input, 'r') as file:
            data = None
            for line in file.readlines():
                capture = re.match(r'\\(\d+)-grams:', line)
                if len(line) < 5:
                    data = None
                if data != None:
                    collect = line.split()
                    if len(collect) > 4:
                        collect[3] = ' '.join(collect[3:])
                        self.models[data].append(collect[:4])
                    else:
                        self.models[data].append(collect)
                elif capture:
                    data = float(capture[1])
                    self.models.update({data:[]})
                else:
                    data = None

        for size in self.models:
            # Transforming the raw data floato an Ngram
            self.models[size] = Model(self.models[size], size)

    def get_model(self, size):
        return self.models[size]

    def __str__(self):
        content = ''
        for num, mod in self.models.items():
            content += str(mod)
            content += '\n\n'
        return content
