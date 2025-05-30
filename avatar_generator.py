import requests
from config import DEEPAI_KEY

def generate_avatar(prompt):
    url = "https://api.deepai.org/api/text2img"
    response = requests.post(
        url,
        data={'text': prompt},
        headers={'api-key': DEEPAI_KEY}
    )
    data = response.json()
    return data.get('output_url', "https://via.placeholder.com/512")
