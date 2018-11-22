from scrapy import Spider, Request, FormRequest
import requests


class GithubLoginSpider(Spider):
    name = "caip"
    allow_domains = ['310win.com']

    # post登入的必须要的头字段
    post_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",

    }

    def start_requests(self):
        """
        执行spider，开始请求
        :return: 返回一个Request对象，请求登录的页面
        """
        return [Request(url='https://accounts.douban.com/login', meta={'cookiejar': 1}, callback=self.post_login)]

    def post_login(self, response):
        """
        登录的页面请求成功后，解析响应的页面，获取登录需要的<input>标签的信息
        :param response: 登录接口返回的页面
        :return:
        """

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
        :param response:
        :return: 返回一个响应
        """
        if response.status == 200:
            return Request("https://www.douban.com/people/172348475/",
                           meta={'cookiejar': response.meta['cookiejar']},
                           callback=self.parse_page)

    def parse_page(self, response):
        """
        将响应的我的页面数据，写入文件
        :param response:
        :return:
        """
        if response.status == 200:
            with open('my_account3.html', 'wb')as f:
                f.write(response.body)
