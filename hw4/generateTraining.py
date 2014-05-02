# -*- coding: utf-8 -*-

import re

if __name__ == '__main__':
    
    #test or dev
    
    #datatype = "test"
    datatype = "dev"
  
    datafile = open("C:\\Users\\Mario\\Git\\sp2014.11-731\\hw4\data\\"+datatype+".100best")
    
    meteors = open("C:\\Users\\Mario\\Git\\sp2014.11-731\\hw4\data\\"+datatype+"_meteor.txt")
    
    hypnum = 0
    for line in datafile:
      line = line.strip()
      hyptext = line.split('|||')[1]
#      feats = [float(v.split('=')[1]) for v in line.split('|||')[2].split()]
      feats = {v.split('=')[0]:float(v.split('=')[1]) for v in line.split('|||')[2].split()}
#      feats = {}
#      for feature in line.split('|||')[2].split():
#        feats[feature.split('=')[0]] = feature.split('=')[1]
      
      words = hyptext.split()
      feats["sentLen"] = len(words)
      cyrillic = set(unicode("ёъяшертыуиопющэасдфгчйкльжзхцвбнмЁЪЯШЕРТЫУИОПЮЩЭАСДФГЧЙКЛЬЖЗХЦВБНМ"))
      cyrils = 0
      for word in words:
        if set(word) & cyrillic:
          cyrils += 1
          print word,
      #cyrils = re.findall("[\A ][^ ]*[ёъяшертыуиопющэасдфгчйкльжзхцвбнмЁЪЯШЕРТЫУИОПЮЩЭАСДФГЧЙКЛЬЖЗХЦВБНМ][^ ]*[\B ]",hyptext,re.UNICODE)
      #feats["untrans"] = len(re.findall("[\A ][^ ]*[ёъяшертыуиопющэасдфгчйкльжзхцвбнмЁЪЯШЕРТЫУИОПЮЩЭАСДФГЧЙКЛЬЖЗХЦВБНМ][^ ]*[\B ]",hyptext,re.UNICODE))
      feats["untrans"] = cyrils
      if feats["untrans"] > 1:
        print hyptext
        print feats
        hypnum += 1
      if hypnum > 200:
        break
    
    datafile.close()
    meteors.close()
