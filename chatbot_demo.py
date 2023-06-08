from pyutils.live2d_control import tts_and_play_audio
import warnings
warnings.filterwarnings("ignore")

from revChatGPT.V1 import Chatbot

access_token = "浏览器访问https://chat.openai.com/api/auth/session获取"
conversation_id = ""

chatbot = Chatbot(config={"access_token": access_token}, conversation_id=conversation_id)

def ask(prompt):
    for data in chatbot.ask(prompt):
        response = data["message"]
    return response

while True:
    q = input("输入问题:")
    res = ask(q)
    print(res)
    tts_and_play_audio(res)
    
