import time
import torch
import ollama
from ollama import Client

# Initializing Ollama client
client = Client()

# Initialize models using CUDA if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")
for i in range(torch.cuda.device_count()):
    print(f"GPU {i+1}: ", torch.cuda.get_device_name(i))
    print("        Total memory:", torch.cuda.get_device_properties(i).total_memory / 1e9, "GB")
    print("        MultiProcessor Count:", torch.cuda.get_device_properties(i).multi_processor_count)
    print("        Is available:", torch.cuda.is_available())
    print("___________________________________________________\n")

# Test data
test_data = [
    "Count number of 'r' in strawberry",
    "Why is the sky blue?"
]

# Power measurement function
def measure_performance(model_name, test_data):
    results = {
        "model": model_name,
        "response_times": [],
        "accuracies": [],
        "tokens_per_second": [],
        "responses": [] # Added to store individual responses
    }
    
    for data in test_data:
        start_time = time.time()
        
        # Using the stream to get the answer
        stream = client.chat(
            model=model_name,
            messages=[{'role': 'user', 'content': data}],
            stream=True,
        )

        response_text = ''
        token_count = 0
        for chunk in stream:
            words = chunk['message']['content'].split()
            token_count += len(words)
            response_text += ' '.join(words) + ' '

        end_time = time.time()

        response_time = end_time - start_time
        tokens_per_second = token_count / response_time
        
         # We assume that the precision is measured by some function `calculate_accuracy`
        accuracy = calculate_accuracy(response_text.strip(), data)
        
        results["response_times"].append(response_time)
        results["accuracies"].append(accuracy)
        results["tokens_per_second"].append(tokens_per_second)
        results["responses"].append(response_text.strip())  # Saving the answer

    
    return results

# Main features for model comparison
def compare_models(model_names, test_data):
    performances = []
    
    for model_name in model_names:
        performance = measure_performance(model_name, test_data)
        performances.append(performance)
    
    return performances

# Accuracy calculation function (must be replaced by a real implementation)
def calculate_accuracy(output, input_query):
    if input_query == "Count number of 'r' in strawberry":
        expected_output = "3"  # correct answer is 3
    elif input_query == "Why is the sky blue?":
        expected_output = "Rayleigh scattering"  # brief explanation
    
    # Comparison of output with expected output (to be fine-tuned as needed)
    return expected_output.lower() in output.lower()

# Start comparison
model_names = ["llama3", "gemma2", "llama3.1"]
performances = compare_models(model_names, test_data)

# Listing of results
for performance in performances:
    print(f"Model: {performance['model']}")
    print(f"Average response time: {sum(performance['response_times']) / len(performance['response_times'])} s")
    print(f"Average accuracy: {sum(performance['accuracies']) / len(performance['accuracies'])}")
    print(f"Average number of tokens per second: {sum(performance['tokens_per_second']) / len(performance['tokens_per_second'])}")
    print("The answers:")
    for i, response in enumerate(performance["responses"]):
        print(f"  Promt: {test_data[i]}")
        print(f"  Completion: {response}")
    print("___________________________________________________\n")