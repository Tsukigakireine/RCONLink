from mcrcon import MCRcon #  mc的rcon
from rcon.battleye import Client #  be的rcon
import os
import readline
import time
import datetime
import schedule
import json
import rcon.source #  起源rcon
import threading

#  开头声明
print('#  Copyright (c) 2026 Tsukigakireine')
print('#  本程序是自由软件，遵循 GNU General Public License v3.0')
print('#  详情请参阅 LICENSE 文件')
print('配置教程在仓库的README.md，建议阅读完后使用本程序')
print('反馈问题优先提交issue，其次选择qq（注明来意）')
print('可输入leave离开（需连接服务器后，或者直接点叉关掉窗口也没问题）')
print('Github仓库：https://github.com/Tsukigakireine/RCONLink 在这里获取最新版')
print('作者QQ： 1794499532 免费开源 本软件造成的任何后果作者不承担，请遵守GPLv3开源协议')
print('')

file_fc = ''
#  判断文件是否存在
file_path_fc = "fastconnect.json"
if os.path.exists(file_path_fc):
    print("检测到快速链接配置文件存在，正在进行读取...")
    file_fc = '存在文件'

#  数据内容转换为json并写入
def data_write():
    global data_w
    data_w = {"ip":SERVER_ADDRESS,"port":RCON_PORT,'password':RCON_PASSWORD,'server_type':server_type}
    with open('fastconnect.json', 'w+', encoding='utf-8') as f:
        json.dump(data_w, f, ensure_ascii=False, indent=4)

#  手动输入
def inputdata():
    global SERVER_ADDRESS,RCON_PASSWORD,RCON_PORT,server_type
    print('[1] 我的世界(Java)')
    print('[2] 所有source rcon游戏，比如TF2、求生之路2、CS、GMOD')
    print('[3] 所有be rcon游戏，比如DayZ、ARMA 2/3、PUBG')
    server_type = int(input('请选择你的服务器类型（输入数字编号）：'))
    SERVER_ADDRESS = input('请输入IP：')
    RCON_PORT = int(input('请输入端口：'))
    RCON_PASSWORD = input('请输入RCON密码：')
    data_write()

#  读取json内容并转为data_r并成为全局变量
def data_read():
    global data_r,SERVER_ADDRESS,RCON_PASSWORD,RCON_PORT,server_type
    with open('fastconnect.json', 'r', encoding='utf-8') as f:
        data_r = json.load(f)
    SERVER_ADDRESS = data_r['ip']
    RCON_PORT = data_r['port']
    RCON_PASSWORD = data_r['password']
    server_type = data_r['server_type']

#  读取定时任务
def load_tasks():
    with open('tasks.json', 'r', encoding='utf-8') as f:
        global tasks
        tasks = json.load(f)

#  ——————————测试函数(mc)——————————
def test_connect_mc():
    try:
        with MCRcon(SERVER_ADDRESS,RCON_PASSWORD,port=RCON_PORT) as mcr:
            mcr.command('list')
            return True
    except Exception as e:
        print(f"[错误] {e}")
        return False

#  发送命令函数(mc)
def send_command_mc(command):
    try:
        with MCRcon(SERVER_ADDRESS, RCON_PASSWORD, port=RCON_PORT) as mcr:
            response = mcr.command(command)
            print(f"[执行] {command}")
            print(f"[返回] {response}")
    except Exception as e:
        print(f"[错误] {e}")

#  ——————————测试函数（起源）——————————
def test_connect_source():
    try:
        with rcon.source.Client(SERVER_ADDRESS, RCON_PORT, passwd=RCON_PASSWORD) as client:
            response = client.run("status")
            return True
    except Exception as e:
        print(f"[错误] {e}")
        return False
    
#  发送命令函数（起源）
def send_command_source(command):
    try:
        with rcon.source.Client(SERVER_ADDRESS, RCON_PORT, passwd=RCON_PASSWORD) as client:
            response = client.run(command)
            print(f"[执行] {command}")
            print(f"[返回] {response}")
    except Exception as e:
        print(f"[错误] {e}")

#  ——————————测试函数（BE）——————————
def test_connect_be():
    try:
        with Client(SERVER_ADDRESS, RCON_PORT, passwd=RCON_PASSWORD) as client:
            response = client.run("players")
            return True
    except Exception as e:
        print(f"[错误] {e}")
        return False
    
#  发送命令函数（BE）
def send_command_be(command):
    try:
       with Client(SERVER_ADDRESS, RCON_PORT, passwd=RCON_PASSWORD) as client:
            response = client.run(command)
            print(f"[执行] {command}")
            print(f"[返回] {response}")
    except Exception as e:
        print(f"[错误] {e}")


#  主循环函数
def main_mc():
    while True:
        command = input(">>>")
        if command == 'leave':
            print('再见！')
            break
        send_command_mc(command)

#  主循环函数(起源)
def main_source():
    while True:
        command = input(">>>")
        if command == 'leave':
            print('再见！')
            break
        send_command_source(command)
#  主循环函数(BE)
def main_be():
    while True:
        command = input(">>>")
        if command == 'leave':
            print('再见！')
            break
        send_command_be(command)

def make_scheduled_execute(command):
    #  返回绑定了 command 的函数，避免循环内重复定义
    def execute():
        if server_type == 1:
            send_command_mc(command)
        elif server_type == 2:
            send_command_source(command)
        elif server_type == 3:
            send_command_be(command)
    return execute

#  遍历每个任务，直接读取 name、command、interval（如果存在）
def sche():
    for task in tasks:
        name = task.get('name', '未知任务')
        command = task.get('command')
        if not command:
            print(f"警告: 任务 '{name}' 缺少 command 字段，已跳过")
            continue

        #  ---------- 模式1：间隔秒数（旧格式） ----------
        interval = task.get('interval')
        if interval is not None:
            try:
                interval = float(interval)
            except (ValueError, TypeError):
                print(f"警告: 任务 '{name}' 的 interval 无效，已跳过")
                continue
            schedule.every(interval).seconds.do(make_scheduled_execute(command))
            print(f"已注册定时任务: {name} -> 每 {interval} 秒执行 '{command}'")
            continue

        #  ---------- 模式2：每周定时 ----------
        task_type = task.get('type', '').lower()
        if task_type == 'weekly':
            weekday = task.get('weekday')
            time_str = task.get('time', '00:00')
            #  将 weekday 转为数字（0=周一，6=周日）
            weekday_map = {
                'monday': 0, 'tuesday': 1, 'wednesday': 2,
                'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6
            }
            if isinstance(weekday, str):
                weekday_num = weekday_map.get(weekday.lower())
            else:
                weekday_num = int(weekday) if weekday is not None else None
            if weekday_num is None or not (0 <= weekday_num <= 6):
                print(f"警告: 任务 '{name}' 的 weekday 无效，已跳过")
                continue
            #  验证时间格式
            try:
                hour, minute = map(int, time_str.split(':'))
                if not (0 <= hour < 24 and 0 <= minute < 60):
                    raise ValueError
            except:
                print(f"警告: 任务 '{name}' 的 time 格式无效，已跳过")
                continue
            #  使用 schedule 的 weekly + weekday 链式调用
            #  schedule 的 weekday 是属性，用 getattr
            job = getattr(schedule.every().weeks, list(weekday_map.keys())[weekday_num])
            job = job.at(time_str)
            job.do(make_scheduled_execute(command))
            print(f"已注册定时任务: {name} -> 每周 {weekday} {time_str} 执行 '{command}'")
            continue

        #  ---------- 模式3：每月定时 ----------
        if task_type == 'monthly':
            day = task.get('day')
            time_str = task.get('time', '00:00')
            try:
                day = int(day)
                if not (1 <= day <= 31):
                    print(f"警告: 任务 '{name}' 的 day 应在1~31之间，已跳过")
                    continue
            except (ValueError, TypeError):
                print(f"警告: 任务 '{name}' 的 day 无效，已跳过")
                continue
            try:
                hour, minute = map(int, time_str.split(':'))
                if not (0 <= hour < 24 and 0 <= minute < 60):
                    raise ValueError
            except:
                print(f"警告: 任务 '{name}' 的 time 格式无效，已跳过")
                continue

            #  schedule 没有直接支持每月某日，采用每日检查的方式
            #  每天在指定时间检查日期是否匹配
            def monthly_check(command, target_day):
                now = datetime.datetime.now()
                if now.day == target_day:
                    make_scheduled_execute(command)()  #   直接执行
            schedule.every().day.at(time_str).do(monthly_check, command, day)
            print(f"已注册定时任务: {name} -> 每月第{day}天 {time_str} 执行 '{command}'")
            continue

        #  如果走到这里，说明任务类型无法识别
        print(f"警告: 任务 '{name}' 的类型或参数不完整，已跳过")

#  主体函数
def start():
    if server_type == 1:
        if test_connect_mc():
            print('连接成功！')
            main_mc()
        else:
            input('连接失败！请按任意键退出')
    elif server_type == 2:
        if test_connect_source():
            print('连接成功！')
            main_source()
        else:
            input('连接失败！请按任意键退出')
    elif server_type == 3:
        if test_connect_be():
            print('连接成功！')
            main_be()
        else:
            input('连接失败！请按任意键退出')

#  定时任务主循环函数
def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)
scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
scheduler_thread.start()

if file_fc == '存在文件':
    print('检测到存在快速链接配置文件，是否使用上次链接方式？')
    print('[1] 链接上次链接的服务器')
    print('[2] 不链接上次链接方式，手动输入地址')
    connect_choose = int(input('请输入数字编号: '))
    if connect_choose == 1:
        data_read()
    elif connect_choose == 2:
        inputdata()
    else:
        print('输入无效，将使用手动输入方式')
        inputdata()
else:
    inputdata()

#  判断文件是否存在
file_path = "tasks.json"
if os.path.exists(file_path):
    print("配置文件存在，正在进行读取...")
    load_tasks()
    sche()
    print('定时指令已开启！')
    start()
else:
    print("定时指令配置文件不存在，正在生成默认配置文件...")
    print('定时指令配置文件已生成，本次程序已禁用定时指令，重启程序后可开启定时指令')
    default_tasks = [
        {
            "name": "测试任务1",
            "command": "list",
            "interval": 5
        },
        {
            "name": "每周一早上8点",
            "command": "say 周一早安",
            "type": "weekly",
            "weekday": "monday",
            "time": "08:00"
        },
        {
            "name": "每月15号中午",
            "command": "say 月中",
            "type": "monthly",
            "day": 15,
            "time": "12:00"
        }
    ]
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(default_tasks, f, ensure_ascii=False, indent=4)
    tasks = default_tasks
    start()
