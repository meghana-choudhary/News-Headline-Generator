# News Headline Generator

An AI-powered News Headline Generator that crafts compelling, concise, and relevant headlines based on user-provided articles. It allows customization through tone, platform, headline style, audience, keywords, and additional specific requirements.

---

## Features

- **Customizable Tone:** Generate headlines in various tones such as neutral, witty, professional, dramatic, or inspirational.
- **Platform-specific Headlines:** Tailor headlines for platforms like LinkedIn, Twitter, News Websites, or Blogs.
- **Length Control:** Limit headlines to a maximum number of words.
- **Keyword Inclusion:** Emphasize specified keywords within the headlines.
- **Headline Styles:** Choose from styles like Listicle, How-to, Question, or Statement.
- **Audience Targeting:** Adapt headlines for different audiences such as general public, professionals, students, or executives.
- **Additional Requirements:** Include any extra instructions to further refine headline generation.

---

## Technologies Used

- **Python** — Backend logic and integration.
- **Streamlit** — User-friendly UI for interaction.
- **Gemini 2.5 Flash Preview** — Language model powering headline generation.

---

## Installation & Setup

1. **Clone the repository:**

```bash
git clone https://github.com/meghana-choudhary/News-Headline-Generator.git
cd News-Headline-Generator
```
2. **Install Dependencies:**

```bash
pip install -r requirements.txt
```
3. **Create Environment File:** Create a file named .env in the root directory of the project.

4. **Add API Keys:** Open the .env file and add your API keys like this:

```bash
GOOGLE_API_KEY=YOUR_GOOGLE_API_KEY
```

5. **Run the Backend:**

```bash
streamlit run app.py
```

## Usage
- Paste your article content.

- Customize options including tone, platform, headline style, audience, keywords, and extra requirements.

- Click Generate Headlines to receive AI-generated headline suggestions.

- Use Clear to reset the form.

