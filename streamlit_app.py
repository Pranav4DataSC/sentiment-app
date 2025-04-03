import streamlit as st
from textblob import TextBlob

def main():
    st.title("Sentiment Analysis Web App")
    st.subheader("Enter your text below:")

    user_input = st.text_area("Your Text:")
    
    if st.button("Analyze Sentiment"):
        result = analyze_sentiment(user_input)
        st.write("Sentiment:", result)

def analyze_sentiment(text):
    # Your sentiment analysis logic goes here
    # This could be achieved using various libraries like NLTK, TextBlob, or transformers
    # For simplicity, let's assume a basic example
    if "happy" in text.lower():
        return "Positive"
    elif "sad" in text.lower():
        return "Negative"
    else:
        return "Neutral"

if __name__ == "__main__":
    main()

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

def main():
    st.title("Sentiment Analysis Web App")
    st.subheader("Enter your text below:")

    user_input = st.text_area("Your Text:")

    if st.button("Analyze Sentiment"):
        result = analyze_sentiment(user_input)
        st.write("Sentiment:", result)
        display_sentiment_emoji(result)

def display_sentiment_emoji(sentiment):
    emojis = {"Positive": "😊", "Negative": "😢", "Neutral": "😐"}
    st.write(f"Sentiment Emoji: {emojis.get(sentiment, '🤔')}")

