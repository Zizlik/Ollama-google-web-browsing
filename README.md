# Ollama-Google-Web-Browsing

This repository provides a Python script that integrates Google Custom Search and Ollama's chat functionality. The script allows users to type messages, perform Google searches, and interact with the Ollama chat model to process search results or answer queries. Additionally, the repository contains two extra Python scripts: one for testing the Ollama model and another for verifying CUDA setup.

## Features

- **Google Custom Search:** Perform searches using Google's Custom Search API.
- **Ollama Chat:** Chat with the Ollama model to process and respond to user queries.
- **Interactive Command-Line Interface:** Continuously interact with the script via the command line.
- **Ollama Model Testing: Test the Ollama model's capabilities with a dedicated script.

## Prerequisites

To use this project, you'll need to set up the following:

- **Google API Key:** For accessing the Google Custom Search API.
- **Ollama API:** For processing and generating conversational responses.

### How to Obtain Google API Key
1. Visit the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Enable the "Custom Search API" under the "APIs & Services" section.
4. Go to "Credentials" and create an API key.
5. Copy the API key and paste it into the `api_key` variable in the code.

### How to Obtain Ollama API Access
1. Visit the [Ollama API Documentation](https://ollama.com/docs/).
2. Sign up or log in to your Ollama account.
3. Create an API client and obtain the necessary credentials.
4. Use the provided credentials to set up the `ollama.Client()` in the code.

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Zizlik/Ollama-google-web-browsing.git
    cd Ollama-google-web-browsing
    ```

2. **Install the required libraries:**
    ```sh
    pip install requests ollama
    ```

3. **Update the script with your API credentials:**
    ```python
    # Google API account
    api_key = "YOUR_API_KEY"
    search_engine_id = "YOUR_SEARCH_ENGINE_ID"
    ```

## Usage

1. **Run the script:**
    ```sh
    python Ollama_Google.py
    ```

2. **Interact with the script:**
    - Type a message and press Enter to chat with the Ollama model.
    - Type a message containing the word "google" followed by your search query to perform a Google search.
    - Type 'exit' to terminate the script.

## Example

```sh
> Enter a message (or 'exit' to exit): google Python tutorials
> Ollama: Here are the top Google search results:
> Result 1: Python Official Documentation - (Link: https://www.python.org/doc/)
> Result 2: W3 Schools Python Tutorial - (Link: https://www.w3schools.com/python/)
> Result 3: Real Python - (Link: https://realpython.com/)
>
> Ollama can help with further processing or answering questions about these results.
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.

---

Feel free to modify the description, examples, or any sections to better fit your repository or use case.
