# Google and Ollama Chat Integration

This repository provides a Python script that integrates Google Custom Search and Ollama's chat functionality. The script allows users to type messages, perform Google searches, and interact with the Ollama chat model to process search results or answer queries.

## Features

- **Google Custom Search:** Perform searches using Google's Custom Search API.
- **Ollama Chat:** Chat with the Ollama model to process and respond to user queries.
- **Interactive Command-Line Interface:** Continuously interact with the script via the command line.

## Requirements

- Python 3.6 or later
- `requests` library
- `ollama` library

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/username/repository.git
    cd repository
    ```

2. **Install the required libraries:**
    ```sh
    pip install requests ollama
    ```

3. **Obtain Google Custom Search API key and Search Engine ID:**
    - Sign up for Google Custom Search API and generate an API key.
    - Create a custom search engine and obtain the Search Engine ID.

4. **Update the script with your API credentials:**
    ```python
    # Google API account
    api_key = "YOUR_API_KEY"
    search_engine_id = "YOUR_SEARCH_ENGINE_ID"
    ```

## Usage

1. **Run the script:**
    ```sh
    python script_name.py
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
