import socket
soc=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
soc.connect(('192.168.3.244',2426))
#版本号:包编号:发送者姓名:发送者主机名:命令字:附加信息
msg='11:'+'123:'+'哥哥来玩啊:'+'localhost:'+str(0x00000200)+':hello'
i=1
soc.send(msg.encode())
