"""
xAI API Client Module
~~~~~~~~~~~~~~~~~~~~

This module provides a client for interacting with the xAI API.
"""

from decouple import config
from openai import OpenAI
from anthropic import Anthropic

class XAIClient:
    def __init__(self):
        self.api_key = config('XAI_API_KEY')
        self.openai_client = OpenAI(
            api_key=self.api_key,
            base_url="https://api.x.ai/v1"
        )
        self.anthropic_client = Anthropic(
            api_key=self.api_key,
            base_url="https://api.x.ai"
        )

    def chat_completion_openai(self, messages, model="grok-beta", stream=False):
        """使用OpenAI SDK进行聊天完成"""
        try:
            completion = self.openai_client.chat.completions.create(
                model=model,
                messages=messages,
                stream=stream
            )
            return completion
        except Exception as e:
            return f"Error: {str(e)}"

    def chat_completion_anthropic(self, messages, system="", model="grok-beta"):
        """使用Anthropic SDK进行聊天完成"""
        try:
            message = self.anthropic_client.messages.create(
                model=model,
                max_tokens=1024,
                system=system,
                messages=messages
            )
            return message
        except Exception as e:
            return f"Error: {str(e)}"

    def create_embedding(self, input_text, model="grok-beta"):
        """创建文本嵌入"""
        try:
            embedding = self.openai_client.embeddings.create(
                model=model,
                input=input_text
            )
            return embedding
        except Exception as e:
            return f"Error: {str(e)}"

    def list_models(self):
        """列出可用模型"""
        try:
            models = self.openai_client.models.list()
            return models
        except Exception as e:
            return f"Error: {str(e)}"
