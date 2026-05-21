<div align="center">

# 📝 NoteNest

**Intelligent Markdown Note Manager | 智能Markdown笔记管理工具**

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-orange)](requirements.txt)

[English](#english) | [简体中文](#简体中文) | [繁體中文](#繁體中文)

</div>

---

## English

### 🎉 Introduction

**NoteNest** is an intelligent Markdown note management tool designed for developers, writers, and knowledge workers who value **privacy**, **speed**, and **simplicity**.

Inspired by the growing need for local-first note-taking solutions, NoteNest offers a zero-dependency Python implementation that puts you in complete control of your data. No cloud, no tracking, no bloat — just your thoughts, organized.

**Key Differentiators:**
- 🚀 **Zero Dependencies**: Pure Python standard library, no pip install hell
- 🧠 **Smart Tagging**: Automatic tag extraction from YAML frontmatter and inline hashtags
- 🔍 **Intelligent Search**: Full-text search with relevance scoring
- 🔗 **WikiLinks Support**: Connect your thoughts with `[[Note Links]]`
- 🏠 **Local-First**: Your data stays on your machine, always
- ⚡ **Lightning Fast**: Instant search across thousands of notes

### ✨ Core Features

| Feature | Description | Emoji |
|---------|-------------|-------|
| **Smart Tag Extraction** | Auto-detects tags from YAML frontmatter, hashtags (#tag), and frontmatter lists | 🏷️ |
| **Full-Text Search** | Search titles, tags, and content with intelligent relevance scoring | 🔍 |
| **WikiLinks** | Create connections between notes using `[[Note Title]]` syntax | 🔗 |
| **Beautiful CLI** | Emoji-enhanced terminal interface for pleasant interaction | ✨ |
| **Zero Config** | Works out of the box, sensible defaults | 🎯 |
| **Privacy First** | No internet required, no data leaves your machine | 🔒 |

### 🚀 Quick Start

#### Requirements
- Python 3.7 or higher
- No additional dependencies required!

#### Installation

```bash
# Clone the repository
git clone https://github.com/gitstq/NoteNest.git
cd NoteNest

# Make it executable (optional)
chmod +x notenest.py

# Create a symlink for global access (optional)
ln -s $(pwd)/notenest.py /usr/local/bin/notenest
```

#### Usage

```bash
# Create a new note
python3 notenest.py create "My First Note" --tags "ideas,project"

# Search notes
python3 notenest.py search "python"

# List all notes
python3 notenest.py list

# List notes by tag
python3 notenest.py list --tag "project"

# Show statistics
python3 notenest.py stats

# Rebuild search index
python3 notenest.py rebuild
```

### 📖 Detailed Usage Guide

#### Creating Notes

Notes are created with YAML frontmatter automatically:

```bash
python3 notenest.py create "Meeting Notes" --tags "work,meeting" --content "Discussed Q4 goals..."
```

This creates:
```markdown
---
title: "Meeting Notes"
created: 2026-05-21T10:30:00
modified: 2026-05-21T10:30:00
tags:
  - work
  - meeting
---

Discussed Q4 goals...
```

#### Tag Formats Supported

NoteNest automatically detects tags in multiple formats:

1. **YAML Frontmatter**:
   ```yaml
   tags:
     - python
     - tutorial
   ```

2. **Inline Hashtags**:
   ```markdown
   This is a note about #python and #coding
   ```

3. **Frontmatter List**:
   ```yaml
   tags: [python, tutorial, beginner]
   ```

#### WikiLinks

Connect your notes:

```markdown
See also: [[Related Note]] and [[Another Topic]]
```

Links are indexed and searchable.

### 💡 Design Philosophy

**Why NoteNest?**

In an era of cloud-everything, we believe your personal notes deserve to stay personal. NoteNest is built on these principles:

1. **Simplicity**: Do one thing well — manage Markdown notes
2. **Privacy**: Local-first architecture, no network calls
3. **Portability**: Single Python file, run anywhere
4. **Speed**: Instant operations, no waiting
5. **Openness**: MIT licensed, hackable source code

### 📦 Project Type

This is a **CLI Tool/Library** project. No executable release required.

### 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 简体中文

### 🎉 项目介绍

**NoteNest** 是一款智能 Markdown 笔记管理工具，专为重视**隐私**、**速度**和**简洁**的开发者、写作者和知识工作者设计。

受到本地优先笔记解决方案需求的启发，NoteNest 提供了一个零依赖的 Python 实现，让您完全掌控自己的数据。没有云端、没有追踪、没有臃肿——只有您的想法，井井有条。

**核心差异化亮点：**
- 🚀 **零依赖**：纯 Python 标准库，无需 pip 安装地狱
- 🧠 **智能标签**：自动从 YAML 前置元数据和行内标签提取标签
- 🔍 **智能搜索**：全文搜索，支持相关性评分
- 🔗 **WikiLinks 支持**：使用 `[[笔记链接]]` 连接您的思维
- 🏠 **本地优先**：您的数据始终保存在您的机器上
- ⚡ **极速体验**：数千条笔记中瞬间搜索

### ✨ 核心特性

| 特性 | 描述 | 图标 |
|---------|-------------|-------|
| **智能标签提取** | 自动检测 YAML 前置元数据、话题标签 (#tag) 和前置元数据列表中的标签 | 🏷️ |
| **全文搜索** | 搜索标题、标签和内容，智能相关性评分 | 🔍 |
| **WikiLinks** | 使用 `[[笔记标题]]` 语法创建笔记间的连接 | 🔗 |
| **美观的 CLI** | 表情符号增强的终端界面，交互体验愉悦 | ✨ |
| **零配置** | 开箱即用，合理的默认设置 | 🎯 |
| **隐私优先** | 无需联网，数据不会离开您的机器 | 🔒 |

### 🚀 快速开始

#### 环境要求
- Python 3.7 或更高版本
- 无需额外依赖！

#### 安装

```bash
# 克隆仓库
git clone https://github.com/gitstq/NoteNest.git
cd NoteNest

# 设置为可执行（可选）
chmod +x notenest.py

# 创建全局访问的软链接（可选）
ln -s $(pwd)/notenest.py /usr/local/bin/notenest
```

#### 使用

```bash
# 创建新笔记
python3 notenest.py create "我的第一条笔记" --tags "想法,项目"

# 搜索笔记
python3 notenest.py search "python"

# 列出所有笔记
python3 notenest.py list

# 按标签列出笔记
python3 notenest.py list --tag "项目"

# 显示统计信息
python3 notenest.py stats

# 重建搜索索引
python3 notenest.py rebuild
```

### 📖 详细使用指南

#### 创建笔记

笔记会自动创建 YAML 前置元数据：

```bash
python3 notenest.py create "会议记录" --tags "工作,会议" --content "讨论了 Q4 目标..."
```

这会创建：
```markdown
---
title: "会议记录"
created: 2026-05-21T10:30:00
modified: 2026-05-21T10:30:00
tags:
  - 工作
  - 会议
---

讨论了 Q4 目标...
```

#### 支持的标签格式

NoteNest 自动检测多种格式的标签：

1. **YAML 前置元数据**：
   ```yaml
   tags:
     - python
     - 教程
   ```

2. **行内话题标签**：
   ```markdown
   这是一篇关于 #python 和 #编程 的笔记
   ```

3. **前置元数据列表**：
   ```yaml
   tags: [python, 教程, 入门]
   ```

#### WikiLinks

连接您的笔记：

```markdown
另请参阅：[[相关笔记]] 和 [[另一个主题]]
```

链接会被索引并可搜索。

### 💡 设计理念

**为什么选择 NoteNest？**

在万物云端的时代，我们相信您的个人笔记应该保持私密。NoteNest 基于以下原则构建：

1. **简洁**：把一件事做好——管理 Markdown 笔记
2. **隐私**：本地优先架构，无网络调用
3. **可移植**：单个 Python 文件，随处运行
4. **速度**：即时操作，无需等待
5. **开放**：MIT 许可证，可修改的源代码

### 📦 项目类型

这是一个 **CLI 工具/库** 项目。无需发布可执行文件。

### 🤝 贡献指南

欢迎贡献！请随时提交 Pull Request。

1. Fork 本仓库
2. 创建您的功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

### 📄 开源协议

基于 MIT 协议分发。更多信息请参见 `LICENSE` 文件。

---

## 繁體中文

### 🎉 專案介紹

**NoteNest** 是一款智慧 Markdown 筆記管理工具，專為重視**隱私**、**速度**和**簡潔**的開發者、寫作者和知識工作者設計。

受到本地優先筆記解決方案需求的啟發，NoteNest 提供了一個零依賴的 Python 實現，讓您完全掌控自己的資料。沒有雲端、沒有追蹤、沒有臃腫——只有您的想法，井井有條。

**核心差異化亮點：**
- 🚀 **零依賴**：純 Python 標準庫，無需 pip 安裝地獄
- 🧠 **智慧標籤**：自動從 YAML 前置元資料和行內標籤提取標籤
- 🔍 **智慧搜尋**：全文搜尋，支援相關性評分
- 🔗 **WikiLinks 支援**：使用 `[[筆記連結]]` 連接您的思維
- 🏠 **本地優先**：您的資料始終保存在您的機器上
- ⚡ **極速體驗**：數千條筆記中瞬間搜尋

### ✨ 核心特性

| 特性 | 描述 | 圖示 |
|---------|-------------|-------|
| **智慧標籤提取** | 自動偵測 YAML 前置元資料、話題標籤 (#tag) 和前置元資料清單中的標籤 | 🏷️ |
| **全文搜尋** | 搜尋標題、標籤和內容，智慧相關性評分 | 🔍 |
| **WikiLinks** | 使用 `[[筆記標題]]` 語法建立筆記間的連接 | 🔗 |
| **美觀的 CLI** | 表情符號增強的終端介面，互動體驗愉悅 | ✨ |
| **零配置** | 開箱即用，合理的預設設定 | 🎯 |
| **隱私優先** | 無需連網，資料不會離開您的機器 | 🔒 |

### 🚀 快速開始

#### 環境要求
- Python 3.7 或更高版本
- 無需額外依賴！

#### 安裝

```bash
# 克隆倉庫
git clone https://github.com/gitstq/NoteNest.git
cd NoteNest

# 設定為可執行（可選）
chmod +x notenest.py

# 建立全域訪問的軟連結（可選）
ln -s $(pwd)/notenest.py /usr/local/bin/notenest
```

#### 使用

```bash
# 建立新筆記
python3 notenest.py create "我的第一條筆記" --tags "想法,專案"

# 搜尋筆記
python3 notenest.py search "python"

# 列出所有筆記
python3 notenest.py list

# 按標籤列出筆記
python3 notenest.py list --tag "專案"

# 顯示統計資訊
python3 notenest.py stats

# 重建搜尋索引
python3 notenest.py rebuild
```

### 📖 詳細使用指南

#### 建立筆記

筆記會自動建立 YAML 前置元資料：

```bash
python3 notenest.py create "會議記錄" --tags "工作,會議" --content "討論了 Q4 目標..."
```

這會建立：
```markdown
---
title: "會議記錄"
created: 2026-05-21T10:30:00
modified: 2026-05-21T10:30:00
tags:
  - 工作
  - 會議
---

討論了 Q4 目標...
```

#### 支援的標籤格式

NoteNest 自動偵測多種格式的標籤：

1. **YAML 前置元資料**：
   ```yaml
   tags:
     - python
     - 教學
   ```

2. **行內話題標籤**：
   ```markdown
   這是一篇關於 #python 和 #程式設計 的筆記
   ```

3. **前置元資料清單**：
   ```yaml
   tags: [python, 教學, 入門]
   ```

#### WikiLinks

連接您的筆記：

```markdown
另請參閱：[[相關筆記]] 和 [[另一個主題]]
```

連結會被索引並可搜尋。

### 💡 設計理念

**為什麼選擇 NoteNest？**

在萬物雲端的時代，我們相信您的個人筆記應該保持私密。NoteNest 基於以下原則構建：

1. **簡潔**：把一件事做好——管理 Markdown 筆記
2. **隱私**：本地優先架構，無網路呼叫
3. **可移植**：單個 Python 檔案，隨處執行
4. **速度**：即時操作，無需等待
5. **開放**：MIT 授權，可修改的原始碼

### 📦 專案類型

這是一個 **CLI 工具/庫** 專案。無需發布可執行檔案。

### 🤝 貢獻指南

歡迎貢獻！請隨時提交 Pull Request。

1. Fork 本倉庫
2. 建立您的功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

### 📄 開源協議

基於 MIT 協議分發。更多資訊請參見 `LICENSE` 檔案。

---

<div align="center">

**Made with ❤️ by the NoteNest Community**

[Report Bug](https://github.com/gitstq/NoteNest/issues) · [Request Feature](https://github.com/gitstq/NoteNest/issues)

</div>
