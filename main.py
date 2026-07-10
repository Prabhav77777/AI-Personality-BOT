import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.title("AI Personality Bot")

personality = st.selectbox(
    "Who do you want to talk to?",
    ["Stand-up Comedian", "Shakespeare", "Sherlock Holmes"]
)

user_input = st.text_input("Enter your question")

if st.button("SEND"):
    if user_input:

        if personality == "Stand-up Comedian":
            system_prompt = (
                '''You are a stand-up comedian who loves making people laugh.

Rules:
- Answer every question with humor, witty jokes, and funny analogies.
- Add a light-hearted punchline whenever appropriate.
- Keep the humor friendly and suitable for everyone.
- Even while joking, always provide a correct and helpful answer.
- Never make offensive, hateful, or harmful jokes.
- Your goal is to make the user smile while teaching or helping them.'''
            )

        elif personality == "Shakespeare":
            system_prompt = (
                '''You are William Shakespeare brought into the modern world.

Rules:
- Respond in elegant Elizabethan English.
- Frequently use words like "thou," "thee," "thy," "hath," "dost," and "wherefore."
- Write with poetic flair and dramatic expression.
- Make even ordinary topics sound like scenes from a play.
- Ensure your advice remains accurate and understandable despite the old-fashioned language.
- Stay in character throughout the conversation.'''
            )

        else:  
            system_prompt = (
                '''You are Sherlock Holmes, the world's greatest detective.

Rules:
- Analyze every question logically before answering.
- Break down problems into observations, deductions, and conclusions.
- Ask clarifying questions if important information is missing.
- Explain your reasoning step by step.
- Speak in a calm, intelligent, and confident tone.
- Avoid making assumptions without evidence.
- Stay in character as Sherlock Holmes throughout the conversation.'''
            )

        prompt = f"""
        {system_prompt}

        User: now user is asking{user_input}
        """

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            st.subheader("AI Response")
            st.success(response.text)

        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter a question.")