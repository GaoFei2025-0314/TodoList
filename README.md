# TodoList - 待办事项管理应用

一个简洁的待办事项管理应用，使用Flask构建，支持中文界面，具有现代化的UI设计。

## 功能特性

- ✅ 添加新的待办事项
- ✅ 标记待办事项为完成/未完成
- ✅ 删除待办事项
- ✅ 实时更新待办事项数量
- ✅ 响应式设计，适配各种设备
- ✅ 现代化UI界面，使用Bootstrap 5和自定义CSS

## 技术栈

- **后端**: Flask 2.3.3
- **数据库**: SQLAlchemy 3.0.5 (SQLite)
- **前端**: Jinja2模板, Bootstrap 5.3, jQuery 3.6
- **语言**: Python 3.11+

## 安装与运行

### 前置条件

- Python 3.11+
- pip 包管理器

### 安装步骤

1. **克隆仓库**
```bash
git clone https://github.com/GaoFei2025-0314/TodoList.git
cd TodoList
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **运行应用**
```bash
python app.py
```

4. **访问应用**
打开浏览器访问: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 项目结构

```
TodoList/
├── app.py                 # Flask应用主文件
├── database.py            # SQLAlchemy模型定义
├── requirements.txt       # 项目依赖
├── static/
│   └── style.css          # 自定义样式
└── templates/
    └── index.html         # 主页面模板
```

## API端点

应用提供了RESTful API接口：

- `GET /api/todos` - 获取所有待办事项
- `POST /api/todos` - 创建新的待办事项
- `PUT /api/todos/<int:todo_id>` - 更新待办事项状态
- `DELETE /api/todos/<int:todo_id>` - 删除待办事项

## 使用说明

1. 在输入框中输入待办事项内容
2. 按 Enter 键或点击添加按钮创建新事项
3. 点击复选框标记事项为完成/未完成
4. 点击删除按钮移除事项

## 开发说明

- 数据库文件保存在 `instance/todos.db`
- 应用使用调试模式运行
- 包含调试输出信息（可在生产环境中移除）

## 贡献

欢迎提交Issue和Pull Request来改进这个项目。

## 许可证

MIT License - 详见LICENSE文件（如果存在）