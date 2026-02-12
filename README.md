# Blog to Podcast Generator

Convert any blog article into an AI-generated podcast with just one click! This Streamlit app uses Google Gemini AI to summarize blog content and Google TTS to convert it into natural-sounding speech.

## ✨ Features

- 🌐 **Scrape any blog URL** - Automatically extracts content using Firecrawl
- 🤖 **AI-powered summarization** - Google Gemini creates engaging podcast scripts
- 🎙️ **Text-to-Speech** - Google TTS converts summaries to high-quality audio
- 📥 **Download MP3** - Save podcasts for offline listening
- 🆓 **100% FREE APIs** - All services have generous free tiers

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone or download this repository**

```bash
git clone https://github.com/suhas-sk08/blog_to_Voice
cd blog_to_Voice
```

2. **Install required packages**

```bash
pip install streamlit google-genai gTTS firecrawl-py
```

### Running the App

```bash
streamlit run main.py
```

The app will open in your default browser at `http://localhost:8501`

## 🔑 Getting Free API Keys

### 1. Google Gemini API Key (FREE)

- Visit: https://makersuite.google.com/app/apikey
- Click "Create API Key"
- Copy the key (starts with `AIza...`)
- **Free Tier:** 60 requests/minute, 1,500 requests/day


### 2. Firecrawl API Key (FREE)

- Visit: https://firecrawl.dev/
- Sign up for a free account
- Get your API key from the dashboard
- **Free Tier:** 500 pages/month

## 📖 How to Use

1. **Enter API Keys** in the sidebar
2. **Paste a blog URL** into the input field
3. **Click "🎙️ Generate Podcast"**
4. **Listen** to the generated podcast
5. **Download** the MP3 file (optional)

## 📦 Dependencies

```
streamlit>=1.30.0
google-genai>=0.3.0
gTTS>=2.5.0
firecrawl-py>=0.0.5
```

## 🛠️ Technical Details

### Architecture

```
Blog URL → Firecrawl (Scraping) → Gemini AI (Summarization) → Google TTS (TTS) → Audio Output
```

### Models Used

- **Gemini**: `models/gemini-flash-latest` (Fast & Free)
- **Google TTS Voice**: `Free Voice` 
- **TTS Model**: `eleven_multilingual_v2`

### Processing Pipeline

1. **Scraping**: Firecrawl extracts blog content as markdown
2. **Summarization**: Gemini AI creates a 2000-character podcast script
3. **Audio Generation**: Google TTS converts text to speech
4. **Output**: Streamlit serves audio player and download button

## ⚙️ Configuration

### Adjust Summary Length

Edit line 45 to change maximum summary length:

```python
(max 2000 characters).  # Change to your preferred length
```

### Use Different Gemini Model

Edit line 55 to use a different model:

```python
model="models/gemini-flash-latest",  # Options below
```

**Available FREE Gemini Models:**
- `models/gemini-flash-latest` - Latest Flash (Recommended)
- `models/gemini-1.5-flash` - Stable Flash
- `models/gemini-1.5-flash-8b` - Faster, smaller model
- `models/gemini-1.0-pro` - Legacy model

## 🔒 Security & Privacy

- ✅ **API keys stored locally** - Never sent to any server except official APIs
- ✅ **No data collection** - Your blog URLs and content are private
- ✅ **Secure connections** - All API calls use HTTPS
- ⚠️ **Never commit API keys** - Add `.streamlit/secrets.toml` to `.gitignore`

### Using Secrets (Production)

Create `.streamlit/secrets.toml`:

```toml
GEMINI_API_KEY = "your-key-here"
FIRECRAWL_API_KEY = "your-key-here"
```

Then update code to use:

```python
gemini_key = st.secrets.get("GEMINI_API_KEY", "")
```

## 📝 Code Structure

```
blog-to-podcast/
├── main.py                 # Main Streamlit app
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── .gitignore             # Git ignore file
```

## 🚀 Deployment

### Deploy to Streamlit Cloud (FREE)

1. Push code to GitHub
2. Go to https://share.streamlit.io/
3. Connect your GitHub repository
4. Add API keys in "Secrets" section
5. Deploy!

## 🤝 Contributing

Contributions welcome! Feel free to:

- 🐛 Report bugs
- 💡 Suggest features
- 🔧 Submit pull requests
- 📖 Improve documentation

## 🙏 Acknowledgments

- **Google Gemini** - For free AI summarization
- **ElevenLabs** - For high-quality text-to-speech
- **Firecrawl** - For easy web scraping
- **Streamlit** - For the awesome web framework

## 🎓 Learn More

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Gemini API Docs](https://ai.google.dev/docs)
- [ElevenLabs API Docs](https://elevenlabs.io/docs)
- [Firecrawl Documentation](https://docs.firecrawl.dev/)

## ⭐ Star This Project

If you found this helpful, please star the repository!

---

**Made with ❤️ using AI and Python**

🎙️ **Happy Podcasting!** 🎧
