'''

http://www.cwl.gov.cn

'''

import requests
import re
import time
from bs4 import BeautifulSoup

links = "http://www.cwl.gov.cn/kjxx/ssq/hmhz/index{0}.shtml"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

for i in range(38):
    if i == 0:
        v_ind = ''
    else:
        v_ind = '_'+ str(i)
    link = links.format(v_ind)
    response = requests.get(link, headers=headers)
    time.sleep(2)

    response.encoding = 'UTF-8'
    r = response.text
    soup = BeautifulSoup(r, 'lxml')

    ind = 1
    lst_num = []
    lst_link = {}
    for content in soup.tbody.contents:

        if ind % 2 == 1 and ind >= 5:
            res = re.sub(r"\n[\s| ]*\n", '\t', content.text)
            res = re.sub(r"\n", '\t', res)
            lst_num.append(res)
            kjxx_num = content.find_all('td')[0].text
            for link in content.find_all('a'):
                # print(link.get('href'))
                lst_link[kjxx_num] = link.get('href')
        ind += 1


        # print(content.find_all('a'))

    # print(lst)


    print(lst_link)
    # write win-number records in file
    with open('text.txt', 'a+') as f:
        for i in lst_num:
            f.write(re.sub(r"\t", '', i, 1) + '\n')
        f.close()

    # write links which notes the detail of each win-number
    with open('links.txt', 'a+') as f:
        for i, j in lst_link.items():
            f.write(i + '\t' + j + '\n')
        f.close()
