# -*- coding: utf-8 -*-
'''
Created on Jan 30, 2014

@author: Jeremy Doornbos
@author: Mario Piergallini
'''

from collections import defaultdict
    
if __name__ == '__main__':
    
    def getbest(word, g_sent):
        maxprob = 0
        aligned = -1
        for g in g_sent:
            if t[(g,word)] > maxprob:
                maxprob = t[(g,word)]
                aligned = g_sent.index(g)
        if aligned == len(g_sent)-1:
          return -1
        return aligned
    
    data = 'data//dev-test-train.de-en'
    bitext = [[sentence.strip().split() for sentence in pair.split(' ||| ')] for pair in open(data)]
    
    for sent in bitext:
      sent[0].append("")
    
    numtoprint = 10
    goldData = 'data//dev.align'
    gold = [aligns.strip() for aligns in open(goldData)][:numtoprint]
    
    english_words = set()
    german_words = set()
    
    i = 1
    for (german,english) in bitext:
        if i % 10000 == 0:
            print "sentence:", i
        for english_i in english:
            english_words.add(english_i)
        for german_j in german:
            german_words.add(german_j)
        i += 1
    
    gerlen = len(german_words)
    englen = len(english_words)
    
    t = defaultdict(lambda:1/float(gerlen))
    t_count = defaultdict(float)
    total = defaultdict(float)
    s_total = defaultdict(float)
    
    print gerlen-1,"German words"
    print englen,"English words"
                
    for i in range(5):
        print "iteration = " + str(i+1) + ":"
        for (german,english) in t:
            t_count[(german,english)] = 0
            total[english] = 0
        s = 0
        for sent in bitext:
            if s % 10000 == 0:
                print "   sentence:", s
            s += 1
            for german in sent[0]:
                s_total[german] = 0
                for english in sent[1]:
                    s_total[german] += t[(german,english)]
            for german in sent[0]:
                for english in sent[1]:
                    t_count[(german,english)] += t[(german,english)]/s_total[german]
                    total[english] += t[(german,english)]/s_total[german]

        for (german,english) in t:
            t[(german,english)] = t_count[(german,english)]/total[english]

    output = open("output.txt",'w')
    
    for sent in bitext[:numtoprint]:
        print " ".join(sent[0])
        print gold[bitext.index(sent)]
        print " ".join(sent[1])
        for word in sent[1]:
            if getbest(word,sent[0]) >= 0:
                sentOutput = str(getbest(word,sent[0])) + '-' + str(sent[1].index(word))
            print sentOutput,
        print
        for word in sent[1]:
            print word + '-' + sent[0][getbest(word,sent[0])],
        print
        print
    
    for sent in bitext:
        sentOutput = ""
        for word in sent[1]:
            if getbest(word,sent[0]) >= 0:
                sentOutput += str(getbest(word,sent[0])) + '-' + str(sent[1].index(word)) + ' '
        output.write(sentOutput.strip() + "\n")