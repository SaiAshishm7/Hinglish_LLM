import openai

# Step 1: Set your OpenAI API key
# Replace 'YOUR-API-KEY-HERE' with your actual OpenAI API key
openai.api_key = "YOUR-API-KEY-HERE"

# Step 2: Specify your fine-tuned model's ID
# Replace 'YOUR-FINE-TUNED-MODEL-ID' with the ID of your fine-tuned model
fine_tuned_model = "YOUR-FINE-TUNED-MODEL-ID"

# Step 3: Create a prompt for inference
# Here we're defining a conversation with roles: system, user, assistant
prompt_messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello, how are you?"}
]

# Step 4: Make a request to the fine-tuned model
try:
    print("Sending request to fine-tuned model...")
    response = openai.ChatCompletion.create(
        model=fine_tuned_model,  # Use the fine-tuned model ID
        messages=prompt_messages  # Provide the conversation context
    )

    # Step 5: Extract and print the assistant's response
    assistant_reply = response['choices'][0]['message']['content']
    print("Assistant's Reply:")
    print(assistant_reply)

except Exception as e:
    print(f"An error occurred: {e}")
