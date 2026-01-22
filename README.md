Local AI Chatbot with GPT4All
A lightweight, privacy-focused terminal chatbot powered by the Llama-3.2-1B model. This script uses the GPT4All Python library to run Large Language Models (LLMs) locally on your CPU or GPU.

🚀 Features
100% Local: No data leaves your machine. No API keys or internet connection required after the initial model download.

Persistent Memory: Uses model.chat_session() to maintain context throughout the conversation.

Lightweight: Optimized for performance using the 4-bit quantized Llama-3.2-1B model.

📋 Prerequisites
Before running the script, ensure you have Python 3.8+ installed. You will also need to install the GPT4All Python bindings:

Bash
pip install gpt4all
🛠️ Installation & Setup
Clone the repository:


Download the Model: The script is configured to use Llama-3.2-1B-Instruct-Q4_0.gguf.

On the first run, the script will automatically attempt to download the model to your local ~/.cache/gpt4all/ directory.

Alternatively, you can download it manually from the GPT4All website.

🖥️ Usage
Run the chatbot by executing the Python script:

Bash
python chatbot.py
Commands:

Type your message and press Enter to chat.

Type exit, quit, or bye to end the session.

⚙️ Configuration
You can customize the AI's behavior by modifying the parameters in the model.generate() function:

Parameter	Description	Recommended
max_tokens	Limits the length of the AI response.	200 - 500
temp	Controls randomness. Higher is more creative.	0.7
top_k	Limits the AI to picking from the top K most likely words.	40
📝 License
This project is open-source and available under the MIT License.
