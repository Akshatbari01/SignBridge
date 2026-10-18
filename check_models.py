import google.generativeai as genai

genai.configure(api_key="AIzaSyAqw-pK9LjDvDKv5d8xP8Q1Asfdt69XXCs")

print("Available Models:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)