import bs4
from urllib.request import urlopen
from urllib.request import Request

titles = []

for i in range(1, 30):
    
    print(f"Page: {i}")
    url = "https://www.1111.com.tw/search/job?c0=100200&ks=%E9%8A%91%E5%BA%8A&page={i}&reks=%E6%A9%9F%E6%A2%B0%E5%8A%A0%E5%B7%A5%E6%8A%80%E8%A1%93%E4%BA%BA%E5%93%A1%2C%E8%BB%8A%E5%BA%8A%E4%BA%BA%E5%93%A1%2C%E9%8A%91%E5%BA%8A%E4%BA%BA%E5%93%A1%2CCNC%E6%A9%9F%E5%8F%B0%E6%93%8D%E4%BD%9C%E4%BA%BA%E5%93%A1%2C%E8%BB%8A%E5%BA%8A"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    req = Request(url, headers=headers)
    response = urlopen(req)
    html = bs4.BeautifulSoup(response, "html.parser")
    #print(type(html))
    target = html.find_all("div", class_="company organ")

    # 如果 target 是空的，表示沒有更多頁面，停止循環
    if not target:
        print("No more pages. Stopping.")
        break

    for div in target:
    # 假設每個 div 元素下的 a 標籤包含我們需要的標題
        a_tag = div.find("a")
        if a_tag and "title" in a_tag.attrs:
            titles.append(a_tag["title"])  # 添加實際的標題到列表
# print(titles)
    # 在迴圈外部打開一個文件以寫入
    with open('titles.txt', 'w', encoding='utf-8') as file:
        for title in titles:
            file.write(title + '\n')  # 將每個標題寫入文件，並在每個標題後添加換行符
        