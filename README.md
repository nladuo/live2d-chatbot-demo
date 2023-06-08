# Live2D Chatbot Demo

A live2D Chatbot Demo build with python and js.

![](screenshot.png)

## 使用说明

### 1. 安装依赖
依赖见：requirements.txt


### 2. 配置ChatGPT

见：chatbot_demo.py
``` py
access_token = "浏览器访问https://chat.openai.com/api/auth/session获取"
conversation_id = "xxxxxxx-xxxx-xxxx-xxx-xxxxxxxxxxxx"
```


### 3. 启动前后端服务
```
python live2d_display_server.py
```

### 4. 启动ChatBot
```
python chatbot_demo.py
```