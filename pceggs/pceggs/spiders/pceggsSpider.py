# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
from PIL import Image

class PceggsspiderSpider(scrapy.Spider):
    name = 'pceggsSpider'
    allowed_domains = ['pceggs.com']
    start_urls = ['http://www.pceggs.com',]
    headers_dict = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
         'Host': 'www.pceggs.com',
        'Referer': 'http://www.pceggs.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }
    verifyCodeFile = "captcha.gif"

    # 重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数
    def start_requests(self):
        return [Request("http://www.pceggs.com/nologin.aspx", headers=self.headers_dict, meta={'cookiejar': 1},
                        callback=self.login)]

    def login(self, response):
        captcha = response.xpath('//img[@id="valiCode"]/@src').extract()

        verifyCodeUrl = 'http://www.pceggs.com' + captcha[0]
        UserName = input('Enter ID: ')
        passWD = input('Enter PassWord: ')

        viewstate = response.xpath('//input[@id="__VIEWSTATE"]/@value').extract()[0]
        viewstategenerator = response.xpath('//input[@id="__VIEWSTATEGENERATOR"]/@value').extract()[0]
        head2withdraw = response.xpath('//input[@id="Head2_WithdrawCount"]/@value').extract()[0]

        data = {
            '__VIEWSTATE':viewstate,
            '__VIEWSTATEGENERATOR':viewstategenerator,
            'Head2$WithdrawCount': head2withdraw,
            'txt_UserName': UserName,
            'txt_PWD': passWD,
            'txt_VerifyCode': "" ,
            'Login_Submit.x': '4',
            'Login_Submit.y': '3',
            'FromUrl':'http://www.pceggs.com/',
            'SMONEY':'ABC'
        }
        """
            必须保证验证码的使用，与得到验证码的链接请求是在同一个会话连接中，此处使用 Request 的方法，
            通过 scrapy 将请求下载之后，使用回调函数，在回调函数中进行处理，保证回调函数中的 response 与获取验证码时
            是在同一个会话中
        """

        yield scrapy.Request(verifyCodeUrl,
                             meta={"post_data": data},
                             headers=self.headers_dict,
                             callback=self.login_with_checkcode)

    def login_with_checkcode(self, response):
        post_url = "http://www.pceggs.com/nologin.aspx"
        post_data = response.meta.get("post_data", {})
        #print("Saving the verifyCode picture...")
        with open(self.verifyCodeFile, "wb") as f:
            f.write(response.body)
            f.close()

        try:
            im = Image.open(self.verifyCodeFile)
            im.show()
        except:
            pass

        post_data["txt_VerifyCode"] = input("Enter verifyCode:")

        return [FormRequest(
            url=post_url,
            formdata=post_data,
            headers=self.headers_dict,
            callback=self.crawlerdata
        )]

    def crawlerdata(self, response):
        """
        check if login sucessful
        """
        url_play = "http://www.pceggs.com/play/pxya.aspx"
        if response.xpath('//p/span/a/text()').extract()[0] == '25786377':
            print ('login sucessful!!!!!!!!!!!!!')

        # print(response.url)
        # with open(r'E:/pceggs.html','w') as f:
        #      f.write(response.body.decode('utf-8'))
        # print(response.body.decode('utf-8'))
        # print ('****************************')
    #def parse(self, response):
     #   pass
