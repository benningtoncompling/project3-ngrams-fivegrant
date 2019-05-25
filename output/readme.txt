# My favorite sentences:
unigram
already but ‘ story you the proclamation to and that as was mr without chancellor hand a horses in and ,

bigram 
i should jest of few people to sleep , and get ’ am very expeditious process several little maid -- took to try .

trigram
, `` my good sir , ’ said the waiter , with the tears a-tricklin ’ down his empty drinking vessel ; but it may alone be worth thinking of , i ’ d deane afore -- “ i am , i must keep them still more in her . ) 

# Write Up
I created a module called model.py that captured the data in an overarching 
called a model_collection that contains model objects. This was defined 
generically to allow any size n-gram.

I again learned how useful regular expressions could be in picking out 
incoming data. I also learned how useful it is to structure the data
in a way in which it could be captured.

With bigrams and trigrams, I had issues with keeping track of the probability.
I'd keep getting values that were greater than 1, so I finally made a seperate
dictionary to keep track of them.

I made everything n-gram oriented so it can in theory handle any type of ngram. 
This really was a challenge with the generator which I got passed by 
making the function recursive
