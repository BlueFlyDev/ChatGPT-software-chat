from openai import OpenAI
import Utils as Tool

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=Tool.getYml("account")["key"],
    base_url=Tool.getYml("account")["url"]
)

def gpt_45_api_stream(messages: list):
    """为提供的对话消息创建新的回答 (流式传输)

    Args:
        messages (list): 完整的对话消息

    Returns:
        str: 生成的回答
    """
    generated_response = ""
    for message in messages:
        content = message['content']
        # 在此处添加你的代码来生成回答
        stream = client.chat.completions.create(
            model='gpt-4-1106-preview',
            messages=[message],
            stream=True,
        )
        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                response = chunk.choices[0].delta.content
                generated_response += response
    return generated_response

def sendMessageChatGPT(info):
    messages = [{'role': 'user','content': info},]
    response = gpt_45_api_stream(messages)
    return response
