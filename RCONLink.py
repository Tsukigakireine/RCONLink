from mcrcon import MCRcon #mc的rcon
from rcon.battleye import Client #be的rcon
import os
import readline
import rcon.source #起源rcon

#开头声明
print('# Copyright (c) 2026 Tsukigakireine')
print('# 本程序是自由软件，遵循 GNU General Public License v3.0')
print('# 详情请参阅 LICENSE 文件')
print('配置好RCON即可启用，什么你问我你都能配置RCON了还用这个链接服务器干什么我也不知道我就闲的没事干')
print('配置RCON教程： 在server.properties中设置RCON相关的配置项即可（此提示仅针对Minecraft，其他游戏服务器请自找教程）')
print('可输入leave离开（需连接服务器后，或者直接点叉关掉窗口也没问题）')
print('Github仓库：https://github.com/Tsukigakireine/RCONLink 在这里获取最新版')
print('作者QQ： 1794499532 免费软件 随便分发 本软件造成的任何后果作者不承担，请遵守GPLv3开源协议')

#判断连接类型
print('[1] 我的世界(Java)')
print('[2] 所有source rcon游戏，比如TF2、求生之路2、CS、GMOD')
print('[3] 所有be rcon游戏，比如DayZ、ARMA 2/3、PUBG')
server = int(input('请选择你的服务器类型（输入数字编号）：'))
#信息
SERVER_ADDRESS = input('请输入IP：')
RCON_PORT = int(input('请输入端口：'))
RCON_PASSWORD = input('请输入RCON密码：')

#——————————测试函数(mc)——————————
def test_connect_mc():
    try:
        with MCRcon(SERVER_ADDRESS,RCON_PASSWORD,port=RCON_PORT) as mcr:
            mcr.command('list')
            return True
    except Exception as e:
        print(f"[错误] {e}")
        return False

#发送命令函数(mc)
def send_command_mc(command):
    try:
        with MCRcon(SERVER_ADDRESS, RCON_PASSWORD, port=RCON_PORT) as mcr:
            response = mcr.command(command)
            print(f"[执行] {command}")
            print(f"[返回] {response}")
    except Exception as e:
        print(f"[错误] {e}")

#——————————测试函数（起源）——————————
def test_connect_source():
    try:
        with rcon.source.Client(SERVER_ADDRESS, RCON_PORT, passwd=RCON_PASSWORD) as client:
            response = client.run("status")
            return True
    except Exception as e:
        print(f"[错误] {e}")
        return False
    
#发送命令函数（起源）
def send_command_source(command):
    try:
        with rcon.source.Client(SERVER_ADDRESS, RCON_PORT, passwd=RCON_PASSWORD) as client:
            response = client.run(command)
            print(f"[执行] {command}")
            print(f"[返回] {response}")
    except Exception as e:
        print(f"[错误] {e}")

#——————————测试函数（BE）——————————
def test_connect_be():
    try:
        with Client(SERVER_ADDRESS, RCON_PORT, passwd=RCON_PASSWORD) as client:
            response = client.run("players")
            return True
    except Exception as e:
        print(f"[错误] {e}")
        return False
    
#发送命令函数（BE）
def send_command_be(command):
    try:
       with Client(SERVER_ADDRESS, RCON_PORT, passwd=RCON_PASSWORD) as client:
            response = client.run(command)
            print(f"[执行] {command}")
            print(f"[返回] {response}")
    except Exception as e:
        print(f"[错误] {e}")


#主循环函数
def main_mc():
    while True:
        command = input(">>>")
        if command == 'leave':
            print('再见！')
            break
        send_command_mc(command)

#主循环函数(起源)
def main_source():
    while True:
        command = input(">>>")
        if command == 'leave':
            print('再见！')
            break
        send_command_source(command)
#主循环函数(BE)
def main_be():
    while True:
        command = input(">>>")
        if command == 'leave':
            print('再见！')
            break
        send_command_be(command)

#主体函数
def start():
    if server == 1:
        if test_connect_mc():
            print('连接成功！')
            main_mc()
        else:
            back = input('连接失败！请按任意键退出')
    elif server == 2:
        if test_connect_source():
            print('连接成功！')
            main_source()
        else:
            back = input('连接失败！请按任意键退出')
    elif server == 3:
        if test_connect_be():
            print('连接成功！')
            main_be()
        else:
            back = input('连接失败！请按任意键退出')

#运行 
start()
