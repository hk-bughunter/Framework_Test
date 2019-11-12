import time,threading
import websocket

#连接websocket服务端
# ws=websocket.create_connection("ws://echo.websocket.org")
# ws.send("hello")
# msg=ws.recv()
# print(msg)
# if msg=="hello":
#     print("成功")
# else:
#     print("失败")

#建立websocket客户端
# def when_open(ws):
#     print("建立连接")
#     def run():
#         while True:
#             msg=input("请输入内容")
#             ws.send(msg)
#             time.sleep(1)
#
#             if msg=="close":
#                 ws.close()
#                 break
#     threading.Thread(target=run).start()
# def when_message(ws,msg):
#     print("接收到的消息："+msg)
# def when_close(ws):
#     print("关闭连接")
# ws=websocket.WebSocketApp("ws://echo.websocket.org",on_open=when_open,
#                           on_message=when_message,
#                           on_close=when_close)
# ws.run_forever()
