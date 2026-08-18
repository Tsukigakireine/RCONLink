# RCONLink

一个轻量级的游戏服务器 RCON 远程控制终端，支持 Minecraft 及 Source 引擎游戏（如 Left 4 Dead 2、CS:GO 等）。

## 功能

- 通过 RCON 协议远程连接游戏服务器
- 发送任意指令（如 `list`、`say`、`status`、`changelevel` 等）
- 方向键翻阅命令历史（当前会话有效）
- 连通性自动测试
- 支持自定义图标和版本信息的 EXE 打包

## 依赖

- Python 3.x
- [mcrcon](https://pypi.org/project/mcrcon/)（RCON 协议客户端库）
- (Windows 用户) [pyreadline3](https://pypi.org/project/pyreadline3/)（方向键历史记录支持）

安装所有依赖：

```bash
pip install mcrcon pyreadline3
```

## 使用方法

### 1. 开启服务器 RCON

**Minecraft**：在 `server.properties` 中设置：

```
enable-rcon=true
rcon.password=你的密码
rcon.port=25575
```

**Left 4 Dead 2**：在 `server.cfg` 中设置：

```
rcon_password "你的密码"
```

> 注意：L4D2 的 RCON 端口默认与游戏端口相同（通常为 `27015`）。

### 2. 运行脚本

```bash
python RCONLink.py
```

### 3. 按提示操作

- 输入服务器 IP
- 输入 RCON 端口
- 输入 RCON 密码
- 连接成功后，在 `>>>` 提示符后输入指令即可

### 4. 退出

输入 `leave` 即可退出程序。

## 打包为 EXE

如需分发给不会 Python 的用户，可使用 PyInstaller 打包：

```bash
pip install pyinstaller
pyinstaller --onefile --console --icon=icon.ico --version-file=version_info.txt RCONLink.py
```

打包完成后，EXE 文件位于 `dist/` 文件夹中。

### 自定义图标

将图标文件命名为 `icon.ico`，放在脚本同一目录下，打包时通过 `--icon=icon.ico` 指定即可。

### 自定义版本信息

创建 `version_info.txt` 文件，内容参考 PyInstaller 官方文档的版本信息模板，打包时通过 `--version-file=version_info.txt` 指定。

## 常用 RCON 命令参考

### Minecraft

| 命令 | 说明 |
|------|------|
| `list` | 查看在线玩家 |
| `say 消息` | 广播消息 |
| `stop` | 关闭服务器 |
| `kick 玩家名` | 踢出玩家 |
| `ban 玩家名` | 封禁玩家 |
| `op 玩家名` | 给予管理员权限 |
| `gamemode 模式 玩家名` | 切换游戏模式 |

### Left 4 Dead 2 / Source 引擎

| 命令 | 说明 |
|------|------|
| `status` | 查看服务器和玩家信息 |
| `changelevel 地图名` | 切换地图 |
| `kick 玩家名` | 踢出玩家 |
| `banid 0 玩家ID` | 封禁玩家 |
| `say 消息` | 广播消息 |
| `sv_cheats 1` | 开启作弊（仅管理员） |
| `mp_gamemode versus` | 切换为对抗模式 |

## 许可证

本项目采用 MIT 许可证，详见 [LICENSE](LICENSE)。

## 第三方组件

| 组件 | 许可证 | 来源 |
|------|--------|------|
| [mcrcon](https://pypi.org/project/mcrcon/) | MIT | https://pypi.org/project/mcrcon/ |
| [pyreadline3](https://pypi.org/project/pyreadline3/) | BSD | https://pypi.org/project/pyreadline3/ |

## 致谢

感谢 mcrcon、pyreadline3 等开源项目的作者。

## 作者

QQ：1794499532

欢迎传播、二次开发，但请保留原作者信息。
