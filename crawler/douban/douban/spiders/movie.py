# -*- coding: utf-8 -*-
import scrapy
import requests
from scrapy.http import Request,FormRequest
from lxml.cssselect import etree


class MoviesSpider(scrapy.Spider):
    name = "movie"
    allow_domains = ['douban.com']

    # post登入的必须要的头字段
    post_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
        "Referer": "https://accounts.douban.com",
    }

    def start_requests(self):
        """
        执行spider，开始请求
        :return: 返回一个Request对象，请求登录的页面
        登录页面最好用fiddler一次抓取准确的请求链接
        """
        return [Request(url='https://accounts.douban.com/login', meta={'cookiejar': 1}, callback=self.post_login)]

    def post_login(self, response):
        """
        登录的页面请求成功后，解析响应的页面，获取登录需要的<input>标签的信息
        :param response: 登录接口返回的页面
        :return:
        """
        try:
            captcha = response.xpath('//span[@id="captcha_block"]/text()').extract()
            if len(captcha) > 0:
                img_url = response.xpath('//img[@id="captcha_image"]/@src').extract()[0]
                print(img_url)
                self.get_code(img_url)
                new_captcha = input('请输入获取的验证码：')
                username = 'yuhelg@163.com'
                password = '907625540'
                data = {
                    'form_email': username,
                    'form_password': password,
                    'captcha-solution': str(new_captcha),
                }
            else:
                print('2222222222222')
                username = 'yuhelg@163.com'
                password = '907625540'
                data = {
                    'form_email': username,
                    'form_password': password,
                }
            return FormRequest.from_response(response=response,
                                                 meta={'cookiejar': response.meta['cookiejar']},
                                                 headers=self.post_headers,
                                                 formdata=data,
                                                 callback=self.after_login)
        except Exception as e:
            print(e)
            username = 'yuhelg@163.com'
            password = '907625540'
            data = {
                'form_email': username,
                'form_password': password,
            }
            # 发送FormRequest表单请求
            return FormRequest.from_response(response=response,
                                             meta={'cookiejar': response.meta['cookiejar']},
                                             headers=self.post_headers,
                                             formdata=data,
                                             callback=self.after_login)

    def after_login(self, response):
        """
        form表单请求成功后，请求登入我的页面
        """
        if response.status == 200:
            return Request("https://www.douban.com/people/172348475/",
                           meta={'cookiejar': response.meta['cookiejar']},
                           callback=self.parse_page)

    def parse_page(self, response):
        """
        将响应的我的页面数据，写入文件
        """
        if response.status == 200:
            with open('my_account6.html', 'wb')as f:
                f.write(response.body)


    def get_code(self,url):
        img=requests.get(url).content
        with open(r'C:\Users\Administrator\Desktop\code\code.jpg','wb') as fp:
            fp.write(img)
            fp.close()
