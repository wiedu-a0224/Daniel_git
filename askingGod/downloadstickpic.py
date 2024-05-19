import os
import requests

dirname ="pic"
if not os.path.exists(dirname):
    os.makedirs(dirname)
for i in range(1,61):
    url="http://www.citygod.tw/images/fortune/"+str(i)+".png"
    picname = str(i) + ".png"
    path = "pics/pic/"+ picname
    
    response = requests.get(url, stream=True)
    
    if response.status_code == 200:
        with open(path, "wb") as fp:
            for chunk in response.iter_content(chunk_size=8192):
                fp.write(chunk)
        print("圖檔已下載！")
    else:
        print("錯誤！HTTP請求失敗...")