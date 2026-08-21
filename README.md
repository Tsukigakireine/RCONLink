# RCONLink

> 一个轻量级的游戏服务器 RCON 远程控制终端，支持 Minecraft、Source 引擎及 BattlEye 系列游戏。

[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](LICENSE)

---

## ✨ 功能特性

- **多游戏支持** — 兼容 Minecraft（Java）、Source（L4D2、CS:GO、TF2 等）及 BattlEye（DayZ、ARMA、PUBG 等）引擎
- **交互式终端** — 类 REPL 的命令行交互体验，在 `>>>` 提示符后直接输入指令
- **命令历史** — 方向键（↑/↓）翻阅历史命令，当前会话内有效
- **连通性检测** — 连接前自动测试服务器可达性，快速定位问题
- **快速连接** — 首次输入连接信息后自动保存至 `fastconnect.json`，下次启动可选择一键连接
- **定时任务** — 支持三种定时模式：间隔秒数、每周定时、每月定时，配置存于 `tasks.json`
- **日志记录** — 自动记录所有控制台输出至 `logs/` 文件夹，按时间命名，便于追溯和排错

---

## 🔧 环境要求

- **操作系统**：Windows
- **Python**：>= 3.10
- **网络**：能访问目标服务器的 RCON 端口（TCP）

---

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install rcon mcrcon rcon-battleye loguru pyreadline3
```

### 2. 开启服务器 RCON

#### Minecraft（Java）

编辑 `server.properties`：

```properties
enable-rcon=true
rcon.password=你的密码
rcon.port=你的端口
```

#### Source 引擎游戏（L4D2 / CS:GO / TF2 / GMOD）

编辑 `server.cfg`：

```cfg
rcon_password "你的密码"
rcon_address "0.0.0.0:27015"
```

#### BattlEye 游戏（DayZ / ARMA 2/3 / PUBG）

编辑 `BattlEye/beserver_x64.cfg`：

```cfg
RConPassword 你的密码
RConPort 你的端口
RConIP 0.0.0.0
```

> ⚠️ **安全提示**：RCON 密码请使用强密码，避免明文暴露在公共仓库中。

### 3. 下载 EXE 版本

前往 [Releases](https://github.com/Tsukigakireine/RCONLink/releases) 页面下载最新打包好的 EXE 文件，双击即可运行，无需安装 Python。

---

## 🖥️ 使用方式

### 启动与快速连接

首次启动会提示输入服务器类型、IP、端口和密码，输入后自动保存至 `fastconnect.json`。下次启动时程序会检测到该文件并询问是否使用上次连接信息。

### 交互式命令

成功连接后，终端显示 `>>>` 提示符，直接输入服务器支持的 RCON 命令即可：

```text
>>> status
>>> say 服务器将于5分钟后重启
>>> kick Steve
```

### 命令历史

- **↑（上方向键）**：翻阅上一条命令
- **↓（下方向键）**：翻阅下一条命令

> 历史记录仅在当前会话内有效，关闭程序后不保留。

### 退出程序

在 `>>>` 提示符后输入 `leave` 即可退出，或直接关闭窗口。

---

## 📅 定时任务

定时任务配置文件为 `tasks.json`，支持三种模式：

| 模式 | 关键字段 | 说明 |
|------|----------|------|
| 间隔秒数 | `interval`（秒） | 每隔 N 秒执行一次命令 |
| 每周定时 | `type: "weekly"`、`weekday`、`time` | 每周指定星期几的指定时间执行 |
| 每月定时 | `type: "monthly"`、`day`、`time` | 每月指定日期的指定时间执行 |

**示例 `tasks.json`**：

```json
[
  {
    "name": "每5秒查询玩家",
    "command": "list",
    "interval": 5
  },
  {
    "name": "每周一早安",
    "command": "say 周一早安",
    "type": "weekly",
    "weekday": "monday",
    "time": "08:00"
  },
  {
    "name": "每月15号中午广播",
    "command": "say 月中快乐",
    "type": "monthly",
    "day": 15,
    "time": "12:00"
  }
]
```

> 若 `tasks.json` 不存在，程序会自动生成默认配置并禁用定时任务，重启后生效。

---

## 📝 日志

程序运行时会自动在 `logs/` 文件夹下生成以当前时间命名的 `.log` 文件（如 `2026-08-21_14-30-00.log`），记录所有控制台输出，包括命令执行、返回结果、错误信息及定时任务执行情况。日志文件采用 UTF-8 编码。

---

## 📄 许可证

本项目采用 [GNU 通用公共许可证 v3.0](LICENSE)，详见 [LICENSE](LICENSE) 文件。

---

## 📦 第三方组件

| 组件 | 许可证 | 来源 |
|------|--------|------|
| [rcon](https://pypi.org/project/rcon/) | GPLv3 | https://pypi.org/project/rcon/ |
| [mcrcon](https://pypi.org/project/mcrcon/) | MIT | https://pypi.org/project/mcrcon/ |
| [rcon-battleye](https://pypi.org/project/rcon-battleye/) | MIT | https://pypi.org/project/rcon-battleye/ |
| [loguru](https://pypi.org/project/loguru/) | MIT | https://pypi.org/project/loguru/ |
| [pyreadline3](https://pypi.org/project/pyreadline3/) | BSD | https://pypi.org/project/pyreadline3/ |

详细许可证文本请参见 [THIRD_PARTY_LICENSES.md](THIRD_PARTY_LICENSES.md)。

---

## 👤 作者

**Tsukigakireine**

- GitHub：[@Tsukigakireine](https://github.com/Tsukigakireine)
- 联系方式：QQ 1794499532
- 邮箱：1794499532@qq.com

---

> 💡 **提示**：如果你遇到问题或有功能建议，欢迎提交 [Issue](https://github.com/Tsukigakireine/RCONLink/issues) 或 Pull Request！
