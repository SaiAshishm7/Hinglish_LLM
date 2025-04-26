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
