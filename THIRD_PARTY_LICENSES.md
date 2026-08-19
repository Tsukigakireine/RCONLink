# 第三方组件许可证

本文件汇总了 RCONLink 项目所依赖的第三方开源组件的许可证信息，以确保合规使用。

---

## 目录

- [rcon](#rcon)
- [mcrcon](#mcrcon)
- [pyreadline3](#pyreadline3)
- [许可证全文](#许可证全文)
  - [GNU GPL v3.0](#gnu-gpl-v30)
  - [MIT License](#mit-license)
  - [BSD 3-Clause License](#bsd-3-clause-license)

---

## rcon

| 项目 | 信息 |
|------|------|
| **用途** | RCON 协议客户端库，支持 Source RCON 和 BattlEye RCon 两种协议，负责与游戏服务器建立 RCON 连接并收发指令 |
| **来源** | https://pypi.org/project/rcon/ |
| **原始项目** | https://github.com/conqp/rcon |
| **作者** | Richard Neumann |
| **许可证** | GNU GPL v3.0 |
| **版本要求** | Python >= 3.10 |
| **运行时依赖** | 无 |
| **使用方式** | `pip install rcon`，作为 Python 导入依赖 |
| **项目状态** | 已归档（archived，2025-07 起），仍可使用但不再维护 |

### 许可证声明

> rcon is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. See the full text below.

---

## mcrcon

| 项目 | 信息 |
|------|------|
| **用途** | RCON 协议客户端库（备选/兼容方案），负责与游戏服务器建立 RCON 连接并收发指令 |
| **来源** | https://pypi.org/project/mcrcon/ |
| **原始项目** | https://github.com/Tiiffi/mcrcon （C 语言版本，由 Tiiffi 开发） |
| **PyPI 维护者** | poksiala / aladras |
| **许可证** | MIT License |
| **使用方式** | `pip install mcrcon`，作为 Python 导入依赖 |

### 许可证声明

> mcrcon is licensed under the MIT License. See the full text below.

---

## pyreadline3

| 项目 | 信息 |
|------|------|
| **用途** | Windows 平台下提供交互式命令行功能（方向键历史记录、行编辑等） |
| **来源** | https://pypi.org/project/pyreadline3/ |
| **原始项目** | https://github.com/pyreadline3/pyreadline3 |
| **许可证** | BSD 3-Clause License |
| **使用方式** | `pip install pyreadline3`，仅 Windows 平台需要 |
| **适用范围** | 仅 Windows 系统；Linux / macOS 使用内置 `readline` |

### 许可证声明

> pyreadline3 is licensed under the BSD 3-Clause License. See the full text below.

---

## 许可证全文

### GNU GPL v3.0

> **适用于：rcon**

```
GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007

Copyright (C) 2007 Free Software Foundation, Inc.
Everyone is permitted to copy and distribute verbatim copies of this
license document, but changing it is not allowed.

The full license text is available at:
https://www.gnu.org/licenses/gpl-3.0.txt

----- BEGIN GPLv3 SUMMARY / PREAMBLE -----

The GNU General Public License is a free, copyleft license for
software and other kinds of works.

The licenses for most software and other practical works are designed
to take away your freedom to share and change the works. By contrast,
the GNU General Public License is intended to guarantee your freedom
to share and change all versions of a program--to make sure it remains
free software for all its users. We, the Free Software Foundation,
use the GNU General Public License for most of our software; it
applies also to any other work released this way by its authors. You
can apply it to your programs, too.

When we speak of free software, we are referring to freedom, not
price. Our General Public Licenses are designed to make sure that
you have the freedom to distribute copies of free software (and
charge for them if you wish), that you receive source code or can
get it if you want it, that you can change the software or use
pieces of it in new free programs, and that you know you can do
these things.

To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights. Therefore, you
have certain responsibilities if you distribute copies of the
software, or if you modify it: responsibilities to respect the
freedom of others.

For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received. You must make sure that they, too,
receive or can get the source code. And you must show them these
terms so they know their rights.

Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this
License giving you legal permission to copy, distribute and/or
modify it.

For the full license text, see:
https://www.gnu.org/licenses/gpl-3.0.txt
----- END GPLv3 SUMMARY -----

For the complete legally binding text, refer to the official
GPLv3 document at the URL above. The full text is not reproduced
in-line here to avoid redundancy; the official source is the
canonical reference.
```

> 📌 **注意**：GPLv3 的完整法律文本较长（约 700 行），以上为摘要。如需嵌入完整文本，请从 https://www.gnu.org/licenses/gpl-3.0.txt 获取并保存为 `LICENSE` 文件。本项目仓库根目录的 `LICENSE` 文件即为完整版。

---

### MIT License

> **适用于：mcrcon**

```
MIT License

Copyright (c) 2019 poksiala
Copyright (c) 2019 Tiiffi (original C version)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

### BSD 3-Clause License

> **适用于：pyreadline3**

```
BSD 3-Clause License

Copyright (c) 2020, pyreadline3 contributors
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors
   may be used to endorse or promote products derived from this software
   without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```

---

## 合规说明

- 本项目在分发时（包括源码和打包后的 EXE），均保留上述第三方组件的版权声明和许可证文本。
- 本项目自身采用 **GNU GPL v3**，与所依赖的 `rcon` 模块许可证**完全一致**，可直接作为 GPLv3 项目的一部分分发，无需额外兼容处理。
- `mcrcon` 采用 **MIT License**，属于宽松许可证，与 GPLv3 **兼容**，允许在 GPLv3 项目中使用，只需保留其版权声明。
- `pyreadline3` 采用 **BSD 3-Clause License**，同样与 GPLv3 **兼容**，允许作为依赖使用，只需保留版权声明。
- 由于本项目自身和核心依赖 `rcon` 均为 GPLv3，根据 GPLv3 的「对应源代码」条款：若以二进制形式（如 EXE）分发本项目，必须同时提供完整的对应源代码（Corresponding Source），或在分发时附上 GPLv3 第 6 条所要求的书面承诺。
- 如果你对依赖版本有疑问，可通过以下命令查看当前安装的版本：

```bash
pip show rcon
pip show mcrcon
pip show pyreadline3
```

---

## 更新记录

| 日期 | 变更内容 |
|------|----------|
| 2026-08-19 | 首次创建，收录 mcrcon (MIT) 和 pyreadline3 (BSD) |
| 2026-08-19 | 新增 rcon (GPLv3) 模块信息，更新合规说明以反映 GPLv3 一致性 |
