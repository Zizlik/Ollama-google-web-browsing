import requests
import ollama

def google_search(query, api_key, search_engine_id, num_results=3):
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={search_engine_id}&num={num_results}"
    response = requests.get(url)
    return response.json()

# Google API account
api_key = ""
search_engine_id = ""

def chat_with_ollama(prompt):
    client = ollama.Client()
    response = client.chat(model='llama3.1', messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']

if __name__ == "__main__":
    while True:
        user_input = input("Enter a message (or 'exit' to exit): ")
        if user_input.lower() == 'exit':
            break
        if 'google' in user_input.lower():
            query = user_input.replace("google", "").strip()
            google_results = google_search(query, api_key, search_engine_id)
            if 'items' in google_results:
                google_summary = "Here are the top Google search results:\n"
                for i, item in enumerate(google_results['items']):
                    google_summary += f"Result {i+1}: {item['title']} - {item['snippet']} (Link: {item['link']})\n"
                # Use Ollama to process the Google summary
                ollama_response = chat_with_ollama(google_summary)
                print(f"Ollama: {ollama_response}")
            else:
                print("No results found or error occurred.")
        else:
            response = chat_with_ollama(user_input)
            print(f"Ollama: {response}")
