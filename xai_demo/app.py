"""
Streamlit Web Application
~~~~~~~~~~~~~~~~~~~~~~~

This module provides a web interface for interacting with the xAI API.
"""

import streamlit as st
from .client import XAIClient

def init_session_state():
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'client' not in st.session_state:
        st.session_state.client = XAIClient()

def main():
    st.title("xAI API Integration Demo")
    init_session_state()

    # 侧边栏配置
    st.sidebar.title("配置")
    api_choice = st.sidebar.radio(
        "选择API类型",
        ["OpenAI Compatible", "Anthropic Compatible"]
    )
    
    # 主要功能区域
    tab1, tab2, tab3 = st.tabs(["聊天", "嵌入", "模型列表"])
    
    # 聊天标签页
    with tab1:
        st.header("与Grok对话")
        
        # 显示历史消息
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # 输入区域
        if prompt := st.chat_input("输入你的问题..."):
            # 添加用户消息
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # 获取AI响应
            with st.chat_message("assistant"):
                if api_choice == "OpenAI Compatible":
                    response = st.session_state.client.chat_completion_openai(
                        st.session_state.messages
                    )
                    if isinstance(response, str) and response.startswith("Error"):
                        st.error(response)
                    else:
                        content = response.choices[0].message.content
                        st.markdown(content)
                        st.session_state.messages.append({"role": "assistant", "content": content})
                else:
                    messages = [{"role": m["role"], "content": m["content"]} 
                              for m in st.session_state.messages]
                    response = st.session_state.client.chat_completion_anthropic(
                        messages=messages,
                        system="You are Grok, a chatbot inspired by the Hitchhiker's Guide to the Galaxy."
                    )
                    if isinstance(response, str) and response.startswith("Error"):
                        st.error(response)
                    else:
                        content = response.content
                        st.markdown(content)
                        st.session_state.messages.append({"role": "assistant", "content": content})

    # 嵌入标签页
    with tab2:
        st.header("文本嵌入")
        text_input = st.text_area("输入要进行嵌入的文本:")
        if st.button("生成嵌入"):
            if text_input:
                with st.spinner("生成嵌入中..."):
                    embedding = st.session_state.client.create_embedding(text_input)
                    if isinstance(embedding, str) and embedding.startswith("Error"):
                        st.error(embedding)
                    else:
                        st.success("嵌入生成成功!")
                        st.json(embedding.model_dump())
            else:
                st.warning("请输入文本")

    # 模型列表标签页
    with tab3:
        st.header("可用模型列表")
        if st.button("刷新模型列表"):
            with st.spinner("获取模型列表..."):
                models = st.session_state.client.list_models()
                if isinstance(models, str) and models.startswith("Error"):
                    st.error(models)
                else:
                    st.json(models.model_dump())

if __name__ == "__main__":
    main()
