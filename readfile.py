# -*- coding: utf-8 -*-
import os
import logging
from collections import Counter
import re
import json
import psycopg2
conn=psycopg2.connect(database="word",user="beikaodi",password="bkd_smart123",host="rm-2zeg1e0w5v7w5v7y8o.pg.rds.aliyuncs.com",port="3432")
cur = conn.cursor()
logging.basicConfig()
from bs4 import BeautifulSoup
from readmdict import MDX,MDD
dirstring="资料来源整理/资料来源整理/"
mdx=MDX("牛津英汉简明词典.mdx")
r=r"`1`.*?`2`(\[.*?\])?\s*(\<br\>)?"
r1=r"`\d`"
pattern=re.compile(r)
pattern1=re.compile(r1)
dic={}
for key,value in mdx.items():
    valuelist=[]
    match = pattern.sub("",value)
    #print match
    items=match.split("<br>")
    items=[item.strip() for item in items]
    for item in items:
        item = pattern1.sub("",item)
        valuelist.append(item)
        print item
    value_string=";".join(valuelist)
    print value_string
    #print value_string
    string_json=json.dumps(valuelist)
    if key=="abandon":
        print key
        #print value
    #cur.execute("insert into  bkd_word (spell,brief) values (%s,%s)",(key,string_json))
cur.execute("SELECT * FROM bkd_word")
rows = cur.fetchall()        # all rows in table
print(rows)
for i in rows:
    print(i)
conn.commit()
cur.close()
conn.close()
    #print value
    #print value.split("<br>")[0]
    #soup=BeautifulSoup(value)

# filelist=os.listdir(dirstring)
# for item in filelist:
#     if item.endswith(".mdx"):
#         print item
#         mdx=MDD(dirstring+item)
#         for key, value in mdx.items():
#             print key,value