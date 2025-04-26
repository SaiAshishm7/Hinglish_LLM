# Hinglish AI LLM Fine-Tuning Project

This project helps you fine-tune an OpenAI language model (like GPT-3.5 Turbo) using your own Hinglish (Hindi + English) conversational data.

## What does this project do?
- Lets you use your own dataset to make a chatbot that understands and replies in Hinglish.
- Uses OpenAI's API to upload your data and start a fine-tuning job.

## How to use this project

### 1. Set up your environment
- Make sure you have Python 3.7 or above installed.
- Install the required Python packages:
  ```bash
  pip install openai
  ```

### 2. Prepare your dataset
- Your data should be in a file called `dataset.jsonl` in the same folder as the script.
- Each line in `dataset.jsonl` should look like this:
  ```json
  {"prompt": "User: Kaise ho?\nAssistant:", "completion": "Main theek hoon, tum kaise ho?"}
  ```

### 3. Add your OpenAI API key
- Open the `fine_tune.py` file.
- Replace `YOUR-API-KEY-HERE` with your actual OpenAI API key. You can get it from [OpenAI's API Keys page](https://platform.openai.com/api-keys).

### 4. Run the fine-tuning script
- In your terminal, run:
  ```bash
  python fine_tune.py
  ```
- The script will upload your dataset and start the fine-tuning job.
- It will print out the file ID and the fine-tuning job ID.

### 5. Monitor your fine-tuning job
- You can check the status of your job on the [OpenAI dashboard](https://platform.openai.com/).

## Tips & Troubleshooting
- **API Key Error:** Make sure your API key is correct and active.
- **Quota Error:** If you see a quota error, check your OpenAI account's usage and billing settings.
- **File Not Found:** Make sure `dataset.jsonl` is in the same folder as `fine_tune.py`.
- **Model Support:** Fine-tuning is only available for certain models (like `gpt-3.5-turbo-1106`).

## Why did I make this?
I'm a student and wanted to make a Hinglish chatbot that sounds more natural. This project is my way of learning about AI and sharing it with others who want to do the same!

---

## Design Rationale (Why I did what I did)

### Dataset selection & size
I made my own dataset with 20 Hinglish (Hindi + English) chat examples. I picked topics like daily life, food, studies, and fun stuff because that's how we actually talk with friends. I kept it small (20 examples) since I was just testing and learning, and it's easier to spot mistakes in a small set.

### Model & hyperparameter choices
I chose `gpt-3.5-turbo-1106` because it's the latest model that supports fine-tuning and is good at chat. I used the default settings for things like learning rate and epochs because OpenAI recommends them for small datasets, and I didn't want to mess things up as a beginner.

### Prompt formatting & generation settings
I formatted each prompt like a real chat:
```
{"prompt": "User: Tumhara naam kya hai?\nAssistant:", "completion": "Mera naam HinglishBot hai!"}
```
This way, the model learns to reply just like a real assistant in Hinglish. I kept the prompts short and natural, so the bot sounds friendly and not robotic.

### How I'd evaluate quality in production
If I was using this for real, I'd:
- **Ask friends to chat with the bot** and see if the replies make sense and sound natural (human review).
- **Check for mistakes** like wrong language, weird answers, or not following the prompt.

---

## Sample outputs from inference.py
Here are some example outputs from my Hinglish chatbot:

**Input:** User: Aaj mausam kaisa hai?
**Output:** Aaj thoda sa garmi hai, lekin evening mein thanda ho jayega.

**Input:** User: Office kaam kaisa chal raha hai?
**Output:** Kaafi hectic chal raha hai, par handle kar raha hoon.

**Input:** User: Kya Netflix dekh rahe ho?
**Output:** Breaking Bad dekh raha hoon, har episode mein naye twists aate hain!

**Input:** User: Travel plans bana rahe ho kya?
**Output:** Haan, Goa trip plan kar raha hoon. September tak chalna hai.

**Input:** User: Pet ka kya haal hai?
**Output:** Cyrus mast hai, thodi der pehle apni ball ke saath khel raha tha.

As you can see, the bot can handle different topics naturally - from weather and work to entertainment and pets! It uses that casual Hinglish style that we all use in our daily chats. 😊

---


