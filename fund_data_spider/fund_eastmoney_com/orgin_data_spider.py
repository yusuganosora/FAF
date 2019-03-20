from urllib import request
import re
file=open("../../data/fun_no.txt","w")
resp=request.urlopen("http://info.chinafund.cn/company/")
response_data=resp.read().decode("GB2312","ignore")
re_fund=re.compile("<a href='.*?' target='_blank'>(.*?)</a>")
for i in re_fund.findall(response_data):
    file.write(i+"\n")
resp2=request.urlopen("http://info.chinafund.cn/fund/000310/")
print(resp2.read().decode("GB2312","ignore"))
file.close()