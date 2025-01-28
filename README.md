# Context-Aware Research Assistant with RAG

This Python script implements a **Context-Aware Research Assistant** that leverages **Retrieval-Augmented Generation (RAG)** to answer your questions using up-to-date information from the web. It combines the power of the **SERP API** for web searching and the **Gemini API** for generating insightful and contextually relevant answers.

## Description

This tool is designed to provide answers to your questions by searching the web for relevant information and then using a large language model (Gemini API) to synthesize a response.  It goes beyond simple keyword search by:

* **Context-Aware Search Query Generation:**  It can refine your initial question into a more effective search query by considering the ongoing conversation history.
* **Web Content Retrieval & Processing:** It fetches content from search results, extracts relevant text, and cleans it for better processing.
* **RAG with Gemini API:**  It feeds the retrieved web content as context to the Gemini API, enabling it to generate answers grounded in current web information.
* **Conversation History:** It maintains a short conversation history to provide more contextually relevant answers in subsequent turns.
* **Source Citation:**  The generated answers can cite the sources of information used from the web results, enhancing transparency and credibility.

**In essence, ask a question, and this assistant will:**

1. **Formulate a smart search query** based on your question and conversation history.
2. **Search the web** using the SERP API to find relevant web pages.
3. **Extract and process content** from the top search results.
4. **Generate a comprehensive and contextually aware answer** using the Gemini API, citing sources from the web content.

## Features

* **Real-time Web Information:** Answers are based on the latest information available on the web.
* **Contextual Understanding:** Leverages conversation history to provide more relevant responses.
* **Enhanced Search Queries:** Generates refined search queries for better results.
* **Source Citation:**  Cites sources to back up the generated answers.
* **Cleaned Web Content:** Processes and cleans web page content for better input to the language model.
* **Simple Chat Interface:**  Easy-to-use command-line interface for asking questions.
* **Conversation History Management:** Clears conversation history when needed.

## Getting Started

### Prerequisites

Before running this script, ensure you have the following:

* **Python 3.6 or higher:**  Make sure you have Python installed on your system.
* **Required Python Libraries:** Install the necessary libraries using pip:
   ```bash
   pip install requests google-generativeai beautifulsoup4
   ```
* **API Keys:**
    * **Gemini API Key:** You need a Google Cloud API key to access the Gemini API. You can obtain one by setting up a Google Cloud project and enabling the Gemini API.  Visit [Google AI Studio](https://makersuite.google.com/) to get started and obtain your API Key.
    * **SERP API Key:** You need a SERP API key to access web search results programmatically. Sign up for a free or paid plan at [SerpApi](https://serpapi.com/) and obtain your API Key.

### Installation

1. **Clone the repository (or download the script):**
   ```bash
   git clone https://github.com/NamanSingh69/WebSearchChatBot
   cd WebSearchChatBot
   ```
   If you downloaded the script directly, place it in a directory of your choice and navigate to it in your terminal.

2. **Install Python Libraries (if you haven't already):**
   ```bash
   pip install requests google-generativeai beautifulsoup4
   ```

### Configuration

1. **Open the Python script (`your_script_name.py`, likely the name of your script file).**
2. **Locate the API Key placeholders:**
   ```python
   genai.configure(api_key="Enter your Gemini API key here")
   SERPAPI_KEY = "Enter your SERP API key here"
   ```
3. **Replace `"Enter your Gemini API key here"` with your actual Gemini API key.**
4. **Replace `"Enter your SERP API key here"` with your actual SERP API key.**
5. **Save the script.**

### Running the Script

1. **Open your terminal or command prompt.**
2. **Navigate to the directory where you saved the Python script.**
3. **Run the script using Python:**
   ```bash
   python WebSearchChatBot.py
   ```

4. **Follow the on-screen instructions in the chat interface.** You can now start asking questions to the Context-Aware Research Assistant!

   * Type your question and press Enter.
   * Type `clear` to reset the conversation history.
   * Type `exit` or `quit` to end the chat session.

## Usage Examples

After running the script, you will see the chat interface. Here are some example interactions:

```
=== Context-Aware Research Assistant ===
Type your questions (type 'exit', 'quit', or 'clear' to reset)

Enter your question: What is the current weather in London?

Researching current information...
Assistant: The current weather in London is ... [[1]]

─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
Enter your question: What about Paris? (referring to weather)

Researching current information...
Assistant: The current weather in Paris is ... [[2]]

─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
Enter your question: clear

Assistant: Conversation history cleared.

Enter your question: Who won the last world cup?

Researching current information...
Assistant: Argentina won the last World Cup in 2022. [[3]]

─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
Enter your question: exit

Assistant: Goodbye! Feel free to return with more questions.
```

**Note:**  Source citations like `[[1]]`, `[[2]]`, `[[3]]` will be included in the actual output and ideally, the source URLs or names would be listed at the end of the response (this feature may need to be implemented explicitly in the code if not already present based on the prompt instructions).

## Limitations and Future Work

* **Error Handling:**  More robust error handling can be implemented for network issues, API errors, and web scraping failures.
* **Source Citation Improvement:**  Currently, source citation is basic.  Enhancements could include listing the actual URLs or source names at the end of the answer and making the citations more contextually linked to the specific information they support.
* **Content Filtering & Relevance:** Improve the filtering and ranking of web content to ensure only the most relevant and reliable information is used.
* **Handling Paywalls and Complex Websites:**  The web scraping might struggle with websites behind paywalls or those with very complex structures. Improvements could be made to handle these scenarios more gracefully.
* **Customization:** Allow users to customize search parameters (e.g., location, number of results), model parameters, and prompt templates.
* **More Advanced Conversation History:**  Potentially use a more sophisticated method to manage and utilize conversation history for deeper contextual understanding.
* **Output Formatting:** Improve the formatting of the generated answers for better readability.

## License

Feel free to use and modify this code for your own purposes.  
---

**Disclaimer:** This script uses third-party APIs (SERP API and Gemini API) and is subject to their terms of service and usage limits. Please ensure you are aware of and comply with their respective terms.
```
