# 后端（BE）说明

## 项目简介

本目录为 Flask 实现的后端服务，包含用户认证、注册、登录等接口。

## 环境准备

建议使用 Python 3.11 及以上版本。

### 1. 创建虚拟环境

在 BE 目录下执行：

```bash
python3 -m venv venv
```

### 2. 激活虚拟环境

- macOS/Linux:
  ```bash
  source venv/bin/activate
  ```
- Windows:

  ```cmd
  venv\Scripts\activate
  ```

- 请确认解释器路径
  在 VSCode/Cursor 选择 BE/venv/bin/python 作为解释器，确保用的是虚拟环境。

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

## 启动服务

```bash
python app.py
```

## 其他说明

- 所有配置项在 `config.py` 文件中。

## 数据库迁移（Flask-Migrate）

本项目使用 Flask-Migrate 管理数据库结构变更。

### 初始化迁移环境

```bash
flask db init
```

### 生成迁移脚本

```bash
flask db migrate -m "描述信息"
```

### 应用迁移

```bash
flask db upgrade
```

### 回滚迁移

```bash
flask db downgrade
```

> 说明：
>
> - SQLite 数据库文件（如 demo 环境下的 `app.db`）上传 git 便于演示，但生产环境建议忽略。
