import os
from anthropic import Anthropic

api_key = os.environ.get("ANTHROPIC_API_KEY")
client = Anthropic(api_key=api_key)

response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=10,
    messages=[
        {"role": "user", "content": "."}
    ]
)

print(f"✓ Reset triggered - {response.id}")
