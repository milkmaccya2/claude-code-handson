from openai import OpenAI
import base64
import os

# APIキーを設定（環境変数またはここに直接入力）
api_key = os.getenv("OPENAI_API_KEY") or "your-api-key-here"
client = OpenAI(api_key=api_key)

prompt = """
A cute kawaii-style cat with big sparkling eyes, wearing a tiny digital watch on its paw, 
sitting next to an hourglass timer. The cat has fluffy orange and white fur, 
a cheerful expression, and is surrounded by small floating clock icons and sparkles. 
Anime-inspired art style with soft pastel colors and adorable features.
"""

result = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1024x1024",
    quality="standard"
)

image_url = result.data[0].url

# URLから画像をダウンロード
import requests
response = requests.get(image_url)
with open("timer_cat.png", "wb") as f:
    f.write(response.content)

print("可愛い猫の画像が生成されました: timer_cat.png")