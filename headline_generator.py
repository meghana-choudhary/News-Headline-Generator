from typing import List, Optional
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI  
import os 
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY") 

def generate_headlines(
    article: str,
    tone: Optional[str] = None,
    max_words: Optional[int] = 12,
    keywords: Optional[List[str]] = None,
    platform: Optional[str] = None,
    headline_type: Optional[str] = None,
    audience_type: Optional[str] = None,
    num_variants: int = 3,
) -> str:
    tone_part = f" in a {tone} tone" if tone else ""
    platform_part = f" suitable for {platform}" if platform else ""
    length_part = f" Keep the headline close to and under {max_words} words." if max_words else ""
    keyword_part = f" Try to include the following keywords: {', '.join(keywords)}." if keywords else ""
    headline_type_part = f" The headline style should be {headline_type}." if headline_type else ""
    audience_type_part = f" Tailor the headlines for {audience_type}." if audience_type else ""

    prompt_template = PromptTemplate(
        input_variables=[
            "article", "num_variants", "tone_part", "platform_part",
            "length_part", "keyword_part", "headline_type_part", "audience_type_part"
        ],
        template="""
You are a professional headline writer for digital media platforms.

Your task is to write {num_variants} compelling, concise, and relevant headlines{tone_part}{platform_part}.
The headlines should accurately summarize the article without exaggeration or hallucination.
{length_part}
{keyword_part}
{headline_type_part}
{audience_type_part}

Article:
\"\"\" 
{article}
\"\"\"

Output format:
1. [Headline 1]
2. [Headline 2]
3. [Headline 3]
""",
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-preview-04-17", temperature=0.2, api_key=api_key
    )
    chain = LLMChain(llm=llm, prompt=prompt_template)

    response = chain.run(
        article=article,
        num_variants=num_variants,
        tone_part=tone_part,
        platform_part=platform_part,
        length_part=length_part,
        keyword_part=keyword_part,
        headline_type_part=headline_type_part,
        audience_type_part=audience_type_part,
    )

    return response.strip()

