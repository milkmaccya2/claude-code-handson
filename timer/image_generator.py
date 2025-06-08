from openai import OpenAI
import base64
import os

# APIキーを設定（環境変数またはここに直接入力）
api_key = os.getenv("OPENAI_API_KEY") or "your-api-key-here"
client = OpenAI(api_key=api_key)

prompt = """
A children's book drawing of a veterinarian using a stethoscope to 
listen to the heartbeat of a baby otter.
"""

result = client.images.generate(
    model="gpt-image-1",
    prompt=prompt
)

image_base64 = result.data[0].b64_json
image_bytes = base64.b64decode(image_base64)

with open("otter.png", "wb") as f:
    f.write(image_bytes)