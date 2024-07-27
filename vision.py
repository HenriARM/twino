from prompts import system_prompt
import openai


def extract_text(client: openai.OpenAI, image: str, is_base64: bool = False) -> str:
    if is_base64:
        image_url = f"data:image/jpeg;base64,{image}"
    else:
        image_url = image
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url,
                            "detail": "high",
                        },
                    },
                ],
            },
        ],
        # calculated size example.json with tiktoken
        max_tokens=4096,
        temperature=0.2,
        # response_format={"type": "json_object"},
    )

    return response.choices[0].message.content