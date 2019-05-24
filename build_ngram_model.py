#!/usr/bin/env python3
import math, sys

class Corpus:
    def __init__(self, material):
        self.tokens = []
        self.ngrams = {} 
        self.ngrams_count = {} 
        self.token_count = {}
        with open(material, 'r') as data:
            token_collect = [0, 0]
            unigrams = {}
            for line in data.readlines():
                content = line.replace('\n', '').lower()
                content = content.split(' ')
                content = ['<s>'] + content + ['</s>']
                self.tokens += content

                # Unigram Counts
                for unigram in content:
                    if unigram in unigrams:
                        unigrams[unigram][0] += 1
                    elif unigram != '<s>':
                        unigrams.update({unigram : [1, 0]}) #, unigram]})
                        token_collect[0] += 1

            # For Probability
            token_collect[1] = len(self.tokens)
            for unigram in unigrams:
                unigrams[unigram][1] = \
                 unigrams[unigram][0]/token_collect[1]

            # Saving the Unigrams
            self.ngrams_count.update({1 : unigrams})
            self.token_count.update({1 : token_collect})


    def build(self, count):
        if count not in self.ngrams:
            # Generates N-grams where count > 1
            token_collect = [0, 0]
            ngram_list = [] 
            for start in range(len(self.tokens) - count - 1):
                ngram = []
                for index_iter in range(count):
                    ngram += [self.tokens[start + index_iter]]
                if not ('</s>' in ngram and '</s>' != ngram[-1]): 
                    ngram_list.append(ngram)
            self.ngrams.update({count : ngram_list})
            token_collect[1] = len(ngram_list)
            
            # Calculates Counts
            counts = {}
            # didnt wanna break code + understanding when name is changed
            sample = ngram_list 
            for ngram in sample:
                title = tuple(ngram[:-1])
                if title in counts:
                    if ngram[-1] in counts[title]:
                        counts[title][ngram[-1]][0] += 1
                    else:
                        counts[title].update({ngram[-1]:[1,0, 
                         ' '.join(ngram)]})
                        token_collect[0] += 1
                else:
                    counts.update({title:{ngram[-1]:[1, 1, 
                     ' '.join(ngram)]}})
                    token_collect[0] += 1

            # Probabilities
            for ngram in counts:
                total = 0 
                for key, info in counts[ngram].items():
                    total += info[0]
                for key, info in counts[ngram].items():
                    counts[ngram][key][1] = \
                     counts[ngram][key][0]/total 

            self.token_count.update({count : token_collect})
            self.ngrams_count.update({count : counts})

    def __str__(self):
        content = '\data\ \n'
        for typevtoken in sorted(self.token_count.keys()):
            content += f'{typevtoken}-ngrams: types={self.token_count[typevtoken][0]} tokens={self.token_count[typevtoken][0]}\n\n'
        for nselect in sorted(self.ngrams_count.keys()):
            content += f'\\{nselect}-grams:\n'
            container = []
            for ngram, values in self.ngrams_count[nselect].items():
                if nselect != 1:
                    for pos in self.ngrams_count[nselect][ngram]:
                        cell = [values[pos][0]]
                        cell += [str(values[pos][1])]
                        cell += [str(math.log(values[pos][1]))]
                        cell += [str(values[pos][2])]
                        container += [cell]
                else:
                    cell = [values[0]]
                    cell += [str(values[1])]
                    cell += [str(math.log(float(values[1])))]
                    cell += [str(ngram)]
                    container += [cell]

            present = sorted(container)
            present.reverse()
            for line in present:
                line[0] = str(line[0])
                content += ' '.join(line) + '\n'
        return content


if __name__ == "__main__":
    corp = Corpus(sys.argv[1])
    corp.build(2)
    corp.build(3)
    with open(sys.argv[2], 'w') as output:
        output.write(str(corp))

# stackoverflow.com/questions/2493920/how-to-switch-position-of-two-items-in-a-python-list
# ^ How I swapped to elements in a list
    
