"""
Basic usage example of xai-demo package.

This example demonstrates how to:
1. Initialize the xAI client
2. Make chat completions
3. Generate embeddings
4. List available models
"""

from xai_demo.client import XAIClient

def main():
    # Initialize client
    client = XAIClient()
    
    # Chat completion example
    messages = [{"role": "user", "content": "Hello, how are you?"}]
    response = client.chat_completion_openai(messages)
    print("Chat response:", response)
    
    # Embedding example
    text = "This is a sample text for embedding generation."
    embedding = client.create_embedding(text)
    print("Embedding generated:", len(embedding), "dimensions")
    
    # List models
    models = client.list_models()
    print("Available models:", models)

if __name__ == "__main__":
    main()
