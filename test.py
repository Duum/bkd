# -*- coding: utf-8 -*-
from collections import Counter
import re
import logging
from bs4 import BeautifulSoup
from readmdict import MDX,MDD
dirstring="资料来源整理/资料来源整理/"
mdx=MDX("21世纪大英汉词典.mdx")
r=r"`1`.*?`2`(\[.*?\])?\s*(\<br\>)?"
r1=r"`\d`"
#logging.basicConfig()
logger = logging.getLogger('root')
fh = logging.FileHandler('test.log')
fh.setLevel(logging.INFO)
logger.addHandler(fh)
pattern=re.compile(r)
pattern1=re.compile(r1)
dic={}
valuelist=[]
for key,value in mdx.items():
    try:
       soup=BeautifulSoup(value)

          #print soup.prettify()
       phone= soup.find("span",class_="phone")
       tree=soup.find_all("span",class_="trs")
      # print key
       synonym=soup.find("span",class_="syno")
       #同义词
       antonym=soup.find("span",class_="anto")
       #反义词

       if key=="abandon":
           #print soup.prettify()
           #print tree.text
           meaningdic={}
           for i in range(len(tree)):
              pos=tree[i].find("span",class_="pos")
              for item in tree[i].find_all("span",class_="tr"):
                  print item.text
           #print meaningdic
           # for key ,value in enumerate(meaningdic):
           #     for item in value:
           #         print item
           synonym_dic=[item.text for item in synonym.find_all("span",class_="i")]
           antonym_dic=[item.text for item in antonym.find_all("span",class_="i")]
           print synonym_dic
           print antonym_dic
       #print tree.text

       #print phone.text
       #print phone.text
    except Exception:
        pass
        #print key
        #print soup.prettify()
       # print "some error"
#    valuelist.append(key)
print len(valuelist)