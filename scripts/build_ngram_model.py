import time, sys

def ngrams(count, material):
    content = ''
    

def bigram_count(material):
    d = {}
    material = ngrams(count, material)
    for bi in material:
        key, value = [bi[0].lower(),bi[1].lower()]
        print(str(key) + ' ' + str(value))
        if bi[0] not in d:
            d.update({key : {value:1}})
        else:
            if value not in d[key]:
                d[key].update({value:1})
            else:
                d[key][value] += 1
    return d

def probability(d, phrases):
    print(d)
    c = []
    for ophrase in phrases:
        compare = []
        phrase = word_tokenize(ophrase)
        for index in range(0, len(phrase)-1):
            result = 0
            first, second = [phrase[index], phrase[index + 1]]
            count, versus = (0,0)
            if second in (d[first] if first in d else []):
                count = d[first][second]
                for other, value in d[first].items():
                    print(str(other) + ': ' + str(value))
                    versus += value

            if count > 0 and versus == 0:
                result = 1
            elif count == 0 and (versus > 0 or versus == 0):
                result = 0
            else:
                result = count/versus
            compare.append(result)
        r = 1
        for s in compare:
            r = r * s
        c.append((ophrase, r))
    return c

src = corpus.gutenberg.words('milton-paradise.txt')
bigrams_list = bigramz(src)
phrases_list = [
    'he is',
    'she is',
    'she ate',
    'it was a little thing',
    'the earth trembled',
    'a man appeared',
    'the old man'
]

#print(probability(bigrams_list, phrases_list))
aa = ['a', 'the', 'she', 'he', 'they']
for thing in aa:
    print(bigrams_list[thing])

