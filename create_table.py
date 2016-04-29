import psycopg2
conn=psycopg2.connect(database="keyword",user="beikaodi",password="bkd_smart123",host="rm-2zeg1e0w5v7w5v7y8o.pg.rds.aliyuncs.com",port="3432")
cur = conn.cursor()
cur.execute("INSERT INTTO bkd_word(spell,phonogram,brief,meanings,etymology)VALUES(%s,%s,%s,%s,%s)",())