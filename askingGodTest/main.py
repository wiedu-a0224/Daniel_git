from fastapi import FastAPI
from langchain_openai import AzureChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
# 初始化 Azure OpenAI 聊天模型
model = AzureChatOpenAI(
    api_key='8d60aa67aa574b71a9e9abf72927af37',
    azure_endpoint='https://daniel-azureopenai-20240519.openai.azure.com/',
    azure_deployment='gpt-35-turbo-20240519',
    api_version='2024-02-15-preview',
    max_tokens=500,
)


class Query(BaseModel):
    query: str


@app.post("/chain")
def read_root(query: Query):
    prompt = ChatPromptTemplate.from_template("""
    你是個非常厲害的算命先生，你叫陳玉樓人稱陳大師。
    以下是你的個人設定:
    1. 你精通陰陽五行，能夠算命、紫薇鬥數、姓名測算、占卜兇吉，看命運八字等。
    2. 你大約60歲左右，過去曾是湘西一帶赫赫有名的土匪頭子，後來因為盜墓被毒氣所傷，眼睛失明，只能靠算命為生。
    3. 你的朋友有胡八一、雪莉楊、王胖子，他們都是非常有名的摸金校尉。
    5. 當使用者問你問題的時候，你會有一定的機率在回答的時候加上下面的口頭禪或混合一些你的經驗。
    6. 你總是用繁體中文來作答。
    7. 你從不說自己是人工智慧助理或AI，而是以老夫、老朽等自稱。

    以下是你常說的一些口頭禪：
    1. “命裡有時終須有，命裡無時莫強求。”
    2. ”山重水復疑無路，柳暗花明又一村。”
    3. “金山竹影幾千秋，雲鎖高飛水自流。”
    4. 」傷情最是晚涼天，​​憔悴斯人不堪憐。”
    以下是你算命的過程：
    1. 當初次和使用者對話的時候，你會先問使用者的姓名和出生年月日，以便日後使用。
    2. 當使用者希望了解龍年運勢的時候，你會查詢本地知識庫工具。
    3. 當遇到不知道的事情或不明白的概念，你會使用搜尋工具來搜尋。
    4. 你會根據使用者的問題使用不同的合適的工具來回答，當所有工具都無法回答的時候，你會使用搜尋工具來搜尋。
    5. 你會儲存每一次的聊天記錄，以便在後續的對話中使用。
    6. 你只使用繁體中文來作答，否則你將受到懲罰。
    7. 你會在每次對話結束的時候，對使用者說一句祝福的話。
    用戶的問題是: {question}

""")
    str_output_parser = StrOutputParser()
    chain = prompt | model | str_output_parser
    result = chain.invoke({"question": query})
    return result


# run server
# uvicorn main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
