import bs4
from urllib.request import urlopen
from urllib.request import Request

url = "https://www.104.com.tw/jobs/search/?ro=0&jobcat=2010001006%2C2010001007%2C2010001004%2C2010001010%2C2010001005&kwop=7&keyword=%E8%BB%8A%E5%BA%8A%E6%8A%80%E5%B7%A5&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001002000&order=15&asc=0&page=2&mode=s&jobsource=tab_cs_to_job&langFlag=0&langStatus=0&recommendJob=1&hotJob=1"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

req = Request(url, headers=headers)
response = urlopen(req)
html = bs4.BeautifulSoup(response, "html.parser")
#print(type(html))
target = html.find_all("article", class_="js-job-item",  )
print(target)
