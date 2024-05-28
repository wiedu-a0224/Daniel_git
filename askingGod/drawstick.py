from PIL import Image
import random


# 隨機從1~60選取一個數字
def draw(a, b):
    return random.randint(1, 60)

f  = draw(1, 100)

# 從pic資料夾中選取一張圖片
im = Image.open("pics/stickpic/"+ str(f) +".png")
# 顯示圖片
im.show()

   