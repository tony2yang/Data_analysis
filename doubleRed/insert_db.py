import mysql.connector
import re

conn = mysql.connector.connect(user='dev', password='123456', database='dev')

cursor = conn.cursor()

cursor.execute('drop table double_red_list')

cursor.execute('''create table double_red_list (id mediumint primary key, first_number TINYINT, second_number TINYINT, thrid_number TINYINT,
               forth_number TINYINT, fifth_number TINYINT, sixth_number TINYINT, red_number TINYINT, winner_number SMALLINT, sell_amount INT, rest_amount INT)
               ''')

# read records
f = open('text.txt', 'r')

line = f.readline()

while line:
    ind = 1
    # if line.split('\t')[0] == '2015012':
    # #    pass
    #     print(line)
    lst = line.split('\t')
    for i, el in enumerate(lst):
        if len(lst) > 12:
            ind = 0
        # remove the non-digit characters
        lst[i] = re.sub('\D', '', el)
    # remove the last element which is '\n'
    # if lst[0] == '2015012':
    #     print(lst)
    if ind == 0:
        del lst[10]
        del lst[8]
    if lst[-1] == '':
        lst.pop()

    if lst[0] == '2015012':
        print(lst)
    # insert the list elements to table
    cursor.execute('''insert into double_red_list (id, first_number, second_number, thrid_number, forth_number,
                      fifth_number, sixth_number, red_number, winner_number, sell_amount, rest_amount)
                      values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''', lst)

    # read next line
    line = f.readline()
f.close()


cursor.close()
conn.commit()