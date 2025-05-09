import speech_recognition as sr
import os
import webbrowser
import datetime
import json
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from config import apikey
import random
import shlex
import time
import re


chatStr=""

def chat(query):
    global chatStr
    print(chatStr)

    client = MistralClient(api_key=apikey)
    chatStr += f"Meenu: {query}\n Aura: "

    try:
        response = client.chat(
            model="mistral-tiny",
            messages=[ChatMessage(role="user", content=chatStr)],
            temperature=0.5,
            max_tokens=50,  # ✅ Reduced to prevent long replies
            top_p=0.9
        )

        ai_response = response.choices[0].message.content.strip()

        # ✅ Keep responses concise but meaningful
        ai_response = ai_response.split(".")[0] + "."  # Take only the first sentence

        print(f"Aura: {ai_response}")
        say(ai_response)  # Speak the response
        chatStr += f"{ai_response}\n"

        return ai_response

    except Exception as e:
        print(f"❌ Error in AI function: {e}")
        return "Sorry, I encountered an error."

def ai(prompt):
    client = MistralClient(api_key=apikey)

    try:
        # Generate AI response
        response = client.chat(
            model="mistral-tiny",
            messages=[ChatMessage(role="user", content=prompt)],
            temperature=0.7,
            max_tokens=256,
            top_p=1
        )

        ai_response = response.choices[0].message.content.strip()
        text = f"Mistral AI response for Prompt: {prompt} \n*************************\n\n{ai_response}"

        # ✅ Ensure the directory exists
        folder_path = "MistralAI_files"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # ✅ Generate a valid file name
        clean_prompt = prompt.lower().replace("using artificial intelligence", "").strip()
        safe_prompt = re.sub(r'\W+', '_', clean_prompt)  # Replace invalid characters
        file_name = safe_prompt.strip("_") or f"response_{random.randint(1, 999999)}"

        file_path = os.path.join(folder_path, f"{file_name}.txt")

        # ✅ Save AI response
        with open(file_path, "w") as f:
            f.write(text)

        print(f"✅ AI response saved in: {file_path}")

        return ai_response  # ✅ Return AI response for further use

    except Exception as e:
        print(f"❌ Error in AI function: {e}")
        return "Error generating AI response."

def say(text):
    text = shlex.quote(text)
    os.system(f'say -v Allison -r 100 {text} && sleep 1')  # Reduced speed

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.energy_threshold = 300
        print("Listening...")
        try:
            audio = r.listen(source, timeout=10)  # ✅ Set a timeout to prevent infinite waiting
            print('Recognizing...')
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("❌ Could not understand the audio.")
            return ""  # ✅ Return empty string instead of an error
        except sr.RequestError:
            print("❌ Speech Recognition service is down.")
            return ""
        except Exception as e:
            print(f"❌ Error: {e}")
            return ""


if __name__=='__main__':
    print('PyCharm')
    say("Hello I am Aura A.I")
    while True:
        print("Listening...")
        query = takeCommand().lower()  # ✅ Convert to lowercase once for consistency

        # ✅ Dictionary for site shortcuts
        sites = {
            'youtube': 'https://www.youtube.com',
            'wikipedia': 'https://www.wikipedia.com',
            'google': 'https://www.google.com'
        }

        # ✅ Open websites (Stops execution immediately after opening)
        for site_name, site_url in sites.items():
            if f"open {site_name}" in query:
                say(f"Opening {site_name}...")
                webbrowser.open_new_tab(site_url)
                break  # ✅ Stops AI from responding

        else:  # ✅ This runs only if no site was opened
            if 'open music' in query:
                musicPath = '/Users/meenakshi/Downloads/for-her-chill-upbeat.mp3'
                os.system(f"open {musicPath}")

            elif 'the time' in query:
                hour = datetime.datetime.now().strftime("%H")
                minute = datetime.datetime.now().strftime("%M")
                say(f"Sir, the time is {hour} hours {minute} minutes")

            elif "open facetime" in query:
                os.system("open /System/Applications/FaceTime.app")

            elif "open photos" in query:
                os.system("open /System/Applications/Photos.app")

            elif "Using Artificial Intelligence".lower() in query:
                ai(prompt=query)

            elif "quit" in query:
                say("Aura Quitting")
                exit()

            elif "reset chat" in query:
                chatStr = ""

            else:
                chat(query)  # ✅ Run chat **ONLY IF NO OTHER COMMAND MATCHES**

