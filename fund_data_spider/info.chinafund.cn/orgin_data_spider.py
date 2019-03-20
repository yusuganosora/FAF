# -*- coding: UTF-8 -*-
"""
该python文件从http://info.chinafund.cn网站上爬取所有的基金代码
lwf 2019-03-20
"""
from urllib import request
import re
file=open("../../data/fun_no.txt","w")
rep=request.Request("http://info.chinafund.cn/company/")
rep.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36")
rep.add_header("Connection","keep-alive")
resp=request.urlopen(rep)
if(resp.status==200):
    response_data=resp.read().decode("GB2312","ignore")
    re_fund=re.compile("<a href='.*?' target='_blank'>(.*?)</a>")
    for i in re_fund.findall(response_data):
      file.write(i+"\n")
else:
    file2=open("spider_log","w+")
    file2.write("info.chinafund.cn-->orgin_data_spider-->error-->http_status:"+resp.status+"\n")
    file2.close()
file.close()