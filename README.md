# Aura AI - Generative AI-Powered Voice-Activated Chatbot

Aura AI is a voice-activated chatbot built using Python and Mistral AI, capable of understanding spoken commands, generating intelligent responses, executing basic system functions, and saving generated content to structured text files. It aims to blend traditional voice assistant features with generative AI capabilities for a smooth and interactive user experience.

## 🔮 Features

- 🎤 Voice input using `SpeechRecognition`
- 🤖 Conversational responses using `Mistral-Tiny` model
- 📁 Auto-saving AI-generated content as `.txt` files
- 🌐 System-level command execution (e.g., opening websites, apps)
- 🗣️ Spoken responses via macOS `say` command
- 💡 Modular and extensible design for future upgrades

---

## 📁 Project Structure

```
├── aura_ai.py           # Main script  
├── config.py            # Contains API key  
├── MistralAI_files/     # Folder where AI responses are saved  
├── README.md            # Project documentation  
```


---

## ⚙️ Requirements

- Python 3.7+
- MacOS (due to use of `say` command)
- Libraries:
  - `speech_recognition`
  - `mistralai`
  - `datetime`
  - `webbrowser`
  - `os`
  - `shlex`
  - `re`

Install dependencies using:

```bash
pip install speechrecognition mistralai

## 🚀 Getting Started

```bash
# Clone the repository
git clone https://github.com/your-username/aura-ai.git
cd aura-ai
```

```python
# Add your Mistral API key to config.py
apikey = "your_mistral_api_key"
```

```bash
# Run the assistant
python aura_ai.py
```

### 🎙️ Speak a command like:
- "Open YouTube"
- "What is artificial intelligence?"
- "Using artificial intelligence write a poem"
- "Open FaceTime"
- "Quit"
```

---

## 🧠 Example Prompts

```text
Query: “Using artificial intelligence write an essay on climate change.”
→ Response saved to MistralAI_files/climate_change.txt

Command: “Open Google”
→ Opens browser tab with Google.

Chat Mode: “Tell me a joke.”
→ Mistral generates a short response, spoken via TTS.
```

---

## ✅ Tested Scenarios

```yaml
- Voice command recognition (in both quiet and noisy environments)
- Handling unrecognized or partial commands
- Generating and saving structured AI responses
- Executing system-level functions on macOS
- Multi-turn chat continuity
```

---

## 🔒 Notes

```text
- Currently compatible with macOS due to `say` voice output.
- For other OS platforms, modify the `say()` function using `pyttsx3` or equivalent.
- Model used: `mistral-tiny` (adjustable via the API)
```

---

## 📌 Future Enhancements

```yaml
- Add cross-platform TTS support
- Incorporate GUI for easier interactions
- Enable dynamic skill loading (e.g., calendar, email)
```

---

## 🤝 Contributions

```text
Pull requests are welcome. For major changes, please open an issue first to discuss.
```

---

## 📄 License

```text
This project is licensed under the MIT License.
```

---

## 🙋‍♀️ Author

```yaml
Meenakshi S Menon  
CSE (AIML), VIT Bhopal University
```





