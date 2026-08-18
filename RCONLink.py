from mcrcon import MCRcon
import os
import readline

#开头声明
print('配置好RCON即可启用，什么你问我你都能配置RCON了还用这个链接服务器干什么我也不知道我就闲的没事干')
print('配置RCON教程： 在server.properties中设置RCON相关的配置项即可')
print('Github仓库：https://github.com/Tsukigakireine/RCONLink')
print('作者QQ： 1794499532 免费软件 随便分发 本软件造成的任何后果作者不承担，请遵守MIT开源协议')

#信息
SERVER_ADDRESS = input('请输入IP：')
RCON_PORT = int(input('请输入端口：'))
RCON_PASSWORD = input('请输入RCON密码：')

#测试函数
def test_connect():
    try:
        with MCRcon(SERVER_ADDRESS,RCON_PASSWORD,port=RCON_PORT) as mcr:
            mcr.command('list')
            return True
    except:
        return False

#发送命令函数
def send_command(command):
    try:
        with MCRcon(SERVER_ADDRESS, RCON_PASSWORD, port=RCON_PORT) as mcr:
            response = mcr.command(command)
            print(f"[执行] {command}")
            print(f"[返回] {response}")
    except Exception as e:
        print(f"[错误] {e}")

#主循环函数
def main():
    while True:
        command = input(">>>")
        if command == 'leave':
            print('再见！')
            break
        send_command(command)

#连通性测试判断
if test_connect():
    print('连接成功！')
    main()
else:
    back = input('连接失败！请按任意键退出')
