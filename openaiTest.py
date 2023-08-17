import os
import openai
from config import apikey

openai.api_key = apikey
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "Give me some business ideas. "
    },
    {
      "role": "user",
      "content": ""
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
'''
{
  "id": "chatcmpl-7oUu4Ju3PNIY71jO3KjKyVyEiGeLJ",
  "object": "chat.completion",
  "created": 1692269548,
  "model": "gpt-3.5-turbo-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "1. Virtual event planning and management: With the increasing popularity of virtual events, starting a business that specializes in planning, organizing, and managing virtual conferences, webinars, and team-building activities can be a lucrative venture.\n\n2. Personalized gift creation: Offer customized and unique gift options for various occasions, such as birthdays, weddings, and anniversaries. This can include personalized items like engraved jewelry, custom-made artwork, or bespoke gift boxes.\n\n3. Sustainable clothing line: Start a clothing brand that focuses on eco-friendly and sustainable materials, manufacturing processes, and ethical production. Offer stylish and sustainable alternatives to conventional fashion options.\n\n4. Corporate wellness services: Provide wellness programs and services to businesses, such as workplace yoga classes, mindfulness workshops, and fitness challenges, to promote employee well-being and productivity.\n\n5. Subscription box service: Launch a subscription-based business that offers curated boxes filled with niche products or speciality items, tailored to specific interests like beauty, self-care, cooking, or pet supplies.\n\n6. Bike-sharing platform: Create a platform or mobile app that facilitates the rental and sharing of bicycles to promote eco-friendly transportation options in urban areas.\n\n7. Online tutoring platform: Build a digital platform that connects students with qualified tutors, offering a range of subjects and academic levels"
      },
      "finish_reason": "length"
    }
  ],
  "usage": {
    "prompt_tokens": 18,
    "completion_tokens": 256,
    "total_tokens": 274
  }
}
'''


