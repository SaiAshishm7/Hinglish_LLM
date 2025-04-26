import openai

# Set your OpenAI API key
openai.api_key = "YOUR-API-KEY-HERE"

# Path to your .jsonl file
dataset_path = "dataset.jsonl"

# Upload the dataset
print("Uploading dataset...")
upload_response = openai.File.create(
    file=open(dataset_path, "rb"),
    purpose='fine-tune'
)
file_id = upload_response["id"]
print(f"Dataset uploaded successfully. File ID: {file_id}")

# Start fine-tuning
print("Starting fine-tuning job...")
fine_tune_response = openai.FineTuningJob.create(
    training_file=file_id,
    model="gpt-3.5-turbo-1106"
)
fine_tune_id = fine_tune_response["id"]
print(f"Fine-tuning job started. Fine-tune Job ID: {fine_tune_id}")


