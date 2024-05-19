from flask import Flask, request, jsonify
from PIL import Image
import random


app = Flask(__name__)

@app.route('/Github/Daniel_git/askingGod/drawstick', methods=['get'])
def handle_request():

    # 隨機從1~60選取一個數字
    def draw(a, b):
        return random.randint(1, 60)
    f  = draw(1, 100)

    # 從pic資料夾中選取一張圖片
    im = Image.open("pics/stickpic/"+ str(f) +".png")
    # 顯示圖片
    im.show()
   # Return the result as JSON
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
            

   