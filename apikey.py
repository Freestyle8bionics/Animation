from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "write a haiku about ai"}
  ]
)

print(completion.choices[0].message)
