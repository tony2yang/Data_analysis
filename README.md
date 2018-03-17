# Data_analysis
## Item One:
	Description:<br>
	Analyze the history records of double red winning numbers to perdict lottery number.<br>
	Step:<br>
		1. Crawl data from the official site<br>
			 a. sort the blue numbers before load data<br>
		2. load data to Mysql<br>
		3. analysze data by using python tools<br>
		

# Command Notes
Python mirrors address:<br>
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyspider<br>

-

1. create project:<br>
scrapy startproject <project_name><br>
e.g. scrapy startproject PCeggs<br>
<br>
startproject: create project
PCeggs: created project name

-

2. create spider:<br>
scrapy genspider <spider_name> <"website"><br>
<br>
e.g. scrapy genspider pceggs "www.pceggs.com"<br>
<br>
gensider: create a spider (default class is scrapy.Spider)<br>
pceggs: spider name (corresponding the parameter of 'name' in spider script)<br>
"www.pceggs.com": allowed spider domain<br>

-

3. execute spider:<br>
scrapy crawl <spider_name><br>
e.g. scrapy crawl pceggs<br>
<br>
crawl: start a scrapy spider<br>
pceggs: the spider name which would be started (the spider name is the same as parameter 'name' in script)<br>
