import openai
from openai import OpenAI
import os
#
# Set the environment variable within the script (for development purposes)
os.environ['OPENAI_API_KEY'] = 'sk-proj-207qJIZ4VPrEfEzkpTxeT3BlbkFJZ1EQwRMUcF0EEfq11wIt'

openai.api_key = os.environ['OPENAI_API_KEY']

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
)

# Rest of your code
response = client.images.generate(
    prompt="a white siamese cat",
    n=1,
    size="1024x1024"
)

image_url = response['data'][0]['url']
print(f"Generated image URL: {image_url}")
