# TOOLS.md - 工具箱

我的核心工具是 `dong-read` CLI。

## 安装

```bash
pipx install dong-read
```

## 命令列表

### 初始化

```bash
dong-read init
```

### 添加摘录

```bash
dong-read add "一句话说得真好"
dong-read add --url "https://example.com"
dong-read add "内容" --url "链接" --source "来源"
dong-read add "AI 相关内容" --tags "AI,技术"
```

### 列出摘录

```bash
dong-read ls                    # 列出所有摘录
dong-read ls --limit 50         # 指定数量
dong-read ls --type quote       # 只摘录
dong-read ls --type link        # 只链接
dong-read ls --tag "AI"         # 按标签筛选
```

### 搜索摘录

```bash
dong-read search "关键词"              # 全字段搜索
dong-read search "关键词" --field content   # 搜索内容
dong-read search "关键词" --field source    # 搜索来源
```

### 获取详情

```bash
dong-read get 123                 # 获取单条摘录
dong-read get 123 --field content # 只获取内容字段
```

### 删除摘录

```bash
dong-read delete 123 --force      # 删除单条
dong-read delete 123 124 125 --force # 批量删除
```

### 查看标签

```bash
dong-read tags              # 列出所有标签及数量
```

### 统计信息

```bash
dong-read stats             # 统计摘录数量、类型分布、标签分布
```

## JSON 输出

所有命令支持 JSON 输出，方便 AI 解析：

```bash
dong-read add "xxx"
dong-read ls
dong-read search "关键词"
dong-read stats
```

## 数据库

数据存储在 `~/.dong/read.db`

---

*📚 收集知识，沉淀智慧*
