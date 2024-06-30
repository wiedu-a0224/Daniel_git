import bs4
from urllib.request import urlopen
from urllib.request import Request

titles = []

for i in range(1, 19):
    
    print(f"Page: {i}")
    url = "https://www.104.com.tw/jobs/search/?ro=0&jobcat=2010001006%2C2010001007%2C2010001004%2C2010001010%2C2010001005&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&area=6001003000%2C6001004000&order=15&asc=0&page="+str(i)1&mode=s&jobsource=tab_cs_to_job&langFlag=0&langStatus=0&recommendJob=1&hotJob=1"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    req = Request(url, headers=headers)
    response = urlopen(req)
    html = bs4.BeautifulSoup(response, "html.parser")
    #print(type(html))
    target = html.find_all("ul", class_="b-clearfix")

    # 如果 target 是空的，表示沒有更多頁面，停止循環
    if not target:
        print("No more pages. Stopping.")
        break

    job_no = 1  # 初始化職位編號
    for ul in target:
        for li in ul.find_all("li"):
            a_tag = li.find("a")
            if a_tag and "title" in a_tag.attrs:
                titles.append(a_tag['title'])
                job_no += 1  # 每次迭代後增加職位編號 
    # print(titles)
    # 在迴圈外部打開一個文件以寫入
    with open('titles.txt', 'w', encoding='utf-8') as file:
        for title in titles:
            file.write(title + '\n')  # 將每個標題寫入文件，並在每個標題後添加換行符
        