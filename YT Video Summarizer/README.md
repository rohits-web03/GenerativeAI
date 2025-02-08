# YouTube Video Summarizer 🎥📝

A simple Python app to summarize YouTube videos to simplify making notes for educational purposes. It uses **Streamlit** for the frontend and **Ollama** (with Llama 3.1) for generating summaries. The app extracts video transcripts and provides concise summaries with key points.

## Features ✨
- Enter a YouTube URL to get a summary.
- Fetches video transcripts automatically.
- Generates summaries using Ollama's Llama 3.1 model.
- Clean and easy-to-use interface.

## Requirements 📋
- Python 3.8+
- Ollama (with Llama 3.1 model installed)
- Libraries: `streamlit`, `youtube-transcript-api`, `requests`

## Local Setup 🛠️

Follow these steps to set up the project locally:

### 1. Clone the Repository  
```sh
git clone https://github.com/rohits-web03/GenerativeAI.git
cd "YT Video Summarize"
```

### 2. Create a Virtual Environment (Optional but Recommended)  
```sh
python -m venv ytsummarizer
source ytsummarizer/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install Dependencies  
```sh
pip install -r requirements.txt
```

### 4. Install & Start Ollama  
- **Download & Install Ollama:** Follow the instructions at [Ollama's website](https://ollama.com)  
- **Start the Ollama Server:**  
  ```sh
  ollama serve
  ```
- **Ensure Llama 3.1 is installed:**  
  ```sh
  ollama pull llama3.1
  ```

### 5. Run the Streamlit App  
```sh
streamlit run app.py
```

Now, open your browser at **http://localhost:8501** and start summarizing YouTube videos! 🚀

## Future Improvements 🚧
This is a **basic prototype**. More features might be added later.