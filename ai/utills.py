import cohere
from django.conf import settings
import inspect

co = cohere.ClientV2(settings.COHERE_API_KEY)
def generate_blog_article(topic: str) -> str:
    response = co.chat(
        messages=[
            
            {
                "role": "user",
                "content": topic,
            }
        ],
            model="command-xlarge-nightly",
    )

    


    mesaage = dict(response)
    answer = dict(dict(mesaage['message'])['content'])[('type', 'text')][1]
    print("\n\n emoji")
    print(answer)
    print("\n\n emoji")

    return answer






