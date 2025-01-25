import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import re
import requests

def extract_video_id(url):
    # Extract video ID from different YouTube URL formats
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(regex, url)
    return match.group(1) if match else None

def get_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([t['text'] for t in transcript_list])
        return transcript
    except Exception as e:
        return None

def generate_summary(prompt, text):
    ollama_url = "http://localhost:11434/api/generate"
    
    full_prompt = f"{prompt}\n\nText: {text}"
    
    payload = {
        "model": "llama3.1",
        "prompt": full_prompt,
        "stream": False
    }
    
    try:
        response = requests.post(ollama_url, json=payload)
        response.raise_for_status()
        return response.json()["response"]
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Streamlit UI
st.title("YouTube Video Summarizer 🎥📝")

# Custom CSS for styling
st.markdown("""
    <style>
    .reportview-container {
        background: #f0f2f6;
    }
    .sidebar .sidebar-content {
        background: #ffffff;
    }
    h1 {
        color: #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

url = st.text_input("Enter YouTube Video URL:", placeholder="https://www.youtube.com/watch?v=...")

if st.button("Generate Summary"):
    if url:
        video_id = extract_video_id(url)
        if video_id:
            with st.spinner("Fetching transcript..."):
                transcript = get_transcript(video_id)
            
            if transcript:
                with st.expander("View Transcript"):
                    st.text_area("Transcript", transcript, height=200)
                
                with st.spinner("Generating summary..."):
                    summary_prompt = """Please analyze the following video transcript and generate comprehensive notes. Organize the content into clear sections with the following structure:
                        1. **Key Topics Covered**: List the main topics discussed in the video.
                        2. **Detailed Explanations**: For each topic, provide an in-depth explanation of the underlying concepts. Use simple language and include examples where applicable.
                        3. **Key Takeaways**: Summarize the most important points in bullet form.
                        4. **Additional Insights**: Include any relevant background information, real-world applications, or connections to related concepts.

                        Ensure the notes are:
                        - Well-structured and easy to follow
                        - Free of promotional content or brand mentions
                        - Focused on explaining concepts thoroughly
                        - Include examples or analogies to clarify complex ideas
                    """
                    
                    summary = generate_summary(summary_prompt, transcript)  # Limiting to 3000 chars for demo
                
                st.subheader("Detailed Notes")
                st.write(summary)
            else:
                st.error("Could not retrieve transcript. The video might not have captions.")
        else:
            st.error("Invalid YouTube URL")
    else:
        st.warning("Please enter a YouTube URL")

st.markdown("---")
st.caption("Note: Make sure Ollama is running locally with the Llama3 model installed.")