import os
# from AppOpener import open
import speech_recognition as sr
import pyttsx3
import openai
from config import apikey
import webbrowser
import vlc
import datetime
import json
import requests

chatStr = ""


def chat(prompt):
    global chatStr
    openai.api_key = apikey
    chatStr += f"Meet: {prompt}\n Jarvis: "
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": chatStr
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
    try:
        say(response["choices"][0]["message"]["content"])
        chatStr += f"{response['choices'][0]['message']['content']}\n"
    except Exception as e:
        print("Sorry Error occurred. Please try again!")

    if not os.path.exists('OpenAi'):
        os.mkdir('OpenAi')

    # with open(f"OpenAi/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
    #     f.write(text)


def getNews():
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=0cee12112fe64148a3ff2513f7b1de52'
    try:
        response = requests.get(url)
        text = json.loads(response.text)
        for i in range(10):
            news = text["articles"][i]["title"]
            say(news)
    except Exception as e:
        say("Internet Connection Error. Please Try again")


def openAi(prompt):
    text = f"chatgpt response for Prompt: {prompt}\n *****************\n\n"
    openai.api_key = apikey
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": prompt
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
    try:
        print(response["choices"][0]["message"]["content"])
        text += response["choices"][0]["message"]["content"]
    except Exception as e:
        print("Sorry Error occurred. Please try again!")

    if not os.path.exists('OpenAi'):
        os.mkdir('OpenAi')

    with open(f"OpenAi/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)


def say(text):
    text_speech = pyttsx3.init();
    text_speech.say(text)
    text_speech.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "Some Error occurred. Sorry from jarvis. "


if __name__ == '__main__':
    say("Hello Meet, what can I do for you?")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["google", "https://www.google.com"], ["find best for you", "https://www.findbestforyou.com"],
                 ["youtube", "https://www.youtube.com"]]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "play music" in query:
            p = vlc.MediaPlayer("Music/scamMusic.mp3")
            p.play()

        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir the time is {hour} hours and {min} minutes.")

        # if "word" in query.lower():
        #     open("word")

        elif "using artificial intelligence ".lower() in query.lower():
            openAi(query)
        elif "stop jarvis".lower() in query.lower():
            exit()
        elif "reset chat".lower() in query.lower():
            chatStr = ""
        elif "news".lower() in query.lower():
            getNews()
        else:
            chat(query)
