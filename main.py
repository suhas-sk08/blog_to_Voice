import os
import streamlit as st

st.set_page_config(page_title="Blog to Podcast", page_icon="🎙️")
st.title("Blog to Podcast Agent (Gemini)")

st.sidebar.header("API Keys")

gemini_key = st.sidebar.text_input("Google Gemini API Key", type="password")
elevenlabs_key = st.sidebar.text_input("ElevenLabs API Key", type="password")
firecrawl_key = st.sidebar.text_input("Firecrawl API Key", type="password")

url = st.text_input("Enter Blog URL:")

if st.button(
    "🎙️Generate Podcast",
    disabled=not all([gemini_key, elevenlabs_key, firecrawl_key])
):
    if not url.strip():
        st.warning("Please enter a blog URL")
    else:
        with st.spinner("Scraping blog and generating podcast..."):
            try:
                from google import genai
                from elevenlabs import ElevenLabs
                from firecrawl import FirecrawlApp
                os.environ["FIRECRAWL_API_KEY"] = firecrawl_key

                client_gemini = genai.Client(api_key=gemini_key)

                firecrawl = FirecrawlApp(api_key=firecrawl_key)

                scrape_result = firecrawl.scrape(
                    url,
                    formats=["markdown"]
                )

                blog_content = scrape_result.markdown or scrape_result.content

                if not blog_content:
                    st.error("Failed to scrape blog content")
                    st.stop()

                prompt = f"""
You are a podcast script writer.

Based on the following blog content, create a concise and engaging podcast summary
(max 2000 characters).

Rules:
- Conversational tone
- No markdown symbols
- Easy to listen to

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

                client_audio = ElevenLabs(api_key=elevenlabs_key)

                audio_generator = client_audio.text_to_speech.convert(
                    text=summary,
                    voice_id="JBFqnCBsd6RMkjVDRZzb",
                    model_id="eleven_multilingual_v2",
                )

                audio_bytes = b"".join(audio_generator)

                st.success("Podcast generated successfully!")

                st.audio(audio_bytes, format="audio/mp3")

                st.download_button(
                    label="Download Podcast",
                    data=audio_bytes,
                    file_name="podcast.mp3",
                    mime="audio/mp3",
                )

                with st.expander("Podcast Summary"):
                    st.write(summary)

            except Exception as e:
                st.error("Something went wrong")
                st.exception(e)

with st.sidebar:
    st.markdown("---")
    st.markdown("### Get Your Free API Keys")
    st.markdown("""
    - **Gemini**: https://makersuite.google.com/app/apikey  
    - **ElevenLabs**: https://elevenlabs.io/  
    - **Firecrawl**: https://firecrawl.dev/  
    """)

    st.markdown("---")
    st.markdown("### How It Works")
    st.markdown("""
    1. Enter API keys  
    2. Paste blog URL  
    3. Click Generate Podcast  
    4. Listen + Download MP3  
    """)

   