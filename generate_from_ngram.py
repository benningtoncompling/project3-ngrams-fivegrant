import random, sys

class Generator:
    def __init__(self, material, ngram_size);
        self.size = ngram_size
        self.ngrams = {}
        with open(material, 'r') as data:
            activated = False
            key = 0
            for line in data.readlines():
                if line == ('\\' + ngram_size + '-grams:'):
                    activated = True:
                if activated:
                    data = line.split(' ')
                    key += data[0]
                    self.ngrams.update({key : data[3]})

    def create(self):
        focus = '<s>'
        while()
            select = random.random()
            for prob in self.ngrams:
                if  < prob
