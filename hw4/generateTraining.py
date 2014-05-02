# -*- coding: utf-8 -*-

import re

if __name__ == '__main__':
    
    #test or dev
    #datatype = "test"
    datatype = "dev"
  
    datafile = open("C:\\Users\\Mario\\Git\\sp2014.11-731\\hw4\data\\"+datatype+".100best")
    meteors = open("C:\\Users\\Mario\\Git\\sp2014.11-731\\hw4\data\\"+datatype+"_meteor.txt")
    
    hypnum = 0
    avglen = 0.0
    hypotheses = []
    for line in datafile:
      line = line.strip()
      hyptext = line.split('|||')[1]
      feats = {v.split('=')[0]:float(v.split('=')[1]) for v in line.split('|||')[2].split()}
      
      #get sentence length
      words = hyptext.split()
      feats["sentLen"] = len(words)
      #find words with Cyrillic letters and count them as untranslated/untransliterated
      untrans = 0
      for word in words:
        if re.search("[^\w\.\,'\"\?\!;()%\-\*:/$&ščťáéíóúüöæåøхapѕ[\]\+\#]",word,re.UNICODE):
          untrans += 1
      feats["untrans"] = untrans
      
      #print hypothesis and features to check
#      print hyptext
#      print feats
      
      hypotheses.append((hyptext,feats))
      hypnum += 1
      if hypnum > 200:
        break
    
    for i in range(0,len(hypotheses)):
      if i%100 == 0:
        if i != 0:
          avglen = float(totLen)/100
          print "\nAverage length for translation",i/100,":",avglen
          for j in range(i-100,i):
            hypotheses[j][1]["compLength"] = float(hypotheses[j][1]["sentLen"])/avglen
            
            print hypotheses[j][0]
            print hypotheses[j][1]
      
        totLen = 0
      
      totLen += hypotheses[i][1]["sentLen"]
    
    datafile.close()
    meteors.close()
