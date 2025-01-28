import requests
import google.generativeai as genai
from bs4 import BeautifulSoup

# API Configuration (Replace with your keys)
genai.configure(api_key="Enter your Gemini API Key here")
model = genai.GenerativeModel('gemini-pro')
SERPAPI_KEY = "Enter your SERP API Key here"

class SerpApiRAG:
    def __init__(self):
        self.search_endpoint = "https://serpapi.com/search"
        self.conversation_history = []
    
    def search_web(self, query, num_results=5):
        params = {
            "api_key": SERPAPI_KEY,
            "engine": "google",
            "q": query,
            "num": num_results,
            "location": "United States",
            "google_domain": "google.com"
        }

        try:
            response = requests.get(self.search_endpoint, params=params)
            results = response.json()
            return [r.get("link") for r in results.get("organic_results", [])][:num_results]
        except Exception as e:
            print(f"Search error: {str(e)}")
            return []

    def fetch_page_content(self, url):
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            response = requests.get(url, headers=headers, timeout=15)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Clean unnecessary elements
            for element in soup(['script', 'style', 'nav', 'footer', 'header', 'form']):
                element.decompose()

            # Extract main content
            main_content = soup.find('article') or soup.find('main') or soup.body
            paragraphs = main_content.find_all(['p', 'h1', 'h2', 'h3', 'ul']) if main_content else []
            text = '\n'.join([p.get_text().strip() for p in paragraphs if p.get_text().strip()])
            return text[:10000]  # Limit to 10k characters
        except Exception as e:
            print(f"Error fetching {url}: {str(e)}")
            return ""

    def generate_answer(self, query, context_chunks):
        # Build conversation context
        history_context = "\n".join(
            [f"User: {entry['user']}\nAssistant: {entry['assistant']}" 
             for entry in self.conversation_history[-2:]]  # Keep last 2 exchanges
        ) if self.conversation_history else "No previous conversation"

        # Build web context
        web_context = "\n\n".join(
            [f"[[Source {i+1}]]\n{text}" for i, text in enumerate(context_chunks)]
        )

        prompt = f"""**Conversation Context**
{history_context}

**New Research Context**
{web_context}

**Instructions**
1. Answer the new question considering both contexts
2. Resolve pronouns (e.g., 'there' -> Paris)
3. Cite sources like [[1]] when using specific info
4. If conflicting info, state clearly
5. Be concise but thorough

**New Question**: {query}

**Formatted Answer**:"""

        response = model.generate_content(prompt)
        return response.text

    def rag_query(self, query, num_sources=3):
        # Enhance query with conversation context
        enhanced_query = query
        if self.conversation_history:
            last_exchange = self.conversation_history[-1]
            if 'paris' in last_exchange['assistant'].lower():
                enhanced_query += " in Paris, France"
            elif 'france' in last_exchange['assistant'].lower():
                enhanced_query += " in France"

        # Get fresh web results
        urls = self.search_web(enhanced_query, num_results=num_sources)
        context_chunks = []
        
        # Fetch and process content
        for url in urls:
            content = self.fetch_page_content(url)
            if content:
                context_chunks.append(f"URL: {url}\n{content}")

        # Generate answer
        answer = self.generate_answer(query, context_chunks)
        
        # Update history (keep last 5 exchanges)
        self.conversation_history.append({"user": query, "assistant": answer})
        if len(self.conversation_history) > 5:
            self.conversation_history.pop(0)
            
        return answer
    
    def clear_history(self):
        self.conversation_history = []

def chat_interface():
    rag = SerpApiRAG()
    print("\033[1;36m\n=== Context-Aware Research Assistant ===\033[0m")
    print("\033[90mType your questions (type 'exit', 'quit', or 'clear' to reset)\033[0m\n")
    
    while True:
        try:
            # Get user input
            user_input = input("\033[90mEnter your question:\033[0m ").strip()
            
            if user_input.lower() in ('exit', 'quit'):
                print("\033[1;35m\nAssistant: Goodbye! Feel free to return with more questions.\033[0m")
                break
                
            if user_input.lower() == 'clear':
                rag.clear_history()
                print("\033[1;35m\nAssistant: Conversation history cleared.\033[0m\n")
                continue
                
            if not user_input:
                continue
                
            # Process query
            print(f"\n\033[1;34mUser: {user_input}\033[0m")
            print("\033[90mResearching current information...\033[0m")
            answer = rag.rag_query(user_input)
            
            # Print formatted response
            print(f"\033[1;32mAssistant:\033[0m {answer}")
            print("\033[90m" + "─" * 80 + "\033[0m\n")
            
        except KeyboardInterrupt:
            print("\033[1;35m\n\nAssistant: Session ended. Thank you!\033[0m")
            break
        except Exception as e:
            print(f"\033[91m\nError: {str(e)}\033[0m")

if __name__ == "__main__":
    chat_interface()
