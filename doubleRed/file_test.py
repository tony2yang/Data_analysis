import re
f = open('text.txt','r')

line = f.readline()

while line:
    print(line)
    lst = line.split('\t')
    for i, el in enumerate(lst):

        lst[i] = re.sub('\D', '', el)

    print(lst)
    lst.pop()

    print(lst)
  #  print(re.sub('\D','',line.split('\t')))
    line = f.readline()
f.close()

#print(re.sub('\d','abc','as123avc'))