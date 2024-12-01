# xAI API Integration Demo

这是一个集成了xAI API的示例应用程序，展示了如何使用OpenAI和Anthropic兼容的SDK与xAI API进行交互。

## 功能特点

- 支持OpenAI和Anthropic SDK集成
- 聊天完成功能
- 文本嵌入生成
- 模型列表查询
- 友好的Web界面

## 安装说明

1. 克隆仓库：
```bash
git clone <repository-url>
cd xai-integration-demo
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

3. 配置API密钥：
- 复制`.env.example`文件为`.env`
- 在`.env`文件中填入你的xAI API密钥：
```
XAI_API_KEY=your_api_key_here
```

4. 运行应用：
```bash
streamlit run app.py
```

## 使用说明

### 聊天功能
- 在侧边栏选择API类型（OpenAI或Anthropic）
- 在聊天输入框中输入问题
- 查看AI的回复

### 文本嵌入
- 在文本区域输入要进行嵌入的文本
- 点击"生成嵌入"按钮
- 查看生成的嵌入向量

### 模型列表
- 点击"刷新模型列表"按钮
- 查看可用的模型列表

## 注意事项

- 确保API密钥配置正确
- 网络连接正常
- API调用限制和计费说明请参考xAI官方文档

## 技术栈

- Python 3.8+
- Streamlit
- OpenAI Python SDK
- Anthropic Python SDK
- python-decouple
