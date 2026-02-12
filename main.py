import os
import streamlit as st
from gtts import gTTS  
import io

st.set_page_config(page_title="Blog to Podcast", page_icon="🎙️")
st.title("🎙️ Blog to Podcast (Gemini)")

st.sidebar.header("API Keys")

gemini_key = st.sidebar.text_input("Google Gemini API Key", type="password")
firecrawl_key = st.sidebar.text_input("Firecrawl API Key", type="password")

url = st.text_input("Enter Blog URL:")

if st.button(
    "🎙️ Generate Podcast",
    disabled=not all([gemini_key, firecrawl_key])
):
    if not url.strip():
        st.warning("Please enter a blog URL")
    else:
        with st.spinner("Scraping blog and generating podcast..."):
            try:
                from google import genai
                from firecrawl import FirecrawlApp
                
                os.environ["FIRECRAWL_API_KEY"] = firecrawl_key

                # Initialize Gemini
                client_gemini = genai.Client(api_key=gemini_key)

                firecrawl = FirecrawlApp(api_key=firecrawl_key)
                scrape_result = firecrawl.scrape(url, formats=["markdown"])
                blog_content = scrape_result.markdown or scrape_result.content

                if not blog_content:
                    st.error("Failed to scrape blog content")
                    st.stop()

                st.info("Generating podcast script with AI...")
                prompt = f"""
You are a podcast script writer.

Based on the following blog content, create a concise and engaging podcast summary
(max 2000 characters).

Rules:
- Conversational tone
- No markdown symbols or special characters
- Easy to listen to
- Natural speaking style
- Engaging and friendly

Blog content:
{blog_content[:8000]}

Now generate the podcast summary:
"""

                response = client_gemini.models.generate_content(
                    model="models/gemini-flash-latest",
                    contents=prompt
                )

                summary = response.text.strip()

                if not summary:
                    st.error("Failed to generate summary")
                    st.stop()

                st.success(f"Generated {len(summary)} characters")

                st.info("🎙️ Converting to speech with Google TTS...")
                
                tts = gTTS(text=summary, lang='en', slow=False)
                audio_buffer = io.BytesIO()
                tts.write_to_fp(audio_buffer)
                audio_bytes = audio_buffer.getvalue()

                st.success("Podcast generated successfully!")

                st.audio(audio_bytes, format="audio/mp3")

                st.download_button(
                    label="Download Podcast MP3",
                    data=audio_bytes,
                    file_name="podcast.mp3",
                    mime="audio/mp3",
                )

                with st.expander("View Podcast Script"):
                    st.write(summary)

            except Exception as e:
                st.error("Something went wrong")
                st.exception(e)

with st.sidebar:
    st.markdown("---")
    st.markdown("### Get Your FREE API Keys")
    st.markdown("""
    - **Gemini**: https://makersuite.google.com/app/apikey  
    - **Firecrawl**: https://firecrawl.dev/  
    """)

    st.markdown("---")
    st.markdown("### Features")
    st.markdown("""
    **100% FREE** - No paid APIs needed!
    **Google TTS** - Natural voice synthesis
    **AI Summarization** - Gemini creates scripts
    **Auto Scraping** - Firecrawl extracts content
    **MP3 Download** - Save for offline listening
    """)

    st.markdown("---")
    st.markdown("### How It Works")
    st.markdown("""
    1. Enter your FREE API keys
    2. Paste any blog URL  
    3. Click Generate Podcast  
    4. Listen to AI-generated podcast
    5. Download MP3 file  
    """)
    