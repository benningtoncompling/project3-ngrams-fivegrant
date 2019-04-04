#!/usr/bin/env python3
import math, sys, time

class Corpus:
    def __init__(self, material):
        start = time.time()
        self.tokens = []
        self.ngrams = {} 
        self.ngrams_count = {} 
        self.token_count = {}
        with open(material, 'r') as data:
            for line in data.readlines():
                content = line.replace('\n', '').lower()
                content = content.split(' ')
                content = ['<s>'] + content + ['<\\s>']
                self.tokens += content
        finish = str(round(time.time() - start, 2))
        print('Corpus Object initialized in ' + finish + ' seconds')

    def build(self, count):
        if count not in self.ngrams:
            start = time.time()

            #Generates N-grams
            token_collect = [0, 0]
            ngram_list = [] 
            for start in range(len(self.tokens) - (count - 1)):
                ngram = []
                for index_iter in range(count):
                    ngram += [self.tokens[start + index_iter]]
                if not ('<\s>' in ngram and '<\s>' != ngram[-1]): 
                    ngram_list.append(ngram)
                    token_collect[0] += 1
#                    print(ngram)                                        #d
            self.ngrams.update({count : ngram_list})
            
            #Calculates Counts and Probabilities
            counts = {}
            sample = self.ngrams[count]
            for ngram in sample:
                title = ' '.join(ngram[:-1])
                print(ngram)                                            #d
                if ngram[:-1] in counts:
                    if sample[0] in ngram[0]:
                        counts[title][ngram[0]][0] += 1
                    else:
                        counts[title].update({ngram[0]:[1,0, 
                         ' '.join(ngram)]})
                    total = 0 
                    for key, info in counts[title].items():
                        total += info[0]
                        counts[title][ngram[0]][1] = \
                         counts[title][ngram[0]][0]/total  
                else:
                    counts.update({title:{ngram[0]:[1, 1, 
                     ' '.join(ngram)]}})
                    token[1] += 1
            self.token_count.update({count : token_collect})
            self.ngrams_count.update({select : counts})
            finish = str(round(time.time() - start, 2))
            print(str(count) + '-grams analyzed in ' + finish + 'seconds')
        else:
            print(str(count) + '-gram already exists')

    def __str__(self):
        content = '\data\ \n'
        for tokenvtype in sorted(self.token_count.keys):
            content += '%s-ngrams: types=%s tokens=%s \n' % (
             str(tokenvtype), str(self.token_count[tokenvtype][0]), 
             str(self.token_count[tokenvtype][1]))
        for nselect in sorted(self.ngrams_count.keys):
            content += '\\%s-grams:\n' % str(nselect)
            container = []
            for ngram in self.ngrams_count[nselect]:
                for pos in ngram:
                    cell = str(ngram[pos][1]) + ' '
                    cell += str(ngram[pos][0]) + ' '
                    cell += str(math.log(ngram[pos][0])) + ' '
                    cell += str(ngram[pos][2]) + '\n'
            for line in sorted(container):
                content += line
        return content
            
q = Corpus('./data/input/dickens_test.txt')
q.build(1)
q.build(2)
q.build(3)
print(dothis)
