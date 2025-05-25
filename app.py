import streamlit as st
from headline_generator import generate_headlines

st.set_page_config(page_title="News Headline Generator", page_icon="📰", layout="wide")
st.title("🤖 AI-powered News Headline Generator")


if "reset" not in st.session_state:
    st.session_state.reset = False

if st.session_state.reset:

    st.session_state.article = ""
    st.session_state.tone = ""
    st.session_state.platform = ""
    st.session_state.max_words = 12
    st.session_state.headline_type = ""
    st.session_state.audience_type = ""
    st.session_state.num_variants = 3
    st.session_state.keywords = ""
    st.session_state.extra_reqd = ""
    st.session_state.reset = False
    st.rerun()



left_col, right_col = st.columns([1.5, 1])

with left_col:
    st.markdown("### ✍️ Paste Your Article")
    article = st.text_area("Article Content", height=350, label_visibility="collapsed", key="article")

with right_col:
    st.markdown("### 🎨 Customization Options")

 
    col1, col2, col3 = st.columns(3)
    with col1:
        tone = st.selectbox("Tone", ["", "Neutral", "Witty", "Professional", "Dramatic", "Inspirational"], key="tone")
    with col2:
        platform = st.selectbox("Platform", ["", "LinkedIn", "Twitter", "News Website", "Blog"], key="platform")
    with col3:
        max_words = st.slider("Max Words", 5, 20, 12, key="max_words")


    col4, col5, col6 = st.columns(3)
    with col4:
        headline_type = st.selectbox("Headline Style", ["", "Listicle", "How-to", "Question", "Statement"], key="headline_type")
    with col5:
        audience_type = st.selectbox("Audience", ["", "General Public", "Professionals", "Students", "Executives"], key= "audience_type")
    with col6:
        num_variants = st.slider("Variants", 1, 5, 3, key="num_variants")


    keywords_input = st.text_input("Keywords (comma-separated):", key="keywords")
    extra_reqd= st.text_input("Enter additional requirements (if any):", key="extra_reqd")

button_col1, button_col2, button_col3, button_col4, button_col5 = st.columns([1, 1, 1, 1, 1])
with button_col2:
    generate = st.button("🚀 Generate Headlines", use_container_width=True)
with button_col4:
    clear = st.button("🧹 Clear", use_container_width=True, type="secondary")


if clear:
    st.session_state.reset = True
    st.rerun()

if generate:
    if not article.strip():
        st.warning("Please paste your article content.")
    else:
        keywords = [kw.strip() for kw in keywords_input.split(",") if kw.strip()] if keywords_input else None

        extra_reqd_clean = extra_reqd.strip() if extra_reqd else None


        with st.spinner("Generating headlines..."):
            try:
                headlines = generate_headlines(
                    article=article,
                    tone=tone or None,
                    max_words=max_words,
                    keywords=keywords,
                    platform=platform or None,
                    headline_type=headline_type or None,
                    audience_type=audience_type or None,
                    num_variants=num_variants,
                    extra_reqd=extra_reqd
                )
                st.markdown("### 📢 Generated Headlines")
                st.code(headlines)
            except Exception as e:
                st.error(f"An error occurred: {e}")


